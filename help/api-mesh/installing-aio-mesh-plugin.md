---
title: Installing Adobe Developer IO command-line interface and API Mesh plugin
description: Discover how to install Adobe Developer IO command-line interface and the API Mesh plugin
landing-page-description: Discover how to use Adobe App Builder and install the Adobe Developer IO with API Mesh plugin.
kt: 11801
doc-type: tutorial
audience: all
last-substantial-update: 2023-2-8

---

# Installing Adobe Developer IO and Mesh plugin

Before you begin using API Mesh for Adobe Developer App Builder, you'll need to install the `aio` CLI and the API Mesh plugin.
For installation instructions and prerequisites, visit the API Mesh [Getting started](https://developer.adobe.com/graphql-mesh-gateway/gateway/getting-started/) page.

## Who is this video for?

* Developers new to API Mesh or [!DNL Adobe Commerce] with limited experience using [Adobe IO](https://developer.adobe.com/runtime/docs/guides/overview/) and API Mesh.

## Video content

* Introduction to API Mesh
* Installing the Adobe IO CLI (command-line interface)
* Installing the API Mesh plugin

>[!VIDEO](https://video.tv.adobe.com/v/3414122/)

## Installing the `aio` CLI and API Mesh plugin

After installing `node` and `npm`, run the following command to install the `aio` CLI:

```bash
npm install -g @adobe/aio-cli
```

Once the Adobe IO CLI is installed, use the following command to install the API Mesh plugin:

```bash
aio plugins:install @adobe/aio-cli-plugin-api-mesh
```

{{$include /help/_includes/api-mesh-related-links.md}}
