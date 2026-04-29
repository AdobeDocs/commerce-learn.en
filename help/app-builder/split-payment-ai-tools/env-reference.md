---
title: "Split payment POC: environment variables reference"
description: Learn how to map Commerce OAuth, base URL, payment threshold, and optional demo settings to the orchestrator, UI extension, and simulation environment files.
feature: App Builder, Configuration, Extensibility, Paas, REST, Security
topic: App Builder, Commerce, Development, I/O Events, Integrations, Runtime
role: Developer, Leader, User
level: Intermediate
doc-type: Tutorial
duration: 115
jira: KT-20902
last-substantial-update: 2026-04-27
---
# Split payment POC: environment variables reference

The same four Commerce OAuth credentials are used in every component. In **[!UICONTROL Commerce Admin]**, create one **[!UICONTROL Integration]**, then reuse the four values in every `.env` file below. (See [Split payment POC: prerequisites and environment setup](split-payment-poc-prerequisites-and-setup.md) for the activation steps.)

## The four OAuth credentials (used everywhere)

| Variable | Where to get it |
| --- | --- |
| `COMMERCE_CONSUMER_KEY` | **[!UICONTROL Commerce Admin]** > **[!UICONTROL System]** > **[!UICONTROL Integrations]** > *[your integration]* |
| `COMMERCE_CONSUMER_SECRET` | Same as above — values are only shown at activation |
| `COMMERCE_ACCESS_TOKEN` | Same as above |
| `COMMERCE_ACCESS_TOKEN_SECRET` | Same as above |


## App Builder orchestrator

### `split-payment-orchestrator/.env`

Copy from `.env.example` in the orchestrator directory. Do not commit this file.

```dotenv
# Commerce REST base URL — no trailing slash
COMMERCE_BASE_URL=https://your-store.example.com

# OAuth 1.0a integration credentials
COMMERCE_CONSUMER_KEY=
COMMERCE_CONSUMER_SECRET=
COMMERCE_ACCESS_TOKEN=
COMMERCE_ACCESS_TOKEN_SECRET=

# Must match split_payment/general/threshold in Commerce config (default: 100)
# Both Commerce and App Builder fall back to 100 if this is missing, non-numeric, or ≤ 0
PAYMENT_THRESHOLD=100

LOG_LEVEL=info

# Demo dashboard: if set, requires ?secret=<value> in URL or x-demo-secret header
# Leave empty for private staging only (anyone with the URL can list/accept orders)
DEMO_UI_SECRET=

# Optional: override the base URL used in dashboard action links (useful behind proxies)
DEMO_UI_BASE_URL=
```


## Experience Cloud UI extension (commerce-checkout-starter-kit)

### `commerce-checkout-starter-kit/.env`

This component uses two credential sets: IMS for order listing with the **[!UICONTROL Admin]** UI SDK, and OAuth 1.0a for accept and decline actions.

```dotenv
# IMS — used by CustomMenu/commerce-rest-api to list orders
# The Admin UI SDK provides the IMS token context; these set the Commerce base URL
COMMERCE_BASE_URL=https://your-store.example.com
OAUTH_CLIENT_ID=
OAUTH_CLIENT_SECRETS=
OAUTH_TECHNICAL_ACCOUNT_ID=
OAUTH_TECHNICAL_ACCOUNT_EMAIL=
OAUTH_SCOPES=
OAUTH_IMS_ORG_ID=
AIO_CLI_ENV=stage

# OAuth 1.0a — same four credentials, COMMERCE_INTEGRATION_ prefix
COMMERCE_INTEGRATION_BASE_URL=https://your-store.example.com
COMMERCE_INTEGRATION_CONSUMER_KEY=
COMMERCE_INTEGRATION_CONSUMER_SECRET=
COMMERCE_INTEGRATION_ACCESS_TOKEN=
COMMERCE_INTEGRATION_ACCESS_TOKEN_SECRET=
```


## Simulation script

### `commerce-backend-ui-1/.env.simulation`

Copy from `.env.simulation.example` in the same directory.

```dotenv
COMMERCE_BASE_URL=https://your-store.example.com
COMMERCE_CONSUMER_KEY=
COMMERCE_CONSUMER_SECRET=
COMMERCE_ACCESS_TOKEN=
COMMERCE_ACCESS_TOKEN_SECRET=
```


## Notes

**`PAYMENT_THRESHOLD`** — Must match `split_payment/general/threshold` in **[!UICONTROL Commerce]** system configuration. Both sides default to `100` if the value is missing, not numeric, or less than or equal to `0`. If you change the threshold in **[!UICONTROL Commerce]**, update the App Builder `.env` to match.

**`DEMO_UI_SECRET`** — Optional but recommended for any deployment that is not localhost. Anyone with the dashboard URL can list orders and run accept and decline if this is empty. For a real staging environment, set a shared secret.

**`COMMERCE_BASE_URL`** — Never include a trailing slash. The Commerce REST client appends `/rest/V1/` automatically.

**`AIO_CLI_ENV`** — Set to `stage` for the **[!UICONTROL Stage]** workspace. Change to `prod` when you deploy to **[!UICONTROL Production]**.


{{$include /help/_includes/split-payment-ai-tools-related-links.md}}
