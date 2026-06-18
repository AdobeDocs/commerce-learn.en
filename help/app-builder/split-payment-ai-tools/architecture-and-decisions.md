---
title: Split payment POC — architecture and design decisions
description: Learn how the split payment POC maps sync checkout to Commerce and I/O-driven steps to App Builder, with extension attributes, REST, and five plugin edge cases.
feature: App Builder, Eventing, Extensibility, Paas, Payments, REST
topic: App Builder, Commerce, Development, I/O Events, Integrations, Runtime
role: Developer, User
level: Intermediate
doc-type: Tutorial
duration: 293
jira: KT-20902
last-substantial-update: 2026-04-27
---
# Split payment POC: architecture and design decisions

This page explains the architectural choices behind the split payment proof of concept. Read it before you use the build prompts in this series, so you understand how each component is structured, and how to adapt the patterns in your own project.

## The core principle

The proof of concept is not about the most elegant split payment implementation. It is about showing **how to start moving Commerce logic to App Builder without a big-bang rewrite**.

The rule that is applied throughout is:

> **If something must run synchronously in the Commerce request cycle, or must invoke Commerce-internal APIs that have no clean external surface, it stays in PHP. Everything else moves to App Builder.**

## What lives in Commerce (PHP) and why

### 1. Store credit application: `PlaceOrderPlugin`

Store credit is applied to the cart using `Magento\CustomerBalance\Api\BalanceManagementInterface::apply()`. This method only works on an **active** cart. The cart becomes inactive the moment the order is placed. App Builder receives the I/O event *after* the order is placed, so applying store credit from App Builder is not possible.

**The lesson:** Anything that must change cart state before order placement must run in Commerce. There is no workaround.

### 2. Synchronous threshold guard: `CheckoutPlugin`

The $100 order threshold check must block the customer at the payment step, before they select **[!UICONTROL Place Order]**. The response must be synchronous in the Commerce request cycle. App Builder is event-driven and asynchronous, so it cannot return an immediate error in that moment.

App Builder *also* validates the threshold (as an audit), but the customer experience depends on the Commerce check running first.

### 3. Custom REST endpoints: `webapi.xml` and `SplitPaymentManagement`

The following endpoints must:

* Invoke `SplitInvoiceService` (invoices that use the Commerce internal invoice service)
* Invoke `ShipOrder::execute()` (Commerce's internal shipment service)
* Update order state and status with Commerce's order state machine

`/V1/split-payment/orders/:id/cash-received` and `/V1/split-payment/orders/:id/cash-decline`

There is no clean public REST layer for that behavior, so Commerce exposes the endpoints. App Builder calls them.

### 4. Split amounts on quote and order: observers and plugins

Commerce needs the split amounts (`split_store_credit_amount`, `split_cash_amount`, `split_cash_status`) on the order, both for the REST responses App Builder reads and for the **[!UICONTROL Admin]** order view. The amounts are attached with extension attributes and are copied from the quote to the order in an observer on `sales_model_service_quote_submit_before`.

## What lives in App Builder and why

### 1. Event-driven order processing: `payment-orchestrator`

After `sales_order_place_before` fires, App Builder receives the event. It re-validates the threshold (as an audit), records a *cash pending* comment on the order, and updates order status. None of that requires new PHP, only REST back into Commerce.

### 2. Cash acceptance: `payment-accept`

When an ERP (or an operator in the dashboard) confirms cash was received, `payment-accept` calls `POST /V1/split-payment/orders/:id/cash-received`. Invoice, shipment, and order status are handled in Commerce. App Builder is the trigger.

### 3. Cash decline: `payment-decline`

`payment-decline` calls `POST /V1/split-payment/orders/:id/cash-decline` and Commerce cancels the order. Same pattern as cash acceptance.

### 4. Operator dashboard: `demo-dashboard`

A self-contained HTML dashboard served from an App Builder web action. It fetches orders that are waiting on cash from Commerce REST and provides **[!UICONTROL Accept]** / **[!UICONTROL Decline]** actions that call the App Builder actions above. Commerce **[!UICONTROL Admin]** is not required.

## The threshold: enforced twice on purpose

```text
Customer at checkout
        |
        v
[Commerce: CheckoutPlugin]     <- Synchronous, blocks immediately, user sees error
        |
        |  (if somehow bypassed: direct API call, and so on)
        v
[Order placed] -> I/O Event -> [App Builder: payment-orchestrator]
                                        |
                                        v
                              [evaluateThreshold()]  <- Async audit, records failure comment
```

**Commerce owns the user-facing guard; App Builder owns the post-placement audit.** That is intentional.

## The store credit: why it stays in PHP

```text
What you might think would work (it does not):
  Order placed -> I/O Event -> App Builder -> PUT /V1/carts/:id/store-credit
  (Fails: cart is inactive after place order)

What actually works:
  AroundPlaceOrder plugin
  -> BalanceManagementInterface::apply($cartId, $amount)  <- cart is still active
  -> place order
  -> order placed
  -> I/O event: App Builder (store credit is already applied)
```

The `store-credit.js` file in the orchestrator documents this. It is a no-op stub with comments that explain why it is not used.

## Extension attributes: the glue

Split amounts move through the system on extension attributes:

```text
Checkout JavaScript (Knockout)
    |  POST /V1/split-payment/set
    v
SplitPaymentSession (PHP session)
    |  AroundPlaceOrder reads the session
    v
CartInterface extension attributes
    |  `sales_model_service_quote_submit_before` observer
    v
OrderInterface extension attributes -> `sales_order` flat columns
    |  I/O event payload includes these fields
    v
App Builder `payment-orchestrator` reads the split amounts
```

## Data model

**`sales_order` flat columns that this module adds**

| Column | Type | Purpose |
| --- | --- | --- |
| `split_store_credit_amount` | float | Store credit that was applied |
| `split_cash_amount` | float | Cash amount due |
| `split_cash_status` | varchar | `pending`, `received`, or `declined` |
| `split_sc_invoice_id` | int | Entity ID of the store credit invoice |
| `split_cash_invoice_id` | int | Entity ID of the cash invoice |

**Extension attributes** (on `CartInterface`, `OrderInterface`, and `OrderPaymentInterface`)

* `split_store_credit_amount` (float)
* `split_cash_amount` (float)
* `split_cash_status` (string)

## I/O event payload fields

`observer.sales_order_place_before` is configured in `io_events.xml` to include the following in the event:

```xml
entity_id, quote_id, increment_id, subtotal,
split_store_credit_amount, split_cash_amount, split_cash_status
```

App Builder uses `entity_id` as the order ID and `split_store_credit_amount` and `split_cash_amount` for threshold validation.

## The five edge cases the proof of concept covers

### 1. `CapCustomerBalanceCollectPlugin`

Commerce’s native **[!UICONTROL Customer balance]** total collector can over-apply (it can see the full available balance, not the session-declared split amount). This plugin caps the amount to the value declared in the session.

### 2. `FixSplitPaymentGrandTotalPlugin`

After store credit is applied, the quote **[!UICONTROL Grand Total]** can drop to the cash-only amount. The checkout JavaScript must compute the order total for split validation *before* that change. The plugin runs after totals collection and corrects the display, while the JavaScript does not trust `grand_total` alone and reconstructs the value from subtotal segments.

### 3. `FixInvoiceCustomerBalanceAfterTotalsPlugin`

When invoice totals are recollected, store credit can be applied twice. This plugin corrects `customer_balance_amount` on invoices.

### 4. `SplitPaymentZeroTotalPlugin`

After store credit is applied, the cart **[!UICONTROL Grand Total]** can be $0 (full store credit order). Commerce’s **[!UICONTROL Zero subtotal checkout]** check can block COD in that case. This plugin allows COD when the session cash amount is greater than 0.

### 5. Quote recollection before `BalanceManagementInterface::apply()`

`apply()` checks the amount against the current **[!UICONTROL Grand Total]**. If the total is already the cash portion only, `apply()` can fail or cap. `PlaceOrderPlugin` temporarily suspends the grand-total fix while balance is applied, using a session flag (`beginBalanceApply` / `endBalanceApply`).


{{$include /help/_includes/split-payment-ai-tools-related-links.md}}
