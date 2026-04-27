---
title: "Split payment POC: tutorial quick reference for authors"
description: Learn about the split payment POC file map: which Experience League page matches each AI prompt, suggested section order, and author notes for Luma checkout.
feature: App Builder, Extensibility, Paas, REST, Eventing
topic: App Builder, Commerce, Development, I/O Events, Integrations, Runtime
role: Developer, Leader, User
level: Intermediate
doc-type: Tutorial
duration: 491
jira: KT-20902
last-substantial-update: 2026-04-27
---
# Split payment POC: tutorial quick reference for authors

This page summarizes how the split payment proof-of-concept tutorial series is organized. It maps each numbered source prompt file to its published Experience League page, lists a suggested section order for readers, and collects notes for authors and maintainers.


## Overview: What changed from the original prompts

The original AI prompt files (`CLAUDE_PROMPT.md`, `THE_JOURNEY.md`, `SETUP_CHECKLIST.md`, `ENV_REFERENCE.md`) were accurate but structured as a single monolithic prompt and loose supporting documents. They were reorganized into a numbered sequence of self-contained files that can be used as distinct tutorial sections or given to AI tools independently.

**Key improvements:**

* Each file has a single, clear purpose
* Build prompts are complete and self-contained — copy, paste, and run
* Architecture reasoning is separated from build instructions (so it can be skipped by experienced developers)
* Customization callouts explicitly mark everything that must change for non-Luma themes
* Testing guide is step-by-step and covers common failure modes with fixes
* The Experience Cloud UI extension prompt is now a separate file (it was missing from the original prompts)
* The simulation script context and usage are now part of the testing guide rather than scattered


## File-by-file reference

### [Create a split payment POC: App Builder and AI tools](create-a-split-payment-poc-app-builder-and-ai-tools.md)

**Source label:** `00_TUTORIAL_OVERVIEW.md` (conceptual overview; the published series opens with this introduction and video.)

**Purpose:** Introduction and orientation for the tutorial.

**Why it's needed:** Gives developers the "why" before the "how." Explains what they will build, who the audience is, and critically — what they must customize if their site differs from a clean Luma installation. Also serves as the table of contents for the rest of the series.

**Tutorial use:** Opening section. Sets context before any technical steps.


### [Split payment POC: architecture and design decisions](split-payment-poc-architecture-and-decisions.md)

**Source label:** `01_ARCHITECTURE_AND_DECISIONS.md`

**Purpose:** Deep-dive explanation of every architectural decision in the PoC.

**Why it's needed:** The single most common point of confusion when working with this PoC is understanding *why* something is in PHP versus App Builder. Without this context, developers try to move things that cannot be moved (like store credit application) and fail. This document pre-empts those failures with clear reasoning.

**Key topics covered:**

* The "what must stay in PHP" rule and why
* The threshold double-enforcement pattern
* Why store credit application cannot be async
* The five Commerce edge cases handled by plugins
* The extension attribute data flow from checkout → quote → order → I/O Event → App Builder

**Tutorial use:** "Architecture" or "How it works" section. Can be skipped by experienced Commerce developers but is essential for App Builder newcomers.


### [Split payment POC: prerequisites and environment setup](split-payment-poc-prerequisites-and-setup.md)

**Source label:** `02_PREREQUISITES_AND_SETUP.md`

**Purpose:** Complete pre-flight checklist before any code is written or prompts are run.

**Why it's needed:** The setup phase has the highest failure rate in tutorials. This document ensures Commerce Admin is configured correctly (exact COD title, store credit enabled, test customer has balance, integration created), the App Builder project has I/O Events and the Commerce event provider connected, and the local environment has the right versions.

**Emphasis items:**

* Cash on delivery title must be exactly `Cash` (critical — the JavaScript does string matching)
* Commerce integration must be *activated* (not just saved) for the OAuth credentials to work
* `entity_id` versus `increment_id` explained here to prevent confusion throughout

**Tutorial use:** "Prerequisites" or "Getting started" section. Should be completed interactively — not just read.


### [Split payment POC: environment variables reference](split-payment-poc-env-reference.md)

**Source label:** `03_ENV_REFERENCE.md`

**Purpose:** All environment variables for all three components in one place.

**Why it's needed:** The same four OAuth credentials appear in three different files with different variable names (`COMMERCE_*` versus `COMMERCE_INTEGRATION_*`). Having a single reference prevents the "why isn't this working" debugging where one credential set has a typo.

**Components covered:**

* `split-payment-orchestrator/.env`
* `commerce-checkout-starter-kit/.env` (IMS + OAuth)
* `commerce-backend-ui-1/.env.simulation`

**Tutorial use:** Reference sidebar or "Configuration" section. Also used as a companion to the build prompts.


### [Split payment POC: Commerce module AI prompt](split-payment-poc-commerce-module-prompt.md)

**Source label:** `04_COMMERCE_MODULE_PROMPT.md`

**Purpose:** Complete, self-contained AI prompt to generate the entire `Client_SplitPayment` PHP module.

**Why it's needed:** This is the primary AI build artifact for the PHP side. It is written so that a developer with no PHP experience can hand it to Cursor (with Claude) and get a working module. Every file is specified, every behavioral contract is defined, critical implementation notes are included, and the commands to enable the module afterward are provided.

**Coverage:**

* Complete file structure (30+ files)
* Database schema, extension attributes, REST endpoints, I/O Events config
* All PHP classes with full behavioral specs (not just signatures)
* KnockoutJS checkout component specs
* The five edge case plugins with explanations of why each exists
* Customization callouts for non-Luma themes

**Tutorial use:** "Build the Commerce module" section. The prompt itself is the artifact — developers copy it into their AI tool and run it.


### [Split payment POC: App Builder orchestrator AI prompt](split-payment-poc-app-builder-orchestrator-prompt.md)

**Source label:** `05_APP_BUILDER_ORCHESTRATOR_PROMPT.md`

**Purpose:** Complete, self-contained AI prompt to generate the `split-payment-orchestrator` App Builder application.

**Why it's needed:** The four App Builder actions (`payment-orchestrator`, `payment-accept`, `payment-decline`, `demo-dashboard`) are the core of the "what moved out of PHP" story. This prompt generates all of them with full behavioral specifications, correct `app.config.yaml` structure, and the event registration configuration.

**Coverage:**

* `app.config.yaml` with all four actions and the I/O Event registration
* `commerce-client.js` OAuth 1.0a shared client
* All four actions with complete logic specs
* The `store-credit.js` deprecated stub (with explanation of *why* it's not used — this is pedagogically important)
* The demo dashboard with HTML rendering, order filtering, and security
* `.env.example` with all variables

**Tutorial use:** "Build the App Builder application" section. Companion to the Commerce module prompt.


### [Split payment POC: Experience Cloud UI extension AI prompt](split-payment-poc-experience-cloud-ui-prompt.md)

**Source label:** `06_EXPERIENCE_CLOUD_UI_PROMPT.md`

**Purpose:** AI prompt to generate the optional Experience Cloud Admin UI SDK extension.

**Why it's needed:** The demo dashboard in the orchestrator prompt is intentionally rough — it is proof-of-concept, not production. This section shows developers the next step: embedding the split payment dashboard into the Commerce Admin Shell using the Admin UI SDK. It was missing entirely from the original prompts.

**Coverage:**

* `ext.config.yaml` for the Admin UI SDK extension
* React components for the order dashboard and order detail
* Backend actions using IMS auth for listing and OAuth for accept/decline
* The simulation script (also used for testing)

**Tutorial use:** Optional "Going further" or "Production path" section. Can be skipped if the tutorial focuses only on the PoC.


### [Split payment POC: testing and verification guide](split-payment-poc-testing-and-verification.md)

**Source label:** `07_TESTING_AND_VERIFICATION.md`

**Purpose:** Step-by-step testing guide covering every component in the correct verification order.

**Why it's needed:** Building the components is half the work. Developers need a clear verification path that starts from the lowest level (database columns, REST endpoints) and builds to the full end-to-end flow. The original prompts had a setup checklist but no explicit testing flow.

**Coverage:**

* Commerce module installation verification
* Admin configuration verification
* REST endpoint smoke tests (curl commands)
* Checkout UI walkthrough (including validation cases)
* Threshold guard test
* Full order placement test
* Simulation script usage for accept and decline
* Demo dashboard usage
* App Builder action log inspection
* Ten common failure modes with specific fixes

**Tutorial use:** "Testing" or "Verification" section. Also valuable as a troubleshooting reference.


### [Split payment POC: next steps after the proof of concept](split-payment-poc-next-steps.md)

**Source label:** `08_NEXT_STEPS.md`

**Purpose:** Roadmap for evolving the PoC into production-ready patterns.

**Why it's needed:** A PoC tutorial risks leaving developers with a "what now?" feeling. This document maps the natural progressions from demo to production: replacing the demo dashboard with an Experience Cloud extension, connecting a real ERP, adding API Mesh, expanding App Builder workflow, and production deployment checklist.

**Key content:**

* Architecture evolution diagram (PoC → Phase 2 → Phase 3)
* ERP integration pattern (what changes, what stays the same)
* API Mesh broker pattern
* Production deployment checklist
* Key reference links

**Tutorial use:** "Next steps" closing section. Also useful as a conversation starter for scoping a real project.


## Suggested tutorial sections

Based on these files, a typical structure for readers is:

| Tutorial section | Experience League page |
| --- | --- |
| Introduction and learning objectives | [Create a split payment POC: App Builder and AI tools](create-a-split-payment-poc-app-builder-and-ai-tools.md) |
| End-to-end demo (video) | [Create a split payment POC: App Builder full demo](create-a-split-payment-poc-app-builder-and-ai-tools-full-demo.md) |
| Architecture: what lives where | [Split payment POC: architecture and design decisions](split-payment-poc-architecture-and-decisions.md) |
| Prerequisites and setup | [Split payment POC: prerequisites and environment setup](split-payment-poc-prerequisites-and-setup.md) |
| Environment variables | [Split payment POC: environment variables reference](split-payment-poc-env-reference.md) |
| Step 1: Build the Commerce module | [Split payment POC: Commerce module AI prompt](split-payment-poc-commerce-module-prompt.md) |
| Step 2: Build the App Builder orchestrator | [Split payment POC: App Builder orchestrator AI prompt](split-payment-poc-app-builder-orchestrator-prompt.md) |
| Step 3: Test the end-to-end flow | [Split payment POC: testing and verification guide](split-payment-poc-testing-and-verification.md) |
| Step 4 (optional): Admin UI extension | [Split payment POC: Experience Cloud UI extension AI prompt](split-payment-poc-experience-cloud-ui-prompt.md) |
| Next steps and production path | [Split payment POC: next steps after the proof of concept](split-payment-poc-next-steps.md) |


## Important notes for tutorial authors

**On the Luma theme assumption:** Every build prompt generates code for a clean Luma installation. The tutorial should clearly state this at the top — developers with custom checkouts will need to adapt the `LayoutProcessorPlugin` injection paths and possibly the RequireJS configuration. The series introduction and build prompts include customization callouts for this.

**On the PHP module:** The tutorial explicitly does not provide the PHP code as a copy-paste download. The AI prompt *generates* it. This is intentional — it teaches the pattern of using AI to create Commerce extensions, not just copy-paste boilerplate. However, the generated code when prompted on a clean environment should match the working code in `app/code/Client/SplitPayment/` exactly.

**On the $100 threshold:** This is a hard-coded PoC value. The tutorial should note that real stores will want to configure this via Commerce Admin configuration rather than a compile-time constant.

**On store credit dependency:** The split payment flow as built requires `Magento_CustomerBalance` (the native store credit module). This is part of Adobe Commerce (not Magento Open Source). Developers on Magento Open Source will need a different store credit source or a third-party module.



{{$include /help/_includes/split-payment-ai-tools-related-links.md}}
