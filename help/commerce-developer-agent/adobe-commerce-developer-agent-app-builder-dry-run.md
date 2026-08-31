---
title: Adobe Commerce Developer Agent App Builder dry run
description: Learn how to build, deploy, and test three Commerce extensibility use cases with the Adobe Commerce Developer Agent in this hands-on App Builder dry run.
feature: Extensibility, App Builder, Eventing, Configuration
topic: App Builder, Development, Integrations
role: Developer
level: Intermediate
doc-type: Tutorial
duration: 438
last-substantial-update: 2026-08-28
---
# Adobe Commerce Developer Agent App Builder dry run

A hands-on walkthrough for building, deploying, and testing Commerce extensibility use cases with the Adobe Commerce Developer Agent (CDA). This dry run covers three use cases: a cart quantity limit webhook, a high-value order hold, and event-driven archival for held orders, from blueprint through functional testing.

## Getting started

### How to report issues and feedback

Throughout the dry run, you encounter rough edges — that's expected while working with a new feature. Capture and share any issues with your Adobe program contact using the feedback template provided during onboarding.

>[!TIP]
>
> When reporting an issue:
>
> * Include the `projectId` (visible in your browser URL).
> * Include screenshots whenever relevant.

### Prerequisites

**Accounts and access**

* At least the **Developer** role in your Early Access IMS Organization.
* Admin access to an Adobe Commerce as a Cloud Service (ACCS) instance within that organization, available at experience.adobe.com under **Cloud Service Instances**.
* A GitHub account.

**Tools**

An Edge Delivery Services (EDS) storefront is required for functional validation. You'll need:

* Node.js 22+
* Adobe I/O CLI: `npm install -g @adobe/aio-cli`
* AIO CLI Commerce plugin: `aio plugins:install https://github.com/adobe-commerce/aio-cli-plugin-commerce`

Install the storefront boilerplate in an empty folder, selecting your ACCS instance when prompted:

```bash
aio commerce extensibility app-setup -s aem-boilerplate-commerce -n storefront
```

Start the storefront:

```bash
cd storefront
npm run start
```

## Opening the Commerce Developer Agent

1. Navigate to the Commerce Developer Agent at experience.adobe.com, under **Developer Agent**.
1. Sign in using your Early Access IMS Organization credentials.

## Use case 1: cart maximum units webhook

This use case validates cart quantity limits before a product is added, using a synchronous Commerce webhook.

### Blueprint stage

Enter the following prompt and click **Generate Blueprint**:

```text
Add a validation webhook that runs before a product is added to the cart.

Use the Commerce webhook method observer.sales_quote_item_save_before (type before) — do not use
observer.checkout_cart_product_add_before, observer.sales_quote_add_item, or any other event.

Calculate the total by summing all quote line quantities and the quantity of the current item.
If the same SKU already exists in the quote, exclude its existing quantity to avoid double-counting.

If the total is greater than the maximum allowed, block the add and show:
"You have reached the maximum amount of items."

The maximum allowed must be configurable in Commerce Admin as max_cart_units, with default 10.

Map payload fields using name and source properties:
- name: item.qty, source: data.item.qty
- name: item.sku, source: data.item.sku
- name: quote, source: context_checkout_session.get_quote[items.qty,items.sku]

Set required: true and fallback_error_message: "You have reached the maximum amount of items."
on the webhook config.

When blocking the add, do not use exceptionOperation, because it serializes exceptionClass as class.
Instead, manually return an exception operation response whose body includes type:
{
  "op": "exception",
  "message": "You have reached the maximum amount of items.",
  "type": "\\Magento\\Framework\\GraphQl\\Exception\\GraphQlInputException"
}
```

>[!NOTE]
>
> Look for these things:
>
> * A blueprint (v1) capturing the requirements is created.
> * Tasks to guide the implementation are created.

Refine the blueprint by entering details in the chat box or by clicking one of the pills above the chat box (*Challenge assumptions*, *Find design gaps*, etc.). Once you're satisfied, click **Approve plan** to move forward.

### Develop stage

The agent transitions to the Develop stage and begins provisioning the workspace.

>[!NOTE]
>
> Look for these files in the Explorer panel:
>
> * `app.commerce.config.ts`
> * `app.config.yaml`
> * `install.yaml`
> * `package-lock.json`
> * `package.json`

Once provisioned, the agent shows a list of implementation tasks and starts building.

>[!NOTE]
>
> Look for these things:
>
> * The code generated matches the requirements.
> * The `Validate` streaming screen shows progress on workspace validation (`aio app build`).
> * The agent self-corrects the generated code if validation fails.

Once satisfied with the code, click the **Integrations** tab to move forward.

### Configure integrations

**Connect or create an App Builder workspace**

To create or connect an App Builder project, follow the on-screen instructions.

If connecting to an existing workspace, make sure it has:

* The `Runtime` service added.
* The following APIs added: Adobe Commerce as a Cloud Service, I/O Management API, App Builder Data Services, I/O Events, Adobe I/O Events for Adobe Commerce.

If creating a new workspace, manually add the **Adobe Commerce as a Cloud Service** API.

>[!IMPORTANT]
>
> Once connected to an existing App Builder project, expand **Advanced Configuration** and paste the workspace JSON, then click **Re-check status** to confirm all required APIs are installed.

Click **Next** to continue.

**Connect to Commerce**

Select your ACCS instance from the list, or enter the URL in the **Commerce REST Base URL** field, then click **Connect Commerce instance**. Click **Next** to continue.

**Connect to GitHub**

Connect the workspace to a GitHub repository by entering the repository URL and either using the GitHub App or a personal access token. Click **Next** to continue.

**Configure environment variables**

Fill in any environment variables required by the project.

### Deploy

Click **Develop** to return to the develop stage, then ask the agent to deploy in the prompt field.

>[!NOTE]
>
> Look for a "Confirm deployment" message showing the Organization, Project, Workspace, and Runtime namespace.

Confirm the deployment.

>[!NOTE]
>
> Look for:
>
> * The `Validate` streaming screen showing pre-deploy validation progress.
> * The agent self-correcting the code if validation fails.
> * The `Deploy` streaming screen showing deployment progress (`aio app deploy`).
> * The agent self-correcting the code if deployment fails.

### Associate the app in App Management

1. Navigate to your ACCS instance Admin URL and sign in.
1. Select **Apps** on the left-hand menu, then **App Management**.
1. Click **+ Associate App** (upper right).
1. Select the Project and Workspace that CDA deployed to, then click **Associate**.

>[!NOTE]
>
> Look for a card showing the application name and version, and the capabilities implemented (Business Configuration, Webhooks, Events, etc.).

### Install and configure in App Management

1. On the row for your application, click **Install**, then **Close**.
1. On the same row, click **Configure** to fill in business configuration values, then **Close**.

>[!NOTE]
>
> Look for a form showing every configuration field specified by the blueprint, pre-filled with the defaults you specified.

### Functional testing

1. In the App Management app configuration, set **Maximum cart units** to 3 (a low value for a quick test).
1. On the storefront, start with an empty cart.
1. Add products from the Product Detail Page (PDP) until the total quantity exceeds 3 — the last add fails.
1. On PDP, you see: *"You have reached the maximum amount of items."*
1. Below the limit, adds still succeed.

>[!NOTE]
>
> From the Product Listing Page (PLP), a blocked add fails silently with no message — this is storefront behavior, not a webhook failure. Prefer the PDP for verification.

## Use case 2: high-value order hold and verification code

Navigate back to the **Blueprint** stage to begin this use case.

### Blueprint stage

Enter the following prompt and click **Generate Blueprint**:

```text
Add a Commerce event priority subscription to `plugin.sales.api.order_management.place`.

Extract `entity_id` and `grand_total` from the Commerce event payload using event `fields` in `app.commerce.config.ts`.

Important: the runtime action receives a CloudEvents-shaped payload. For Commerce eventing extracted fields,
parse them from `params.data.value`, not directly from `params.data`. The handler must use:
- `params.data.value.entity_id`
- `params.data.value.grand_total`

When `grand_total` is greater than `order_hold_threshold`:
1. Generate a verification code locally.
2. Put the order on hold with state and status `holded`.
When putting the order on hold, save the verification code using `custom_attributes`, not `extension_attributes`.
The Commerce `POST V1/orders` payload should include:
{
  "entity": {
    "entity_id": <entity_id>,
    "state": "holded",
    "status": "holded",
    "custom_attributes": [
      {
        "attribute_code": "<hold_verification_attribute>",
        "value": "<verification_code>"
      }
    ]
  }
}
3. Save the verification code via a `POST V1/orders` Commerce REST API call.

Make these configurable in Commerce Admin:
- `order_hold_threshold`, default `500`
- `hold_verification_attribute`, default `lab_verification_code`

Validate inputs before use:
- `entity_id` must be a positive integer.
- `grand_total` must be a non-negative number.
```

>[!NOTE]
>
> Look for these things:
>
> * A blueprint (v2) capturing the requirements is created.
> * Original plan tasks are retained.
> * New tasks corresponding to the new requirements have been added.

Refine the blueprint as needed, then click **Approve plan** to move forward.

### Develop, deploy, associate, and install

Follow the same process used in Use case 1 to move from requirements to an installed application — there's no need to reconfigure integrations.

>[!IMPORTANT]
>
> To pick up changes to an already-associated app, you need to **Unassociate** and **Associate** it again in App Management.

### Functional testing

1. In App Management app configuration, set **Order hold threshold (USD)** to 50 (easy to exceed in a test cart).
1. Confirm the order custom attribute exists (default `lab_verification_code`).
1. Place an order with a grand total over $50.
1. Wait ~30 seconds (events are asynchronous; non-priority delivery can take up to ~59s).
1. In Commerce Admin → Sales → Orders, open the order. Status is **On Hold** (`holded`); custom attributes include `lab_verification_code` with a random value.
1. Optional: place an order under $50 first — this handler does not put it on hold.

## Use case 3: event-driven archival for held orders

Navigate back to the **Blueprint** stage to begin this use case.

### Blueprint stage

Enter the following prompt and click **Generate Blueprint**:

```text
When an order is saved with state holded, archive it to external storage and
record a reference that can be looked up later by order ID.

Add an event priority subscription on observer.sales_order_save_after, filtered to fire only when
state equals holded. From the event payload, extract:
- `entity_id`
- `payment.amount_ordered`
- `custom_attributes` (to read the `lab_verification_code` attribute set in Step 3)

The event handler must:
1. Persist the order details to the `held_orders` App Builder DB collection:
{
  "order_id": <entity_id>,
  "grand_total": <payment.amount_ordered>,
  "verification_code": <lab_verification_code>,
  "archived_at": <ISO timestamp>
}
2. Ensure the record can be looked up later by order ID.

The `held_orders` collection must exist before the handler runs:
- Provision persistent App Builder Database Storage in region `amer`.
- Create the collection during app installation.
- Create a unique index on `order_id` during installation.
- Drop the whole `held_orders` collection when the app is uninstalled.

Register the event handler separately from the existing cart validation webhook and high-value order hold action:
- runtime action: `order-archive/archive-held-order`
- non-web action
- `include-ims-credentials: true` on the archive action and the installation action

Follow the `commerce-app-storage` skill for DB auth, installation steps, and ext.config wiring.
Do not use custom IMS credential normalization or `Core.AuthClient.generateAccessToken`.
```

>[!NOTE]
>
> Look for these things:
>
> * A blueprint (v3) capturing the requirements is created.
> * Original plan tasks are retained.
> * New tasks corresponding to the new requirements have been added.

Refine the blueprint as needed, then click **Approve plan** to move forward.

### Develop, deploy, associate, and install

Follow the same process used in the previous use cases to move from requirements to an installed application — there's no need to reconfigure integrations.

>[!IMPORTANT]
>
> To pick up changes to an already-associated app, you need to **Unassociate** and **Associate** it again in App Management.

### Functional testing

1. Ensure the Use case 2 threshold is low enough for testing (for example, $50 in app configuration).
1. Place an order over that threshold so Use case 2 puts it on hold (~30 seconds).
1. In Adobe Developer Console → Your Project → Stage → Events, open the registration for the held-order archival event (added or updated at install).
1. Confirm an event was delivered to that registration after the order moved to hold. Use the event trace or monitoring for the Commerce event linked to `order-archive/archive-held-order`.

>[!NOTE]
>
> Events are asynchronous — allow up to ~30–59 seconds after the order is put on hold.

## Troubleshooting

If the application generated by CDA isn't behaving as expected or is producing errors, ask the agent to troubleshoot from the Develop stage.

>[!NOTE]
>
> CDA has no visibility into steps that happen outside it. Associate, Install, Configure, and Functional testing all run in Commerce Admin, App Management, or the storefront — not in CDA. If an issue shows up in one of those areas, the agent can't see it happen, so give it what it's missing:
>
> * What you did, and where (for example, "clicked Install in App Management").
> * What you expected to happen.
> * What happened.
> * The exact error text or message shown on screen.
> * Any relevant errors from the browser console, or from the Adobe Developer Console's App Builder Logs and Event Registration Debug Traces.

The more concrete the report, the better the agent can diagnose the issue.

## Optional steps

**Download the code**

To continue refining or editing in your favorite IDE, download the code generated by CDA by clicking the download icon on the Develop stage Explorer toolbar. Select a destination folder and click **Save**, then unzip the workspace package.

>[!NOTE]
>
> Look for:
>
> * All files displayed in the Develop stage Explorer are present in the unzipped folder.
> * No "compilation" errors when building the project with `aio app build`.

To use the same agent skills CDA uses, install them in your project folder:

```bash
npx skills add adobe/aio-commerce-sdk --skill commerce-app-init -y && \
npx skills add adobe/aio-commerce-sdk --skill commerce-app-eventing -y && \
npx skills add adobe/aio-commerce-sdk --skill commerce-app-webhooks -y && \
npx skills add adobe/aio-commerce-sdk --skill commerce-app-business-config -y && \
npx skills add adobe/aio-commerce-sdk --skill commerce-app-storage -y && \
npx skills add adobe/skills --skill appbuilder-project-init -y
```

Then start your IDE or CLI and begin prompting.

**Attach context via file or link**

Instead of prompting directly in the Blueprint or Develop stages, you can attach context using a text file or a link:

1. Click the attachment icon on the chat box.
1. Click **Add File** to upload a local text file, or enter a URL and click **Add Link** to add context via a remote file.
1. Click **Done** and enter a prompt to nudge the agent.

>[!NOTE]
>
> Look for the agent incorporating the context from your attachments into its next turn.

## Known issues and workarounds

**The Blueprint stage does not generate tasks**

To get unblocked and continue, nudge the agent to generate tasks.

**The buttons to push to and pull from GitHub are not functional**

Instead, download the project ZIP file from the Develop stage.

{{$include /help/_includes/commerce-developer-agent-related-links.md}}

## Additional resources

* [Commerce Developer Agent overview](https://developer.adobe.com/commerce/extensibility/developer-agent/)
* [Getting started with the Commerce Developer Agent](https://developer.adobe.com/commerce/extensibility/developer-agent/getting-started)
* [Prompting tips for the Commerce Developer Agent](https://developer.adobe.com/commerce/extensibility/developer-agent/prompting)
* [Commerce Developer Agent support and feedback](https://developer.adobe.com/commerce/extensibility/developer-agent/support)
