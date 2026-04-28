---
title: "Create a split payment POC: App Builder full demo"
description: Learn how split payment, REST, App Builder I/O, and operator accept/decline work in this Luma demo, plus a configurable pre-order total that can block the cart.
feature: App Builder, Paas, Payments
topic: App Builder, Commerce, Development, I/O Events, Integrations, Runtime
role: Developer, Leader, User
level: Intermediate
doc-type: Technical Video
duration: 933
jira: KT-20902
last-substantial-update: 2026-04-27
---
# Create a split payment POC: App Builder full demo

This is the end-to-end walkthrough of the split payment proof of concept built on Adobe Commerce and Adobe App Builder. The demo assumes you have already used AI tools and a prompt to produce the in-process Commerce extension and the App Builder app; this video shows what happens after that code is merged, deployed to an Adobe Commerce Cloud website using the native Luma theme, and the App Builder project is live.

A shopper pays with part cash and part **[!UICONTROL Store Credit]**. Commerce owns synchronous checkout and the APIs the storefront needs; App Builder handles orchestration, operator workflows, and I/O event consumers. The reference implementation uses a Commerce (PaaS) project and the Luma native checkout rather than an Edge Delivery Services storefront, which is still a common path for many merchants. If you use **Adobe Commerce as a Cloud service** in a different topology, the App Builder code stays similar but storefront and in-process work would look different. For on-premises, self-hosted, and Commerce in the cloud on Luma, this video shows a practical split between in-process code and App Builder for new functionality.

## Video

>[!VIDEO](https://video.tv.adobe.com/v/3484087?learn=on)

## Who is this video for?

* Technical architects planning Commerce extensibility
* Developers implementing checkout and integrations
* Implementation teams who need a realistic split between PHP and App Builder

## Set up the scenario on the storefront

The demo account has **[!UICONTROL Store Credit]** and you see that balance in checkout. Add products until the order total is about $80. That size gives you room to show both the successful accept path and a decline path, similar to a card decline, without the math fighting you.

**[!UICONTROL Split payment]** is only offered to signed-in customers, because the session must expose store credit. Guest checkout does not show the split option.

1. On the **[!UICONTROL Payment]** step, choose the cash method (the demo renames **[!UICONTROL Cash on delivery]** to **Just Cash**).
1. A split payment area appears under the payment method. The cash field is prefilled to the order total, and the component reads **[!UICONTROL Store Credit]** from the session.
1. For an ~$80 cart, set **$50** cash and **$30** store credit so the component shows $50 + $30 = $80.
1. When the amounts are valid, place the order.

The UI triggers a call to a new **[!UICONTROL Commerce]** REST API for the split. Checkout stays synchronous: Commerce applies store credit, stores split lines on the order, and emits an I/O event that App Builder consumes later. The success page is immediate for the customer.

## Review the order in the Commerce admin

In **[!UICONTROL Sales]** > **[!UICONTROL Orders]**, open the new order. The **[!UICONTROL Payment information]** area shows the split, for example **$50** cash and **$30** store credit. The status is **Pending** when cash is not yet collected; store credit is already taken when the order is created.

**[!UICONTROL Comments]** can include text that App Builder added. The **[!UICONTROL Payment orchestrator action]** in App Builder received the I/O event, checked the split amounts, and used authenticated REST to append comments. **[!UICONTROL Commerce]** treats that like any other REST call and does not need to know the writer.

## Use the App Builder operator dashboard (ERP or back office)

A simple HTML experience runs as an **[!UICONTROL App Builder]** web action (no **[!UICONTROL Admin]** for this view). The dashboard calls the **[!UICONTROL Commerce Order]** REST API and filters to **Pending** so you can find the $50 cash leg.

You typically integrate this pattern with an ERP or fraud tool. Two actions are demonstrated:

* **Accept** &mdash; Confirms that cash was received (in production, often an automated post from a cash drawer or store system).
* **Decline** &mdash; Simulates fraud or a failed collection step (in production, usually automated from your risk service).

**Accept and complete the order**

1. In the **[!UICONTROL App Builder]** app, use **Accept** to confirm cash.
1. The app calls a new **[!UICONTROL Commerce]** endpoint that finalizes the cash line. The core order flow (invoicing, and in this build an automated shipment) runs with native **[!UICONTROL Commerce]** behavior. None of that path requires a human in **[!UICONTROL Admin]**; orchestration and the endpoint live in App Builder.

Refresh the same order in **[!UICONTROL Admin]**: status moves to **Complete** when the cash is accepted, with invoice and, where the product is shippable, a shipment to shorten the full lifecycle in the demo.

**Decline and cancel**

1. Open a prebuilt order that is still in the decline scenario.
1. In the **[!UICONTROL App Builder]** app, use **Decline** to simulate a fraud or collection failure.
1. In **[!UICONTROL Admin]**, the order is **Cancelled**. The history shows a declined cash status, comments explain the result, the shopper was not charged the store-credit line as if it were a final sale, and the store-credit invoice is voided with the cancellation. A production system would also notify the customer and release any holds on inventory or service.

## Order total threshold (validation before the order is created)

App Builder or **[!UICONTROL Commerce]** configuration can support validation rules; this build blocks orders over **$100** in cart value (a demo cap you can change). A value check is not the most common business rule&mdash;inventory or availability checks are more typical&mdash;but it shows that validation can run at **[!UICONTROL Payment]** in **[!UICONTROL Commerce]** before an order is created, while App Builder still handles follow-up automation.

1. Add products until the total is above **$100**.
1. The split **[!UICONTROL UI]** still appears; the over-limit result only surfaces on **Place order**.
1. The shopper sees a generic error such as **Payment could not be processed. Please try again or contact support.**
1. The **[!UICONTROL cart]** is unchanged so the customer can lower the total, pick another method, or contact support.

A risk score, region rule, or similar could plug in here; **[!UICONTROL Commerce]** blocks the order, and **[!UICONTROL App Builder]** can own notifications and case work after the fact.

## Commerce on premises, Commerce in the cloud, and **Adobe Commerce as a Cloud service**

The walkthrough matches **[!UICONTROL Adobe Commerce]** on an infrastructure you manage or **[!UICONTROL Commerce in the cloud]** (PaaS) with a traditional storefront. For **[!UICONTROL Adobe Commerce as a Cloud service]** (SaaS) with a different front end and no in-process module in this shape, the App Builder pieces are largely the same, while storefront and extension work would be different. In all cases, the same principle holds: let **[!UICONTROL Commerce]** do what must happen inside the **[!UICONTROL Commerce]** request, and use **[!UICONTROL App Builder]** for the rest of the experience.

{{$include /help/_includes/split-payment-ai-tools-related-links.md}}
