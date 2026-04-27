---
title: "Split payment POC: Experience Cloud UI extension AI prompt"
description: Learn how to use this optional prompt to embed split payment in Commerce Admin: Admin UI SDK, IMS, OAuth, accept and decline, and the simulation script.
feature: App Builder, Admin Workspace, Extensibility, Paas, REST
topic: App Builder, Commerce, Development, I/O Events, Integrations, Runtime
role: Developer, Leader, User
level: Intermediate
doc-type: Tutorial
duration: 239
jira: KT-20902
last-substantial-update: 2026-04-27
---
# Split payment POC: Experience Cloud UI extension AI prompt

This is the optional step that embeds a split payment orders panel in the **[!UICONTROL Adobe Commerce]** Admin shell (Experience Cloud) using the `commerce-checkout-starter-kit` and the `commerce-backend-ui-1` pattern. The standalone [demo dashboard](split-payment-poc-app-builder-orchestrator-prompt.md) from the App Builder orchestrator covers the same accept and decline flow without Admin shell integration.

## How to use this prompt

Copy everything from **PROMPT START** to **End of prompt** into Cursor or Claude. Run the prompt from the `commerce-checkout-starter-kit/` directory.

## Before you run

* This path needs **IMS** credentials in addition to the OAuth values (see [Split payment POC: environment variables reference](split-payment-poc-env-reference.md) for the `commerce-checkout-starter-kit` variables).
* Complete [Split payment POC: App Builder orchestrator AI prompt](split-payment-poc-app-builder-orchestrator-prompt.md) first if you want the same `payment-accept` and `payment-decline` behavior to compare; the UI extension reuses that logic with `COMMERCE_INTEGRATION_*` env names.

---

## The prompt

**PROMPT START**


You are generating the `commerce-backend-ui-1` Admin UI SDK extension for the split payment PoC. This extension embeds a split payment orders dashboard into the Adobe Commerce Admin Shell using the `@adobe/aio-app-dev-toolkit` and `@adobe/commerce-backend-ui-1` patterns from the Commerce Checkout Starter Kit.

**Base project:** `commerce-checkout-starter-kit/`
**Extension directory:** `commerce-checkout-starter-kit/commerce-backend-ui-1/`

---

### What This Extension Provides

1. **Admin order grid panel** — a custom menu item in the Commerce Admin Shell listing split payment orders with `split_cash_status = 'pending'`
2. **Order detail view** — shows split payment breakdown (cash amount, store credit amount, status) alongside the order
3. **Accept / Decline actions** — buttons that call the `payment-accept` and `payment-decline` App Builder actions via OAuth 1.0a

---

### File Structure to Generate

```
commerce-checkout-starter-kit/commerce-backend-ui-1/
├── ext.config.yaml
├── README.md
├── .env.simulation.example
├── actions/
│   ├── utils.js
│   ├── commerce/
│   │   └── index.js           ← IMS-based Commerce REST (order listing)
│   ├── payment-accept/
│   │   ├── commerce-client.js ← OAuth 1.0a (accept/decline)
│   │   └── index.js
│   ├── payment-decline/
│   │   └── index.js
│   └── registration/
│       └── index.js
├── scripts/
│   ├── README.md
│   └── simulate-split-payment.mjs
└── web-src/
    ├── index.html
    ├── package.json
    ├── .parcelrc
    └── src/
        ├── index.jsx
        ├── index.css
        ├── utils.js
        ├── exc-runtime.js
        ├── config.json
        ├── constants/
        │   └── extension.js
        ├── components/
        │   ├── App.jsx
        │   ├── ExtensionRegistration.jsx
        │   ├── MainPage.jsx
        │   ├── SplitPaymentDashboard.jsx
        │   └── SplitPaymentOrderDetail.jsx
        └── hooks/
            └── useSplitPaymentOrders.js
```

---

### Backend Actions

**`actions/commerce/index.js`** — IMS-authenticated Commerce REST
* Uses the IMS token provided by the Admin UI SDK context to call Commerce REST
* Fetches order list with `split_cash_status` filter
* Returns the order list as JSON

**`actions/payment-accept/commerce-client.js`** — OAuth 1.0a client
* Same implementation as `split-payment-orchestrator/actions/payment-orchestrator/commerce-client.js`
* Uses `COMMERCE_INTEGRATION_*` prefixed env vars (to distinguish from IMS credentials)

**`actions/payment-accept/index.js`** — Accept action
* Same logic as `split-payment-orchestrator/actions/payment-accept/index.js`
* Calls `POST /V1/split-payment/orders/:orderId/cash-received` via OAuth 1.0a

**`actions/payment-decline/index.js`** — Decline action
* Calls `POST /V1/split-payment/orders/:orderId/cash-decline`

**`actions/registration/index.js`** — Admin UI SDK registration
* Registers the extension with the Commerce Admin Shell
* Adds a menu item under Orders for the split payment dashboard

---

### React Frontend Components

**`SplitPaymentDashboard.jsx`**
* Lists pending split payment orders in a Spectrum-styled table
* Columns: Order # (increment_id), Date, Customer, Cash Due, Store Credit, Status
* Accept and Decline buttons per row
* Calls backend actions via `web-src/src/utils.js` fetch helpers
* Shows loading/error states; refreshes on action completion

**`SplitPaymentOrderDetail.jsx`**
* Shows split payment detail for a single order
* Displays: cash amount, store credit amount, current split_cash_status

**`useSplitPaymentOrders.js`** — React hook
* Fetches split payment orders from `actions/commerce/index.js`
* Returns `{ orders, loading, error, refresh }`

---

### Simulation Script

**`scripts/simulate-split-payment.mjs`**

A Node.js ESM script for testing Commerce REST calls directly (without going through App Builder). Uses the same OAuth 1.0a signing as the App Builder actions.

Commands:
* `node simulate-split-payment.mjs help` — show usage
* `node simulate-split-payment.mjs list` — list recent orders with split payment data
* `node simulate-split-payment.mjs show <orderId>` — show split payment fields for a specific order (entity_id)
* `node simulate-split-payment.mjs accept <orderId>` — call `cash-received` endpoint
* `node simulate-split-payment.mjs decline <orderId>` — call `cash-decline` endpoint

Reads credentials from `commerce-backend-ui-1/.env.simulation` (copy from `.env.simulation.example`).

**`.env.simulation.example`:**
```dotenv
COMMERCE_BASE_URL=https://your-store.example.com
COMMERCE_CONSUMER_KEY=
COMMERCE_CONSUMER_SECRET=
COMMERCE_ACCESS_TOKEN=
COMMERCE_ACCESS_TOKEN_SECRET=
```

---

### `ext.config.yaml`

Configure the extension with:
* The `commerce-backend-ui-1` extension type
* The four backend actions (`commerce`, `payment-accept`, `payment-decline`, `registration`)
* `require-adobe-auth: true` for all actions except `registration`
* Input bindings from env for `COMMERCE_INTEGRATION_*` credentials

---

### After Generating Files

```bash
cd commerce-checkout-starter-kit
npm install
cp .env.dist .env
# Fill in IMS credentials and COMMERCE_INTEGRATION_* credentials
aio app deploy
```

### End of prompt


{{$include /help/_includes/split-payment-ai-tools-related-links.md}}
