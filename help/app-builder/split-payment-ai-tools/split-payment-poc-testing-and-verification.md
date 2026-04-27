---
title: "Split payment POC: testing and verification guide"
description: Learn how to verify the split payment POC: Commerce install, REST, checkout, threshold, simulation accept and decline, demo dashboard, and App Builder logs.
feature: App Builder, Configuration, Extensibility, Paas, Payments, REST, Orders
topic: App Builder, Commerce, Development, I/O Events, Integrations, Runtime
role: Developer, Leader, User
level: Intermediate
doc-type: Tutorial
duration: 411
jira: KT-20902
last-substantial-update: 2026-04-27
---
# Split payment POC: testing and verification guide

This guide walks you through verifying that every component works correctly, in the order they should be tested. Start from the bottom (Commerce module) and work up (App Builder).

---

## Step 1 — Verify Commerce Module Installation

After running `bin/magento setup:upgrade` and `bin/magento setup:di:compile`:

```bash
# Confirm module is enabled
bin/magento module:status Client_SplitPayment

# Confirm db_schema columns were added
bin/magento doctrine:schema:validate
# or check directly:
mysql -u <user> -p <dbname> -e "DESCRIBE sales_order;" | grep split
```

Expected output: four columns starting with `split_` visible in `sales_order`.

---

## Step 2 — Verify Commerce Admin Configuration

In Commerce Admin:
1. **[!UICONTROL Stores]** > **[!UICONTROL Configuration]** > **[!UICONTROL Sales]** > **[!UICONTROL Payment Methods]** — confirm **[!UICONTROL Cash On Delivery]** is enabled with title `Cash`
2. **[!UICONTROL Stores]** > **[!UICONTROL Configuration]** > **[!UICONTROL Customers]** > **[!UICONTROL Customer Configuration]** > **[!UICONTROL Store Credit Options]** — confirm enabled
3. Confirm your test customer has store credit: **[!UICONTROL Customers]** > **[!UICONTROL All Customers]** > *[customer]* > **[!UICONTROL Store Credit]**

---

## Step 3 — Verify REST Endpoints Are Accessible

Use curl to confirm the endpoints respond (they will reject unauthorized requests, but a 401 confirms they're routed correctly):

```bash
# Should return 401 (not 404) — endpoint exists but requires auth
curl -X POST https://your-store.example.com/rest/V1/split-payment/orders/1/cash-received

# Should return 200 or session-based response — anonymous endpoint
curl -X POST https://your-store.example.com/rest/V1/split-payment/set \
  -H "Content-Type: application/json" \
  -d '{"storeCreditAmount": 0, "cashAmount": 0}'
```

---

## Step 4 — Test the Checkout UI

1. Log in to the storefront as your test customer (who has store credit)
2. Add a product to cart (total under $100 after shipping + tax)
3. Proceed to checkout
4. At the payment step, select **Cash** (or Cash On Delivery)
5. Verify the split payment fields appear:
   * Your store credit balance shown
   * Cash amount field pre-filled with the order total
   * "Store credit toward this order" field showing $0.00 (since cash = full order total)
6. Reduce the cash amount (e.g., enter $10 for a $50 order)
7. Verify the store credit portion updates to $40.00
8. Verify the message appears: `"The remaining $40.00 will automatically be applied from your store credit."`

**Test validation:**
* Enter a cash amount greater than the order total → error message
* Enter a cash amount that requires more store credit than available → error message
* Enter cash = 0 → error (or store credit covers entire order)

---

## Step 5 — Test Threshold Guard

1. Add products totaling more than $100 (subtotal + shipping + tax > $100)
2. Proceed to checkout, select **Cash**
3. Attempt to place the order
4. Verify the error message appears: `"Payment could not be processed. Please try again or contact support."`
5. Verify the cart is preserved (customer can still adjust cart and try again)

---

## Step 6 — Place a Test Split Payment Order

1. Build a cart under $100 (logged in customer with store credit)
2. Select Cash at checkout
3. Enter a cash amount less than the order total (e.g., $10 of a $45 order)
4. Confirm the store credit message appears
5. Click **Place Order**

After order placement, verify in Commerce Admin:
* Order is in `pending_payment` status
* Order has two history comments:
  1. `"Cash payment of $X.XX pending. Awaiting admin confirmation."` (from App Builder `payment-orchestrator`)
  2. `"Split payment orchestration completed. Order awaiting cash confirmation."` (from App Builder)
* The split payment amounts are visible in the order payment block

> **If no App Builder comments appear:** Check App Builder action logs with `aio app logs`. The event may not have fired or the action may have an error.

---

## Step 7 — Test Accept via Simulation Script

The simulation script is the fastest way to test the accept/decline flow without the full operator UI.

```bash
cd commerce-checkout-starter-kit
cp commerce-backend-ui-1/.env.simulation.example commerce-backend-ui-1/.env.simulation
# Edit .env.simulation with your credentials

# List recent orders (find your test order entity_id)
node commerce-backend-ui-1/scripts/simulate-split-payment.mjs list

# Show split payment fields for a specific order
node commerce-backend-ui-1/scripts/simulate-split-payment.mjs show 42

# Accept the cash payment
node commerce-backend-ui-1/scripts/simulate-split-payment.mjs accept 42
```

After accept, verify in Commerce Admin order view:
* Order status is `processing`
* History comment: `"Cash payment of $X.XX received."`
* Cash invoice created (visible in Invoices tab)
* Shipment created (visible in Shipments tab, if applicable)
* History comment: `"Split payment: cash portion invoiced #XXXXXXXX."`
* History comment: `"Split payment: shipment created after cash was accepted (App Builder / API)."`

---

## Step 8 — Test Decline via Simulation Script

Place another test order (same setup as Step 6), then:

```bash
node commerce-backend-ui-1/scripts/simulate-split-payment.mjs decline <orderId>
```

After decline, verify in Commerce Admin:
* Order status is `canceled`
* History comment: `"Cash payment declined (simulated fraud check)."`
* `split_cash_status` = `declined`

---

## Step 9 — Test the Demo Dashboard

After deploying the `split-payment-orchestrator`, `aio app deploy` prints the action URLs.

Open the `demo-dashboard` URL in a browser:
```
https://[runtime-host]/api/v1/web/split_payment_orchestrator/demo-dashboard
```

If `DEMO_UI_SECRET` is set:
```
https://[runtime-host]/api/v1/web/split_payment_orchestrator/demo-dashboard?secret=<your-secret>
```

With a pending order:
1. The dashboard should show the order in the pending list
2. Click **Accept** → order should move to `processing` in Commerce
3. Place another order; click **Decline** → order should be `canceled` in Commerce

---

## Step 10 — Test App Builder Action Logs

```bash
# Follow logs in real-time
aio app logs --tail

# Or view last invocations
aio runtime activation list --limit 10
aio runtime activation logs <activation-id>
```

For the `payment-orchestrator`, look for:
```
[INFO] Split payment orchestration finished { orderId: '42' }
```

For `payment-accept` or `payment-decline`:
```
[INFO] Cash payment accepted on Commerce via REST { orderId: '42' }
```

---

## Common Issues and Fixes

### "The signature is invalid" from Commerce OAuth

**Cause:** Clock skew between App Builder runtime and Commerce, or an OAuth signing bug.

**Fix:**
* Confirm `COMMERCE_BASE_URL` has no trailing slash
* Confirm the four OAuth credentials are for an _activated_ integration
* Test with the simulation script first — if the script works but App Builder doesn't, it's likely an env variable not loaded (check `aio app deploy` output for missing env vars)

### Split payment fields not appearing in checkout

**Cause:** LayoutProcessorPlugin injection paths don't match your checkout layout.

**Fix:**
* Check the browser console for RequireJS errors loading `Client_SplitPayment/js/view/payment/split-payment`
* Check `bin/magento setup:static-content:deploy` completed successfully
* Flush cache: `bin/magento cache:flush`
* If your theme has a custom checkout, the `LayoutProcessorPlugin` path to inject the component may need adjustment

### Store credit not applying / "Payment could not be processed" at place order

**Cause:** Usually one of the edge case plugins not working correctly.

**Check:**
1. Is `SplitPaymentSession` returning the correct amounts? Add temporary debug logging in `PlaceOrderPlugin`
2. Is `FixSplitPaymentGrandTotalPlugin` running and affecting the quote total before `BalanceManagementInterface::apply()` is called? The `beginBalanceApply()` flag should suppress it.
3. Is the customer balance module enabled in Commerce?

### App Builder action receives event but orderId is missing

**Cause:** The `io_events.xml` field list doesn't include `entity_id`, or the event payload shape changed.

**Fix:**
* Confirm `io_events.xml` includes `entity_id` in the field list
* In the action, log `JSON.stringify(params)` temporarily to see the full payload shape
* Check that the `extractValue()` function is finding the right nesting level

### Orders don't show in demo dashboard

**Cause:** Commerce REST `orders` search criteria not returning orders, or `split_cash_status` field not in the REST response.

**Fix:**
* Confirm `OrderRepositoryPlugin` is loading extension attributes correctly
* Test directly: `GET /rest/V1/orders?searchCriteria[pageSize]=5` and check if `extension_attributes.split_cash_status` appears in the response
* Check that `extension_attributes.xml` is correctly declaring the `split_cash_status` attribute on `OrderInterface`

---

## Verification Checklist

* [ ] `split_*` columns visible in `sales_order` table
* [ ] REST endpoints return 401 (not 404) when called without auth
* [ ] Split payment UI renders at checkout when Cash is selected
* [ ] Validation messages work (overpayment, insufficient credit)
* [ ] Threshold guard blocks orders > $100
* [ ] Placed order has `pending_payment` status and App Builder comments
* [ ] `simulate-split-payment.mjs list` shows the test order with split amounts
* [ ] `simulate-split-payment.mjs accept <id>` moves order to `processing` with invoice and shipment
* [ ] `simulate-split-payment.mjs decline <id>` cancels the order
* [ ] Demo dashboard lists pending orders and accept/decline work from the UI


{{$include /help/_includes/split-payment-ai-tools-related-links.md}}
