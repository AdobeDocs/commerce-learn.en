---
title: Split payment POC — App Builder orchestrator AI prompt
description: "Learn how to use this prompt to build the split-payment-orchestrator app. I/O events, payment-orchestrator, web actions, demo dashboard, and aio app deploy."
feature: App Builder, Configuration, Eventing, Extensibility, Paas, REST
topic: App Builder, Commerce, Development, I/O Events, Integrations, Runtime
role: Developer, User
level: Intermediate
doc-type: Tutorial
duration: 421
jira: KT-20902
last-substantial-update: 2026-04-27
---
# Split payment POC: App Builder orchestrator AI prompt

Use this page to copy the full prompt that generates the **split-payment-orchestrator** project: the **payment-orchestrator** I/O Event consumer, **payment-accept** and **payment-decline** web actions, the **demo-dashboard**, and the Commerce REST client.

## How to use this prompt

Copy everything from **PROMPT START** to **End of prompt** into Cursor (with Claude) or directly into Claude. Run the prompt from the `split-payment-orchestrator/` directory (the App Builder project root).

## Before you run

* Finish [Split payment POC: prerequisites and environment setup](./prerequisites-and-setup.md).
* Have your [Split payment POC: environment variables reference](./env-reference.md) and `.env` file ready in the project.


## The prompt

**PROMPT START**


You are generating a complete Adobe App Builder application for orchestrating split payments in Adobe Commerce. This application receives I/O Events from Commerce, processes split payment decisions, and calls back into Commerce via REST.

**Project:** `split-payment-orchestrator`
**Runtime:** Node.js 18
**Key dependencies:** `@adobe/aio-sdk ^6.0.0`, `got ^11.8.6`, `oauth-1.0a ^2.2.6`

Generate all files listed below. The application must work with Adobe I/O Runtime (`aio app deploy`).


### File Structure to Generate

```
split-payment-orchestrator/
├── package.json
├── app.config.yaml
├── .env.example
└── actions/
    ├── payment-orchestrator/
    │   ├── index.js         ← I/O Event entry point
    │   ├── commerce-client.js
    │   ├── threshold.js
    │   ├── cash-payment.js
    │   ├── order-update.js
    │   └── store-credit.js  ← Deprecated stub; kept for reference
    ├── payment-accept/
    │   └── index.js
    ├── payment-decline/
    │   └── index.js
    └── demo-dashboard/
        └── index.js
```


### `package.json`

```json
{
  "name": "split-payment-orchestrator",
  "version": "1.0.0",
  "private": true,
  "description": "Adobe App Builder action — split payment PoC orchestrator",
  "engines": { "node": ">=18" },
  "scripts": {
    "deploy": "NODE_OPTIONS=--disable-warning=DEP0040 aio app deploy",
    "aio": "NODE_OPTIONS=--disable-warning=DEP0040 aio"
  },
  "dependencies": {
    "@adobe/aio-sdk": "^6.0.0",
    "@adobe/exc-app": "^1.5.9",
    "got": "^11.8.6",
    "oauth-1.0a": "^2.2.6"
  }
}
```


### `app.config.yaml`

Define four actions in the `split_payment_orchestrator` package:

**`payment-orchestrator`**
* `web: "no"` (I/O Event trigger only — not directly callable via HTTP)
* `runtime: nodejs:18`
* `require-adobe-auth: true`, `final: true`
* Inputs from env: `LOG_LEVEL`, `COMMERCE_BASE_URL`, `COMMERCE_CONSUMER_KEY`, `COMMERCE_CONSUMER_SECRET`, `COMMERCE_ACCESS_TOKEN`, `COMMERCE_ACCESS_TOKEN_SECRET`, `PAYMENT_THRESHOLD`

**`payment-accept`**
* `web: "yes"` (HTTP web action — callable by dashboard or ERP)
* `runtime: nodejs:18`
* `require-adobe-auth: true`, `final: true`
* Same Commerce credential inputs (no `PAYMENT_THRESHOLD`)

**`payment-decline`**
* `web: "yes"`
* `runtime: nodejs:18`
* `require-adobe-auth: true`, `final: true`
* Same Commerce credential inputs

**`demo-dashboard`**
* `web: "yes"`
* `runtime: nodejs:18`
* `require-adobe-auth: false` ← Dashboard is publicly accessible (protected only by `DEMO_UI_SECRET` if set)
* Inputs: all Commerce credentials + `DEMO_UI_SECRET`, `DEMO_UI_BASE_URL`

**Events registration** (under `events.registrations`):

```yaml
Split payment — sales order place before:
  description: Invokes payment-orchestrator when an order is about to be placed
  events_of_interest:
    - provider_metadata: dx_commerce_events
      event_codes:
        - com.adobe.commerce.observer.sales_order_place_before
  runtime_action: split_payment_orchestrator/payment-orchestrator
```


### `actions/payment-orchestrator/commerce-client.js`

Shared OAuth 1.0a REST client for Adobe Commerce. Implements:

**`createCommerceClient(params, logger)`** — returns `{ request, baseUrl }`

* Reads `COMMERCE_BASE_URL`, `COMMERCE_CONSUMER_KEY`, `COMMERCE_CONSUMER_SECRET`, `COMMERCE_ACCESS_TOKEN`, `COMMERCE_ACCESS_TOKEN_SECRET` from `params`
* Throws if any credential is missing
* Uses `oauth-1.0a` with `HMAC-SHA256` (Node.js `crypto.createHmac`)
* Uses `got@11` (not `got@12+` — the project uses CJS) with `prefixUrl = ${baseUrl}/rest/V1/`
* Adds `Authorization` header via `beforeRequest` hook
* `request(method, path, options)` — normalizes the path (strips leading `/`), returns `{ statusCode, body }`
* `throwHttpErrors: false` — never throws on 4xx/5xx; always returns the status code


### `actions/payment-orchestrator/threshold.js`

**`evaluateThreshold({ orderTotal, storeCreditAmount, cashAmount, params, logger })`** — returns `{ pass: boolean, reason: string }`

Logic:
1. Read `params.PAYMENT_THRESHOLD`; parse as float; default to `100` if missing, NaN, or ≤ 0
2. If `orderTotal > threshold`: return `{ pass: false, reason: 'PAYMENT_THRESHOLD_EXCEEDED' }`
3. If `Math.abs((storeCreditAmount + cashAmount) - orderTotal) > 0.02`: return `{ pass: false, reason: 'SPLIT_AMOUNT_MISMATCH' }`
4. Otherwise: return `{ pass: true, reason: '' }`


### `actions/payment-orchestrator/cash-payment.js`

**`recordCashPending({ commerce, orderId, cashAmount, logger })`** — returns `{ ok: boolean, error? }`

* Calls `POST orders/${orderId}/comments` with:

  ```json
  {
    "statusHistory": {
      "comment": "Cash payment of $X.XX pending. Awaiting admin confirmation.",
      "entity_name": "order",
      "parent_id": "<orderId>",
      "is_visible_on_front": true,
      "is_customer_notified": false,
      "status": "pending_payment"
    }
  }
  ```
  
* Returns `{ ok: true }` on 2xx; returns `{ ok: false, error: { code, message } }` otherwise
* Wraps in try/catch; returns error object, never throws


### `actions/payment-orchestrator/order-update.js`

**`updateOrderAfterOrchestration({ commerce, orderId, success, detail, logger })`** — returns `{ ok: boolean, error? }`

* If `success`: posts a history comment `"Split payment orchestration completed. Order awaiting cash confirmation."`
* If `!success`: posts `"Payment could not be processed. Please try again or contact support."` — never include `detail` in the customer-visible comment; log `detail` internally only
* Returns `{ ok: boolean, error? }` — never throws


### `actions/payment-orchestrator/store-credit.js`

**`applyStoreCredit({ commerce, cartId, amount, logger })`** — deprecated no-op implementation

Include this file with a JSDoc `@deprecated` notice explaining:
> The orchestrator no longer applies store credit via REST. Store credit is applied at checkout in the Commerce PHP module (`PlaceOrderPlugin`) using `BalanceManagementInterface::apply()`, which requires an active cart. By the time App Builder receives the I/O Event, the cart is inactive. This file is kept for reference or for custom flows where store credit is applied post-order.

Keep a working implementation (same shape as other modules) so developers can study the pattern, but mark it clearly as not used in the current flow.


### `actions/payment-orchestrator/index.js`

I/O Event entry point. Implements `async function main(params)`.

**Payload extraction:**

Adobe Commerce I/O Events may deliver the payload in several shapes. Extract the order value object by checking these paths in order:
1. `params.__ow_body` (parse JSON string if needed) → `.event.data.value`
2. `params.data.value`
3. `params.value`
4. `params.body.event.data.value`
5. Fall back to `params` itself

**Field extraction from value:**
* `orderId = value.entity_id || value.id`
* `orderTotal = parseFloat(value.grand_total ?? value.base_grand_total ?? value.subtotal ?? '0')`
* Split amounts from `value.extension_attributes` (check both `extension_attributes` and `extensionAttributes`):
  * `storeCredit = parseFloat(ext.split_store_credit_amount ?? value.split_store_credit_amount ?? '0')`
  * `cash = parseFloat(ext.split_cash_amount ?? value.split_cash_amount ?? '0')`

**Flow:**
1. Extract value; if `orderId` is missing, log error and return `{ statusCode: 200, body: { ok: false, message: PUBLIC_ERROR } }`
2. Call `evaluateThreshold(...)` — if fails, log and return same 200 response
3. Call `createCommerceClient(params, logger)` — if fails, return 200 error
4. If `storeCredit > 0`, log that store credit was applied at checkout (no REST call needed)
5. Call `recordCashPending(...)` — if fails, call `updateOrderAfterOrchestration(..., success: false)` and return 200 error
6. Call `updateOrderAfterOrchestration(..., success: true)`
7. Return `{ statusCode: 200, body: { ok: true, message: 'processed' } }`

**Important:** Always return `statusCode: 200` — I/O Runtime will retry non-200 responses, which would cause duplicate order processing. Errors are reported in the body.

**`PUBLIC_ERROR` constant:** `"Payment could not be processed. Please try again or contact support."` — used for all external-facing error messages.


### `actions/payment-accept/index.js`

HTTP web action. Calls `POST /V1/split-payment/orders/:orderId/cash-received`.

**Order ID resolution:** Check `params.orderId`, then `params.payload.orderId`, then `params.__ow_body` (parsed JSON). Return 400 if missing.

**Flow:**
1. Resolve `orderId`; return 400 if missing
2. Init commerce client; return 500 if fails
3. Call `POST split-payment/orders/${orderId}/cash-received` with empty JSON body
4. If 2xx: return `{ statusCode: 200, body: { ok: true, orderId, message: 'accepted' } }`
5. If error: log and return `{ statusCode: 200, body: { ok: false, message: PUBLIC_ERROR } }`


### `actions/payment-decline/index.js`

HTTP web action. Same pattern as `payment-accept` but calls `POST /V1/split-payment/orders/:orderId/cash-decline`.

Return `{ ok: true, orderId, message: 'declined' }` on success.


### `actions/demo-dashboard/index.js`

Self-contained demo operator dashboard. Serves an HTML dashboard for listing pending cash orders and triggering accept/decline actions. This is a single web action that serves both the HTML UI and a JSON API.

**Security:**
* Optional `DEMO_UI_SECRET` check: if set, require `?secret=<value>` query param or `x-demo-secret` header on all requests. Return 401 if missing/wrong.
* Log a warning if `DEMO_UI_SECRET` is not set (dashboard is unprotected)

**Routing (based on HTTP method + path/body):**

The action receives all requests. Determine intent from:
* `params.__ow_method` (GET/POST) and `params.__ow_path` or action params
* `GET` with no action → serve the HTML dashboard
* `GET` with `action=list` param → return JSON list of pending orders
* `POST` with `action=accept` and `orderId` → call `payment-accept` logic (or inline the Commerce REST call)
* `POST` with `action=decline` and `orderId` → call `payment-decline` logic

**Fetching pending orders:**
* Call `GET orders?searchCriteria[pageSize]=50` from Commerce REST
* Filter to orders where `extension_attributes.split_cash_status === 'pending'` AND order is not in a terminal state (`complete`, `closed`, `canceled`, `cancelled`)
* Sort newest-first in memory
* Return up to 20 (configurable via `limit` param)

**HTML Dashboard:**
The dashboard is an HTML string returned with `Content-Type: text/html`. It should:
* List pending cash orders in a table: Order # (increment_id), entity_id, customer name, cash amount, store credit amount, date
* Provide **Accept** and **Decline** buttons for each order that call the action's own API endpoint
* Show success/error responses inline
* Include a refresh button
* Be styled enough to be usable (minimal CSS is fine; no external CDN dependencies to avoid CORS issues in Runtime)
* Show a warning banner if `DEMO_UI_SECRET` is not set

**Error surfacing in the UI:**
When a Commerce REST call fails, include the HTTP status and a short description of the Commerce error body (sanitize — strip HTML tags, truncate to 500 chars). Do not expose credentials.

**Response helpers:**

```javascript
function jsonResponse(statusCode, obj, extraHeaders = {}) { ... }
function htmlResponse(html) { ... }
```


### `.env.example`

```dotenv
# Commerce REST base URL — no trailing slash
COMMERCE_BASE_URL=

# OAuth 1.0a integration credentials (Admin → System → Integrations)
COMMERCE_CONSUMER_KEY=
COMMERCE_CONSUMER_SECRET=
COMMERCE_ACCESS_TOKEN=
COMMERCE_ACCESS_TOKEN_SECRET=

# PoC threshold — must match split_payment/general/threshold in Commerce (default: 100)
PAYMENT_THRESHOLD=100

LOG_LEVEL=info

# Demo dashboard optional shared secret
DEMO_UI_SECRET=
DEMO_UI_BASE_URL=
```


### Deploy Command

After generating all files, from the `split-payment-orchestrator/` directory:

```bash
npm install
cp .env.example .env
# Edit .env with your credentials
aio app deploy
```

After deployment, note the action URLs printed by `aio app deploy`. The `demo-dashboard` URL is where you access the operator dashboard.


### End of prompt


{{$include /help/_includes/split-payment-ai-tools-related-links.md}}
