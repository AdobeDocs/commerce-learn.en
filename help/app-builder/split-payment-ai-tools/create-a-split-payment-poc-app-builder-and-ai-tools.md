---
title: "Create a split payment POC: App Builder and AI tools"
description: Learn about a split payment proof of concept with App Builder and Commerce PaaS, including the goals, architecture, and what this first session covers.
feature: App Builder, Paas, Payments
topic: App Builder, Commerce, Development, Integrations
role: Developer, Leader, User
level: Intermediate
doc-type: Technical Video
duration: 259
jira: KT-20791
---
# Create a split payment POC: App Builder and AI tools

This is the first of a set of tutorialsthat introduce you to using AI-assisted development to help you build a split payment proof of concept. You work with Adobe App Builder and Adobe Commerce in the cloud (PaaS) or on-premises, moving from an overview in this session to the hands-on tutorials that follow. Expect goals, high-level architecture, and a roadmap to what the rest of the series covers.

## Video

>[!VIDEO](https://video.tv.adobe.com/v/3483933?learn=on)

## Important Details


This tutorial bridges the gap between where most Adobe Commerce teams are today — deep in PHP — and where Adobe wants them to go: event-driven, serverless business logic running outside Commerce in Adobe App Builder. It does this through a real, working feature rather than a toy example.

### What You'll Actually Build

A split payment system where customers pay using a combination of Cash on Delivery and Store Credit. After the order is placed, an operator (or ERP system) confirms or declines the cash payment through a standalone dashboard — without ever opening Commerce Admin. The entire accept/decline workflow runs in App Builder.
The Architectural Lesson (This Is the Core Teaching)
The tutorial demonstrates a deliberate and repeatable decision framework:

What must stay in PHP: anything that runs synchronously in the Commerce request cycle, or that calls Commerce-internal APIs with no clean external surface
What moves to App Builder: everything else — event processing, operator workflow, external integrations, and operator-facing tools

This isn't "move everything to App Builder." It's a practical, honest starting point for teams who need to begin the transition without a rewrite.

### Why the PHP Code Isn't Included

The AI prompt approach is actually better than sample code for this use case, because the prompt captures the behavioral contracts and architectural reasoning that sample code alone cannot convey. A developer who runs the prompt and reads the output understands why the code is shaped the way it is, not just what it looks like.

### What Is Included

Complete App Builder application code (consistent across projects — use it directly or as a reference)
A full set of numbered AI prompts designed for Cursor and Claude, covering the Commerce module, the App Builder orchestrator, the operator dashboard, testing, and the path to production
A simulation script to test the accept/decline flow against a live Commerce site without needing a real ERP
Architecture documentation explaining every decision

### Who This Is For

Developers on Adobe Commerce on-premise or Commerce Cloud who are starting their first real App Builder integration. Not for the fully headless API-first deployment — specifically for teams in the transition, running a traditional storefront, who want to see how to offload real business logic to App Builder without abandoning their existing PHP investment.

### Prerequisites Callout

Adobe Commerce 2.4.5 or later, access to an Adobe Developer Console organization with an App Builder project, and I/O Events enabled. A clean Luma theme is assumed for the checkout UI — custom themes will require adjusting the prompt before running it.

### Final thoughts

This should be considered an entry level discussion on AI-assisted development. This tutorial is a demonstration for using AI tools in a Commerce development workflow, not just a tutorial about split payments.
