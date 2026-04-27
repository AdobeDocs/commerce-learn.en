---
title: "Split payment POC: prerequisites and environment setup"
description: Learn how to set up Commerce, Admin for COD and store credit, OAuth integration, I/O Events, App Builder, and aio CLI before the split payment build prompts.
feature: App Builder, Configuration, Eventing, Extensibility, Paas, Payments, REST
topic: App Builder, Commerce, Development, I/O Events, Integrations, Runtime
role: Developer, Leader, User
level: Intermediate
doc-type: Tutorial
duration: 295
jira: KT-20902
last-substantial-update: 2026-04-27
---
# Split payment POC: prerequisites and environment setup

Complete every step in this tutorial before you run any of the build prompts. Missing a single step is the most common reason the flow breaks mid-tutorial.

## 1. Adobe Commerce requirements

* Adobe Commerce **2.4.5 or later** (on-premises or Commerce Cloud)
* Git access to the Commerce project (you add a module under `app/code/`)
* Access to **[!UICONTROL Commerce Admin]**

### Commerce Cloud only: enable I/O eventing

Add the following to `.magento.env.yaml` and deploy before you add the module:

```yaml
stage:
  global:
    ENABLE_EVENTING: true
```

> **Warning:** This deploy must finish successfully before the I/O Event module dependency can resolve.


## 2. Commerce Admin configuration

Do these steps before anything else. The checkout JavaScript depends on exact string matches.

### 2a. Enable Cash on Delivery with the exact title

**[!UICONTROL Stores]** > **[!UICONTROL Configuration]** > **[!UICONTROL Sales]** > **[!UICONTROL Payment Methods]** > **[!UICONTROL Cash On Delivery Payment]**

* **[!UICONTROL Enabled]**: **Yes**
* **[!UICONTROL Title]**: **`Cash`** (this exact string is what the checkout JavaScript matches)

> **Note:** If your store uses a different cash-on-delivery (COD) implementation or title, adjust `payment-method-helper.js` in the Commerce module.

### 2b. Enable store credit

**[!UICONTROL Stores]** > **[!UICONTROL Configuration]** > **[!UICONTROL Customers]** > **[!UICONTROL Customer Configuration]** > **[!UICONTROL Store Credit Options]**

* **[!UICONTROL Enable Store Credit Functionality]**: **Yes**

### 2c. Add store credit to your test customer

**[!UICONTROL Customers]** > **[!UICONTROL All Customers]** > *[your test customer]* > **[!UICONTROL Store Credit]** > **[!UICONTROL Update Balance]**

Add at least **$50** in store credit. You will test with an order under $100 total.

### 2d. Create the Commerce integration

**[!UICONTROL System]** > **[!UICONTROL Integrations]** > **[!UICONTROL Add New Integration]**

* **[!UICONTROL Name]**: `Split Payment App Builder` (or any name you prefer)
* On the **[!UICONTROL API]** tab, grant at minimum:
  * `Magento_Sales::actions` (required for the `cash-received` endpoint)
  * `Magento_Sales::cancel` (required for the `cash-decline` endpoint)
  * Quote or cart management (full or a relevant subset)
  * **[!UICONTROL Customer balance]** (full or a relevant subset)

Select **[!UICONTROL Save]**, then **[!UICONTROL Activate]**.

**Copy all four values; they are only shown once:**

| Value | Environment variable |
| --- | --- |
| Consumer Key | `COMMERCE_CONSUMER_KEY` |
| Consumer Secret | `COMMERCE_CONSUMER_SECRET` |
| Access Token | `COMMERCE_ACCESS_TOKEN` |
| Access Token Secret | `COMMERCE_ACCESS_TOKEN_SECRET` |

Store these values securely. You need them in every App Builder `.env` file.


## 3. Adobe Developer Console and App Builder

* Access to an Adobe Developer Console organization
* An **App Builder project** (new or one you reuse)
* A workspace configured; the prompts assume **[!UICONTROL Stage]**
* **[!UICONTROL Adobe I/O Events]** added as a service to the workspace
* **Commerce** connected as an event provider for the workspace

The event code used in the proof of concept is: `com.adobe.commerce.observer.sales_order_place_before`

If you have not connected Commerce as an event provider, see [Configure Commerce to emit events to Adobe I/O](https://developer.adobe.com/commerce/extensibility/events/configure-commerce/){target="_blank"} in the Commerce Extensibility guide.


## 4. Local development environment

```bash
# Required versions
node --version    # 18.x or later
npm --version     # any recent version

# Adobe I/O CLI
npm install -g @adobe/aio-cli

# Authenticate
aio login

# Select your project and workspace
aio app use
# Confirm the org, project, and workspace shown are correct
```


## 5. Two project directories to know

This tutorial uses two separate directory roots. Keep them separate.

**Commerce project root** (your Magento git repository):

```text
<commerce-root>/
└── app/code/Client/SplitPayment/   ← Module goes here
```

**App Builder project root** (the `split-payment-orchestrator` folder from the source package, or a new project you create):

```text
split-payment-orchestrator/
├── app.config.yaml
├── package.json
├── .env                            ← Copy from .env.example, then fill in
└── actions/
```


## 6. entity_id compared to increment_id

> **Always use `entity_id` (the numeric database ID), not `increment_id` (for example `000000042`), in REST calls.**

Find `entity_id` from the **[!UICONTROL Commerce Admin]** order URL:

```text
/admin/sales/order/view/order_id/42/   →   entity_id = 42
```

Or from the simulation script:

```bash
node scripts/simulate-split-payment.mjs show 42
```


## 7. The $100 threshold

The split payment UI and threshold guard target orders **$100.00 or less**. The flow behaves as follows:

* **At or below $100:** the split payment UI appears; the customer can set a cash plus store credit split
* **Above $100:** `CheckoutPlugin` throws an error at the payment step

To test, build a cart whose subtotal, shipping, and tax are **less than or equal to $100** (for example, a product under $90 so shipping and tax still fit under the cap).

The threshold is stored in:

* Commerce config: `split_payment/general/threshold` (default `100` in `etc/config.xml`)
* App Builder environment: `PAYMENT_THRESHOLD=100` (must match Commerce)


## 8. Fastly (Commerce Cloud only)

App Builder actions call Commerce over REST (`/rest/V1/split-payment/orders/...`). If your Commerce Cloud project uses Fastly with IP allowlisting, the App Builder runtime egress IP addresses must be allowlisted.

**How to check:** Run the simulation script first (direct curl with OAuth signing). If that works but the App Builder action returns `403`, Fastly is likely blocking the request.

Use Adobe’s current documentation for App Builder egress IP ranges and add them to your Fastly configuration as needed.


## Verification checklist

Before you start the build prompts, confirm the following:

* [ ] Commerce version is 2.4.5 or later
* [ ] I/O eventing is enabled (Commerce Cloud) and deployed
* [ ] Cash on delivery is enabled with the title set exactly to `Cash`
* [ ] Store credit is enabled
* [ ] The test customer has at least $50 store credit
* [ ] The Commerce integration is created and activated, and all four OAuth values are saved
* [ ] The App Builder project has the I/O Events service and the Commerce event provider configured
* [ ] `aio login` is complete and the correct workspace is selected with `aio app use`
* [ ] Node.js 18 or later is installed and the `aio` CLI is installed
* [ ] `.env` files are prepared per [Split payment POC: environment variables reference](split-payment-poc-env-reference.md) (and your source package, if you use one)


{{$include /help/_includes/split-payment-ai-tools-related-links.md}}
