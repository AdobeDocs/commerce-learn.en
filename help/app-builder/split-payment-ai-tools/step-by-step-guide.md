---
title: Split payment POC step-by-step implementation guide
description: Learn how to implement the split payment POC in order after setup completes, covering module, environments, orchestrator, verification, and optional UI.
feature: App Builder, Eventing, Extensibility
topic: Commerce, Architecture, App Builder, Development
role: Developer
level: Intermediate
doc-type: Tutorial
duration: 480
jira: KT-20902
last-substantial-update: 2026-04-30
---
# Split payment POC step-by-step implementation guide

This page is your implementation checklist. It assumes you have already watched the [overview](./overview.md) and the [full demo](./full-demo.md), and that your Commerce site and App Builder project are both ready. The individual tutorial pages contain full detail for every topic below — use this page to know what to do and in what order.

## Before you start

Confirm all of the following before running any prompt or command. The [prerequisites and setup](./prerequisites-and-setup.md) page covers each item in detail.

**Commerce side**

* [ ] Adobe Commerce 2.4.5 or later
* [ ] I/O eventing enabled and deployed (Commerce Cloud only — requires `ENABLE_EVENTING: true` in `.magento.env.yaml`)
* [ ] **Cash on Delivery** enabled in Admin with its title set exactly to `Cash`
* [ ] Store credit enabled in Admin
* [ ] Test customer has at least $50 store credit
* [ ] Commerce integration created, activated, and all four OAuth values saved securely

**App Builder side**

* [ ] App Builder project exists in Adobe Developer Console
* [ ] Adobe I/O Events service added to the workspace
* [ ] Commerce connected as an event provider
* [ ] `aio login` complete; correct workspace selected with `aio app use`
* [ ] Node.js 18 or later installed; `aio` CLI installed (`npm install -g @adobe/aio-cli`)

If anything above is missing, stop here and complete it first.

## Phase 1 — Build the Commerce module

**What this does:** Generates the `Client_SplitPayment` PHP module that handles the checkout UI, store credit application, REST endpoints, and the I/O event subscription. This is the thin in-Commerce adapter — all operator workflow stays in App Builder.

### Step 1.1 — Customize the prompt for your project

Open the [Commerce module AI prompt](./commerce-module-prompt.md) page and note the following before you copy the prompt:

* Replace `Client` with your real vendor name in the prompt
* Replace `SplitPayment` if you want a different module name
* If your theme is not Luma, the `LayoutProcessorPlugin` injection path and RequireJS mappings may need adjusting
* If your Cash on Delivery method uses a code other than `cashondelivery`, update `payment-method-helper.js`

### Step 1.2 — Run the prompt

Copy the full prompt from **PROMPT START** to **End of prompt** and paste it into Cursor (with Claude) or directly into Claude. Run it from the root of your Commerce project so the AI can create files under `app/code/`.

### Step 1.3 — Enable and install the module

Run these commands from your Commerce project root:

```bash
bin/magento module:enable Client_SplitPayment
bin/magento setup:upgrade
bin/magento setup:di:compile
bin/magento setup:static-content:deploy -f
bin/magento cache:flush
```

### Step 1.4 — Verify the module installed correctly

```bash
# Confirm the module is active
bin/magento module:status Client_SplitPayment

# Confirm the split_ columns were added to sales_order
mysql -u <user> -p <dbname> -e "DESCRIBE sales_order;" | grep split
```

You should see five columns: `split_store_credit_amount`, `split_cash_amount`, `split_cash_status`, `split_sc_invoice_id`, and `split_cash_invoice_id`.

Then confirm in a browser that the split payment fields appear at checkout when a logged-in customer with store credit selects **Cash** as the payment method.

## Phase 2 — Configure environment variables

**What this does:** Prepares the credential files used by the App Builder orchestrator, the simulation script, and (optionally) the Experience Cloud UI extension. The same four OAuth values from your Commerce integration are used in every `.env` file.

Refer to the [environment variables reference](./env-reference.md) for the complete list of variables per component.

### Step 2.1 — Create the orchestrator `.env`

In your `split-payment-orchestrator/` directory:

```bash
cp .env.example .env
```

Fill in every value:

| Variable | Where to get it |
|---|---|
| `COMMERCE_BASE_URL` | Your store URL — no trailing slash |
| `COMMERCE_CONSUMER_KEY` | Commerce Admin > System > Integrations |
| `COMMERCE_CONSUMER_SECRET` | Same — only shown at activation |
| `COMMERCE_ACCESS_TOKEN` | Same |
| `COMMERCE_ACCESS_TOKEN_SECRET` | Same |
| `PAYMENT_THRESHOLD` | Must match `split_payment/general/threshold` in Commerce (default: `100`) |
| `DEMO_UI_SECRET` | Optional — if set, required as `?secret=` in the dashboard URL |

### Step 2.2 — Create the simulation script `.env`

```bash
cp commerce-backend-ui-1/.env.simulation.example commerce-backend-ui-1/.env.simulation
```

Fill in `COMMERCE_BASE_URL` and the four OAuth values (same credentials as above).

## Phase 3 — Build the App Builder orchestrator

**What this does:** Generates the `split-payment-orchestrator` App Builder project: the `payment-orchestrator` I/O Event consumer, the `payment-accept` and `payment-decline` web actions, and the `demo-dashboard` operator UI.

### Step 3.1 — Run the orchestrator prompt

Open the [App Builder orchestrator AI prompt](./orchestrator-prompt.md) page. Copy the full prompt and run it from the `split-payment-orchestrator/` directory.

### Step 3.2 — Install dependencies and deploy

```bash
cd split-payment-orchestrator
npm install
# Confirm .env is filled in (from Phase 2, Step 2.1)
aio app deploy
```

After deployment, `aio app deploy` prints the action URLs. Note the `demo-dashboard` URL — you need it in Phase 4.

### Step 3.3 — Confirm the event registration

In Adobe Developer Console, open your App Builder project workspace. Under **Events**, confirm that the `Split payment — sales order place before` registration exists and is bound to the `payment-orchestrator` action.

## Phase 4 — Test the complete flow

Work through the verification steps in order. The [testing and verification guide](./testing-and-verification.md) has the full curl commands, simulation script usage, and troubleshooting reference for each step below.

### Step 4.1 — Verify REST endpoints are routable

```bash
# Expect 401, not 404 — the endpoint exists but requires auth
curl -X POST https://your-store.example.com/rest/V1/split-payment/orders/1/cash-received
```

### Step 4.2 — Test the checkout UI

1. Log in to the storefront as your test customer (the one with store credit)
2. Add a product to cart with a total under $100 after shipping and tax
3. At the payment step, select **Cash**
4. Confirm the split payment fields appear: balance shown, cash pre-filled, store credit at $0
5. Reduce the cash amount and confirm the store credit portion updates correctly

### Step 4.3 — Test the threshold guard

Add products totaling more than $100, proceed to checkout, select Cash, and attempt to place the order. The error `"Payment could not be processed. Please try again or contact support."` must appear.

### Step 4.4 — Place a test split payment order

Build a cart under $100, enter a cash/store credit split, and place the order. In Commerce Admin, confirm:

* Order status is `pending_payment`
* Two comments from App Builder are visible on the order:
  1. `"Cash payment of $X.XX pending. Awaiting admin confirmation."`
  2. `"Split payment orchestration completed. Order awaiting cash confirmation."`

If no App Builder comments appear, check logs with `aio app logs` before continuing.

### Step 4.5 — Test accept via simulation script

```bash
# Find your order's entity_id
node commerce-backend-ui-1/scripts/simulate-split-payment.mjs list

# Accept the payment
node commerce-backend-ui-1/scripts/simulate-split-payment.mjs accept <entity_id>
```

In Commerce Admin, confirm:

* Order status changed to `processing`
* History comment: `"Cash payment of $X.XX received."`
* Cash invoice visible on the Invoices tab
* Shipment visible on the Shipments tab (if applicable)

### Step 4.6 — Test decline via simulation script

Place another test order, then:

```bash
node commerce-backend-ui-1/scripts/simulate-split-payment.mjs decline <entity_id>
```

Confirm order status is `canceled` and `split_cash_status` is `declined`.

### Step 4.7 — Test the demo dashboard

Open the dashboard URL from Step 3.2. With a pending order in the system:

1. Confirm the order appears in the pending list
2. Click **Accept** and confirm the order moves to `processing` in Commerce
3. Place a fresh order, return to the dashboard, and click **Decline** — confirm cancellation

## Phase 5 (optional) — Add the Experience Cloud UI extension

This phase embeds the operator dashboard into the Commerce Admin shell instead of using the standalone `demo-dashboard`. Skip this phase if the standalone dashboard meets your needs.

### Step 5.1 — Review the prerequisites

The Experience Cloud UI extension requires IMS credentials in addition to the OAuth integration values. Read the [Experience Cloud UI extension AI prompt](./experience-cloud-ui-prompt.md) page before running the prompt, paying attention to the `OAUTH_CLIENT_ID` and related IMS variables.

### Step 5.2 — Run the UI extension prompt

Copy the full prompt from **PROMPT START** to **End of prompt** and run it from the `commerce-checkout-starter-kit/` directory.

### Step 5.3 — Deploy

```bash
cd commerce-checkout-starter-kit
npm install
cp .env.dist .env
# Fill in IMS credentials and COMMERCE_INTEGRATION_* credentials
aio app deploy
```

## Quick troubleshooting reference

| Symptom | First thing to check |
|---|---|
| Split payment fields do not appear at checkout | RequireJS errors in the browser console; also run `bin/magento cache:flush` |
| `"Payment could not be processed"` at place order | `PlaceOrderPlugin` or `BalanceManagementInterface` — add temporary debug logging in `PlaceOrderPlugin` |
| No App Builder comments on the order | Run `aio app logs` to see if the event fired and what the action returned |
| `403` from Commerce REST in App Builder | Fastly IP allowlisting — test with the simulation script first; if that works, the issue is egress IP blocking |
| `"The signature is invalid"` from Commerce | Confirm `COMMERCE_BASE_URL` has no trailing slash; confirm the integration is activated |
| Orders do not appear in demo dashboard | Check that `extension_attributes.split_cash_status` appears in a direct `GET /rest/V1/orders` response |

For full troubleshooting details, see the [testing and verification guide](./testing-and-verification.md#common-issues-and-fixes).

{{$include /help/_includes/split-payment-ai-tools-related-links.md}}
