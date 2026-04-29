---
title: "Split payment POC: Commerce module AI prompt"
description: "Learn how to use this prompt to generate Client_SplitPayment. REST, plugins, checkout JavaScript, I/O events, and enable, compile, and deploy commands."
feature: App Builder, Backend Development, Eventing, Extensibility, Paas, REST, Orders
topic: App Builder, Commerce, Development, I/O Events, Integrations, Runtime
role: Developer, Leader, User
level: Intermediate
doc-type: Tutorial
duration: 503
jira: KT-20902
last-substantial-update: 2026-04-27
---
# Split payment POC: Commerce module AI prompt

Use this page to copy the full prompt that generates the `Client_SplitPayment` in-process module: REST, session handling, **[!UICONTROL Checkout]**, and **[!UICONTROL Admin]** display for the split payment proof of concept. Operator workflow stays in App Builder.

## How to use this prompt

Copy everything from **PROMPT START** to **End of prompt** into Cursor (with Claude) or directly into Claude. Run it from the root of your Commerce project or a directory where the AI can create files.

## Customize before you run

* Replace `Client` with your real vendor name.
* Change `SplitPayment` if you want a different module name.
* If the site uses a custom theme, layout XML and RequireJS paths may need changes.
* If your **[!UICONTROL Cash on delivery]** method uses a different code than `cashondelivery`, update `payment-method-helper.js`.


## The prompt

**PROMPT START**

You are generating a complete, production-ready Adobe Commerce 2.4.5+ in-process module for a split payment feature. This module is the thin PHP adapter that exposes the right REST surface and attaches the right data at the right moments in the Commerce lifecycle. All operator workflow logic lives in Adobe App Builder (not in this module).

**Module identity:**
* Vendor: `Client`
* Module: `SplitPayment`
* Full name: `Client_SplitPayment`
* Namespace: `Client\SplitPayment`
* Location: `app/code/Client/SplitPayment/`
* Dependencies: `Magento_Checkout`, `Magento_CustomerBalance`, `Magento_Sales`, `Magento_Quote`, `Magento_WebApi`, `Magento_AdobeCommerceEventsClient`

Generate every file listed in the file structure below. Do not omit any file. Use `declare(strict_types=1)` in all PHP files.


### File Structure to Generate

```
app/code/Client/SplitPayment/
├── registration.php
├── composer.json
├── Api/
│   ├── Data/SplitPaymentInterface.php
│   └── SplitPaymentManagementInterface.php
├── Block/
│   └── Order/SplitPaymentInfo.php
├── Controller/
│   └── Checkout/StoreCreditBalance.php
├── etc/
│   ├── acl.xml
│   ├── config.xml
│   ├── db_schema.xml
│   ├── db_schema_whitelist.json
│   ├── di.xml
│   ├── events.xml
│   ├── extension_attributes.xml
│   ├── io_events.xml
│   ├── module.xml
│   ├── webapi.xml
│   └── frontend/
│       └── routes.xml
├── Model/
│   ├── SplitPaymentData.php
│   ├── SplitPaymentManagement.php
│   ├── Service/
│   │   └── SplitInvoiceService.php
│   └── Session/
│       └── SplitPaymentSession.php
├── Observer/
│   ├── AutoInvoiceStoreCreditOnOrderPlace.php
│   └── CopySplitPaymentToOrder.php
├── Plugin/
│   ├── CheckoutPlugin.php
│   ├── OrderRepositoryPlugin.php
│   ├── PlaceOrderPlugin.php
│   ├── Adminhtml/
│   │   └── OrderPaymentPlugin.php
│   ├── Checkout/
│   │   └── LayoutProcessorPlugin.php
│   ├── CustomerBalance/
│   │   └── CapCustomerBalanceCollectPlugin.php
│   ├── Payment/
│   │   ├── Block/
│   │   │   └── AdminSplitPaymentTitlePlugin.php
│   │   └── Checks/
│   │       └── SplitPaymentZeroTotalPlugin.php
│   ├── Quote/
│   │   └── FixSplitPaymentGrandTotalPlugin.php
│   └── Sales/
│       └── FixInvoiceCustomerBalanceAfterTotalsPlugin.php
├── Setup/
│   └── Patch/
│       └── Data/
│           └── AddSplitPaymentOrderAttribute.php
└── view/
    └── frontend/
        ├── requirejs-config.js
        ├── layout/
        │   └── sales_order_view.xml
        ├── templates/
        │   └── order/
        │       └── split-payment-info.phtml
        └── web/
            ├── js/
            │   ├── model/
            │   │   └── payment-method-helper.js
            │   └── view/
            │       └── payment/
            │           ├── cashondelivery-method.js
            │           └── split-payment.js
            └── template/
                └── payment/
                    ├── cashondelivery.html
                    └── split-payment.html
```


### Behavioral Specifications

#### 1. Database Schema (`etc/db_schema.xml`)

Add these columns to `sales_order` (resource: `sales`):

| Column | Type | Nullable | Comment |
|---|---|---|---|
| `split_store_credit_amount` | decimal(12,4) | yes | Store credit portion |
| `split_cash_amount` | decimal(12,4) | yes | Cash portion due |
| `split_cash_status` | varchar(32) | yes | `pending` / `received` / `declined` |
| `split_sc_invoice_id` | int unsigned | yes | Store credit invoice entity ID |
| `split_cash_invoice_id` | int unsigned | yes | Cash invoice entity ID |

Also generate the `db_schema_whitelist.json` for these columns.

#### 2. Extension Attributes (`etc/extension_attributes.xml`)

Add `split_store_credit_amount` (float), `split_cash_amount` (float), `split_cash_status` (string) to:
* `Magento\Quote\Api\Data\CartInterface`
* `Magento\Sales\Api\Data\OrderInterface`
* `Magento\Sales\Api\Data\OrderPaymentInterface`

#### 3. REST Endpoints (`etc/webapi.xml`)

```xml
POST /V1/split-payment/set              → anonymous (session-scoped)
POST /V1/split-payment/orders/:orderId/cash-received  → Magento_Sales::actions
POST /V1/split-payment/orders/:orderId/cash-decline   → Magento_Sales::cancel
```

All three map to `Client\SplitPayment\Api\SplitPaymentManagementInterface`.

#### 4. I/O Events (`etc/io_events.xml`)

Subscribe to `observer.sales_order_place_before` and include fields:
`entity_id`, `quote_id`, `increment_id`, `subtotal`, `split_store_credit_amount`, `split_cash_amount`, `split_cash_status`

#### 5. `SplitPaymentSession` — Session Wrapper

Stores declared split amounts in the checkout session. Must expose:
* `setAmounts(float $storeCredit, float $cash): void`
* `getAmounts(): array` — returns `['store_credit' => float, 'cash' => float]`
* `clear(): void`
* `beginBalanceApply(): void` — sets a flag suppressing the grand total fix plugin during store credit application
* `endBalanceApply(): void`
* `isBalanceApplyInProgress(): bool`

#### 6. `SplitPaymentManagement` — REST Controller

**`setSplitPayment(float $storeCreditAmount, float $cashAmount, ?string $cartId = null): bool`**
* Validates the cart belongs to the current session (by comparing numeric and masked quote IDs)
* Stores amounts in `SplitPaymentSession`
* Returns `true` on success; throws `LocalizedException` with generic message on failure

**`markCashReceived(int $orderId): bool`**
* Loads order by `entity_id`
* Validates `split_cash_status === 'pending'`
* Sets status to `received`, state to `processing`
* Adds a history comment: `"Cash payment of $X.XX received."`
* Calls `SplitInvoiceService::createCashPortionInvoice($orderId)`
* Adds a comment with the cash invoice increment ID
* Calls `createShipmentIfPossible($orderId)` — creates a shipment using `ShipOrder::execute()` if there are shippable items
* Returns `true`; throws generic `LocalizedException` on any error

**`markCashDeclined(int $orderId): bool`**
* Loads order
* Validates `split_cash_status === 'pending'`
* Validates `$order->canCancel()`
* Sets status to `declined`, adds comment: `"Cash payment declined (simulated fraud check)."`
* Saves order
* Calls `OrderManagement::cancel($orderId)`
* Returns `true`; throws generic `LocalizedException` on failure

#### 7. `PlaceOrderPlugin` — aroundPlaceOrder on `QuoteManagement`

This is the most critical plugin. Runs `aroundPlaceOrder`:

1. Load the quote; if not active, call `$proceed()` immediately
2. Read `SplitPaymentSession::getAmounts()`
3. If `customer_balance_amount_used > 0` on the quote, call `BalanceManagementInterface::remove($cartId)` (handle `LocalizedException` — log and rethrow as generic message)
4. Call `recollectQuoteForBalanceOperation()` — loads quote, calls `collectTotals()`, saves (within `beginBalanceApply()` / `endBalanceApply()` to suppress the grand total fix plugin)
5. If `$storeCredit > 0`, call `BalanceManagementInterface::apply($cartId, $storeCredit)` (handle failure)
6. Reload quote; set extension attributes: `split_store_credit_amount`, `split_cash_amount`, `split_cash_status = 'pending'`
7. Save `payment->additional_information['client_split_payment']` as `['store_credit' => x, 'cash' => y]`
8. Save quote
9. Call `$proceed()`, capture order ID
10. Call `SplitPaymentSession::clear()`
11. Return order ID

#### 8. `CopySplitPaymentToOrder` — Observer on `sales_model_service_quote_submit_before`

Reads split amounts from session → payment additional_information → quote extension attributes (in that priority order). Writes `split_store_credit_amount`, `split_cash_amount`, `split_cash_status = 'pending'` to the order object.

#### 9. `AutoInvoiceStoreCreditOnOrderPlace` — Observer on `sales_order_place_after`

After order placement, if the order has a store credit amount (`split_store_credit_amount > 0`), call `SplitInvoiceService::createStoreCreditPortionInvoice($orderId)` to immediately invoice the store credit portion.

#### 10. `SplitInvoiceService`

**`createStoreCreditPortionInvoice(int $orderId): ?int`**
Creates an invoice for the store credit portion only. Sets `customer_balance_amount` on the invoice to the store credit amount. Registers and saves the invoice. Returns the invoice entity ID or null on failure (log; do not rethrow).

**`createCashPortionInvoice(int $orderId): ?int`**
Creates an invoice for the cash portion (the remaining order items/amounts not covered by the SC invoice). Registers and saves. Returns entity ID or null on failure.

#### 11. `CheckoutPlugin` — on `PaymentInformationManagement`

Plugin on `Magento\Checkout\Model\PaymentInformationManagement::savePaymentInformationAndPlaceOrder`. Before proceeding:
* Load the quote from the checkout session
* Get the configured threshold: `Magento\Framework\App\Config\ScopeConfigInterface::getValue('split_payment/general/threshold')`, default `100`
* If `$quote->getGrandTotal() > $threshold`, throw `LocalizedException('Payment could not be processed. Please try again or contact support.')`

#### 12. `CapCustomerBalanceCollectPlugin` — on `Customerbalance` total

After the native customer balance total collect runs, cap `customer_balance_amount_used` to `SplitPaymentSession::getAmounts()['store_credit']`. This prevents Commerce from over-applying the full customer balance when the customer has declared a smaller store credit portion.

#### 13. `FixSplitPaymentGrandTotalPlugin` — on `Quote\Address\Total\Grand`

After grand total collect: if a split payment session exists and `isBalanceApplyInProgress()` is false, set the quote grand total to the session cash amount. This makes the checkout UI show only what is due in cash.

#### 14. `FixInvoiceCustomerBalanceAfterTotalsPlugin` — on `Sales\Model\Order\Invoice`

After invoice totals are collected, if the invoice's associated order has a `split_sc_invoice_id`, correct the `customer_balance_amount` on the invoice to prevent double-application of store credit.

#### 15. `SplitPaymentZeroTotalPlugin` — on `Payment\Model\Checks\ZeroTotal`

Allow COD payment when `SplitPaymentSession::getAmounts()['cash'] > 0`, even if the quote grand total is $0 (because store credit covers the entire order).

#### 16. `LayoutProcessorPlugin` — on `Checkout\Block\Checkout\LayoutProcessor`

After the layout is processed:
* Inject the `Client_SplitPayment/js/view/payment/split-payment` component into the `additional` children of the `cashondelivery` payment method component at `components.checkout.children.steps.children.billing-step.children.payment.children.renders.children.offline-payments.children.cashondelivery.children.additional`
* Remove the native store credit UI component (`customerBalance`, `useStoreCredit`) from the payment step — the split payment component owns store credit display/application

#### 17. `OrderRepositoryPlugin` — on `OrderRepositoryInterface`

After `get()` and `getList()`, hydrate the order's extension attributes from the flat `sales_order` columns (`split_store_credit_amount`, `split_cash_amount`, `split_cash_status`).

#### 18. `AdminSplitPaymentTitlePlugin` — on `Payment\Block\Info`

After `getTitle()` returns, if the payment method is `cashondelivery` and the order has a split payment, append `" (Split: Cash $X.XX + Store Credit $Y.YY)"` to the title.

#### 19. `OrderPaymentPlugin` — on `Sales\Block\Adminhtml\Order\Payment`

In `_beforeToHtml` or via afterToHtml, append split payment detail (cash amount, store credit amount, status) to the payment block HTML in the Commerce Admin order view.

#### 20. Storefront Store Credit Balance Controller

`Controller/Checkout/StoreCreditBalance.php` — route: `GET /splitpayment/checkout/storecreditbalance`

Returns JSON: `{"balance": float, "logged_in": bool}`. If customer is not logged in, returns `{"balance": 0, "logged_in": false}`. Reads balance from `Magento\CustomerBalance\Model\Balance`.

Register the frontend route in `etc/frontend/routes.xml` with `frontName="splitpayment"`.

#### 21. Checkout KnockoutJS Component — `split-payment.js`

A `uiComponent` that:
* Detects when the `cashondelivery` payment method is selected (`quote.paymentMethod.subscribe`)
* Loads the customer's store credit balance via `GET /splitpayment/checkout/storecreditbalance`
* Pre-fills the cash amount field with the full order total (calculated from `total_segments` excluding `grand_total` and `customerbalance` — never uses `grand_total` directly since it may be set to the cash remainder)
* As the customer changes the cash amount input: computes store credit needed = order total − cash; validates; posts to `POST /V1/split-payment/set`
* Shows validation messages for: cash > order total, insufficient store credit, not logged in
* Shows a success message when a valid split is entered: `"The remaining $X.XX will automatically be applied from your store credit."`
* Resets when another payment method is selected (posts `{storeCreditAmount: 0, cashAmount: 0}` to clear session)

#### 22. `cashondelivery-method.js`

Extends `Magento_OfflinePayments/js/view/payment/offline-payments`. Uses `payment-method-helper.js` to detect the cash method code. Registers `split-payment` component in its `additional` region.

#### 23. `payment-method-helper.js`

Utility returning `getCashMethodCode()` — checks `window.checkoutConfig.paymentMethods` for `cashondelivery`; falls back to `checkmo` if needed.

#### 24. `cashondelivery.html` Template

Standard COD template but includes `<!-- ko foreach: getRegion('additional') -->` region so the split payment child component can render.

#### 25. `split-payment.html` Template

KnockoutJS template for the split payment fields:
* Available store credit balance display
* Cash amount input (number, step 0.01)
* Store credit portion display (read-only)
* Auto-apply store credit message (shown when split is valid and store credit > 0)
* Validation error message

#### 26. `requirejs-config.js`

Maps:
* `Client_SplitPayment/js/view/payment/split-payment` → the component
* `Client_SplitPayment/js/view/payment/cashondelivery-method` → the COD override
* `Client_SplitPayment/js/model/payment-method-helper` → the helper

#### 27. `etc/config.xml`

Default system config values:

```xml
<split_payment>
  <general>
    <threshold>100</threshold>
    <enabled>1</enabled>
  </general>
</split_payment>
```


### Critical Implementation Notes

**Store credit application must use `BalanceManagementInterface`, not direct model manipulation.** `BalanceManagementInterface::apply()` handles the session, validation, and cart recalculation atomically.

**`PlaceOrderPlugin` must use `aroundPlaceOrder` (not `beforePlaceOrder`).** The store credit must be applied while the cart is still active, and that must be guaranteed before `$proceed()` is called.

**The session flag pattern for `beginBalanceApply` / `endBalanceApply` is critical.** Without it, `FixSplitPaymentGrandTotalPlugin` runs during `collectTotals()` inside the balance operation and sets grand total to the cash remainder, causing `BalanceManagementInterface::apply()` to fail or cap the credit.

**Never expose internal error details to the customer.** All `catch` blocks that surface to REST responses must throw `LocalizedException('Payment could not be processed. Please try again or contact support.')`.

**`entity_id` is the numeric database ID.** REST calls from App Builder always use `entity_id`, not `increment_id`.

**`SplitInvoiceService` should catch and log errors rather than propagate them.** Invoice creation failure should not cancel an already-placed order — log the failure and let the Admin handle it manually.


### After Generating Files

Run these commands in the Commerce project root:

```bash
bin/magento module:enable Client_SplitPayment
bin/magento setup:upgrade
bin/magento setup:di:compile
bin/magento setup:static-content:deploy -f
bin/magento cache:flush
```

### End of prompt


{{$include /help/_includes/split-payment-ai-tools-related-links.md}}
