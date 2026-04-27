---
title: "Split payment POC: next steps after the proof of concept"
description: Learn how to move the split payment POC toward production: Experience Cloud UI, ERP hooks, API Mesh, PHP scope, App Builder workflows, and deploy checklist.
feature: App Builder, API Mesh, Extensibility, Paas, REST, Eventing
topic: App Builder, Commerce, Development, I/O Events, Integrations, Runtime
role: Developer, Leader, User
level: Intermediate
doc-type: Tutorial
duration: 309
jira: KT-20902
last-substantial-update: 2026-04-27
---
# Split payment POC: next steps after the proof of concept

The demo dashboard and simulation script you built in this tutorial are intentionally rough. They exist to prove the pattern. This page describes a practical path from proof of concept to production-style App Builder development.

---

## Step 1 — Replace the Demo Dashboard with an Experience Cloud UI Extension

The `demo-dashboard` web action serves HTML from a string inside a Node.js function. It works, but it is not the production pattern.

The proper replacement is the `commerce-backend-ui-1` extension in the `commerce-checkout-starter-kit` — a React application embedded in the Commerce Admin Shell via the Adobe Admin UI SDK. See [Split payment POC: Experience Cloud UI extension AI prompt](split-payment-poc-experience-cloud-ui-prompt.md) for the generation prompt.

**What changes:**
* Operators log in through Commerce Admin Shell (IMS authentication instead of a shared secret)
* The order list uses the IMS token context — no need for a demo secret
* Accept/decline actions are scoped to the operator's IMS identity
* The UI is embedded in Commerce Admin at the URL Commerce administrators already know

**What stays the same:**
* `payment-accept` and `payment-decline` App Builder actions are unchanged
* Commerce REST endpoints are unchanged
* The PHP module is unchanged

---

## Step 2 — Connect a Real ERP

The accept/decline flow in this PoC is driven by a human clicking a button. In production, this is driven by your ERP, CRM, or payment processor.

**The integration pattern:**
1. Your ERP system captures cash and calls `POST /payment-accept` (the App Builder web action URL) with `{ orderId: <entity_id> }`
2. App Builder validates the call (bearer token or API key — add auth middleware to `payment-accept`)
3. App Builder calls Commerce REST `cash-received`
4. Commerce invoices and ships the order

No PHP changes required. The REST surface is already there. The App Builder action just needs a secure caller instead of a dashboard button.

**Authentication options for the ERP caller:**
* Adobe I/O Runtime supports `require-adobe-auth: true` for IMS tokens (if your ERP can get an IMS token)
* For non-Adobe systems: add a simple API key check in the `payment-accept` action (check a header against a secret stored in the action's env)

---

## Step 3 — Add API Mesh as a Broker Layer

Currently, App Builder calls Commerce REST directly with OAuth 1.0a credentials. For larger deployments, Adobe API Mesh provides a managed gateway layer between App Builder and Commerce.

**Benefits:**
* Centralized credential management — API Mesh holds the Commerce credentials; App Builder calls API Mesh
* Request transformation — map App Builder payloads to Commerce REST shapes without changing the App Builder action
* Rate limiting and caching — protect Commerce from high-volume event traffic

**The pattern:**
* Replace `createCommerceClient(params, logger)` calls with calls to your API Mesh endpoint
* API Mesh handles OAuth signing toward Commerce

---

## Step 4 — Reduce the PHP Footprint

The current PHP module handles five things that must stay in-process (see [Split payment POC: architecture and design decisions](split-payment-poc-architecture-and-decisions.md)). As Adobe Commerce's API surface matures, some of these may become movable:

**Potentially movable in the future:**
* The store credit REST API is evolving — future versions may support applying credit post-order or to inactive carts
* As more Commerce operations become async-safe, the threshold guard may be movable to a pre-order API Mesh resolver

**Not movable (architectural constraints):**
* Quote manipulation before `placeOrder()` will always require in-process code unless Commerce exposes a clean hook via an API-first extension point
* The REST endpoints (`/V1/split-payment/*`) are specific to this feature; they live in Commerce because they call Commerce-internal services

---

## Step 5 — Add More Workflow to App Builder

The current PoC does one thing: listen for order placement, then enable accept/decline. Natural extensions:

**Fraud scoring before accept:**
In `payment-orchestrator`, after recording cash pending, call a fraud scoring API before the orchestration result is considered final. If the score is above a threshold, auto-decline instead of waiting for operator action.

**Notification emails:**
When `payment-accept` succeeds, trigger an email (via Adobe Campaign, SendGrid, or any HTTPS API) notifying the customer that their cash payment was confirmed.

**Loyalty point awards:**
After cash is confirmed, call a loyalty API to award points. This is pure App Builder — no PHP required.

**Timeout handling:**
Add a scheduled App Builder action (using `cron` in `app.config.yaml`) that scans for orders with `split_cash_status = 'pending'` older than X days and auto-declines them.

---

## Step 6 — Deploy to Production

The PoC is configured for `Stage` workspace. Moving to production:

```bash
# Switch to production workspace
aio app use
# Select Production workspace

# Update .env for production
# (same credentials, but production Commerce base URL)

# Deploy
aio app deploy
```

**Checklist for production readiness:**
* [ ] `DEMO_UI_SECRET` set (or demo dashboard replaced with Experience Cloud UI)
* [ ] `LOG_LEVEL=warn` or `error` in production (not `debug`)
* [ ] `PAYMENT_THRESHOLD` matches Commerce production config
* [ ] Commerce Integration credentials in `.env` are for a dedicated production integration (not staging)
* [ ] Fastly IP allowlist updated with App Builder production egress IPs (Commerce Cloud)
* [ ] I/O Event registration confirmed in production workspace

---

## Architecture Evolution Diagram

```
PoC (this tutorial)
┌─────────────────────────────────────────────────┐
│  Commerce                 App Builder            │
│  ┌─────────────┐         ┌──────────────────┐   │
│  │  PHP Module │◄────────│ payment-orchestr │   │
│  │  REST API   │────────►│ payment-accept   │   │
│  │  Checkout UI│         │ payment-decline  │   │
│  └─────────────┘         │ demo-dashboard   │   │
└─────────────────────────────────────────────────┘

Phase 2: Experience Cloud UI
┌─────────────────────────────────────────────────┐
│  Commerce                 App Builder            │
│  ┌─────────────┐         ┌──────────────────┐   │
│  │  PHP Module │◄────────│ payment-orchestr │   │
│  │  REST API   │────────►│ payment-accept   │   │
│  │  Checkout UI│         │ payment-decline  │   │
│  │             │         │ Admin UI ext.    │   │
│  └─────────────┘         └──────────────────┘   │
└─────────────────────────────────────────────────┘

Phase 3: Real ERP + API Mesh
┌──────────────────────────────────────────────────────────┐
│  ERP  ──►  App Builder  ──►  API Mesh  ──►  Commerce     │
│            (orchestrator)   (gateway)    (PHP module      │
│            (accept)                      REST surface)    │
└──────────────────────────────────────────────────────────┘
```

---

## Key References

* [Adobe App Builder documentation](https://developer.adobe.com/app-builder/docs/overview/){target="_blank"}
* [Adobe I/O Events for Commerce](https://developer.adobe.com/commerce/extensibility/events/){target="_blank"}
* [Commerce Checkout Starter Kit](https://github.com/adobe/commerce-checkout-starter-kit){target="_blank"}
* [Adobe Admin UI SDK](https://developer.adobe.com/commerce/extensibility/admin-ui-sdk/){target="_blank"}
* [Adobe API Mesh](https://developer.adobe.com/graphql-mesh-gateway/){target="_blank"}
* [Adobe I/O Runtime (OpenWhisk)](https://developer.adobe.com/runtime/docs/){target="_blank"}



{{$include /help/_includes/split-payment-ai-tools-related-links.md}}
