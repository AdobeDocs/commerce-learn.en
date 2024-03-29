---
title: Installing Adobe I/O Runtime  command-line interface and API Mesh plugin
description: Discover how to install Adobe I/O Runtime command-line interface and the API Mesh plugin
landing-page-description: Discover how to use Adobe App Builder and install the Adobe I/O Runtime with API Mesh plugin.
short-description: Discover how to use Adobe App Builder and install the Adobe I/O Runtime with API Mesh plugin.
kt: 11801
doc-type: tutorial
audience: all
last-substantial-update: 2023-2-8
feature: API Mesh, App Builder, Extensibility, Tools and External Services, Backend Development
topic: App Builder, I/O Events, Developer Console, Commerce, Development, Integrations
role: Architect, Developer
level: Beginner, Intermediate
exl-id: 898a0918-0362-4fa4-9204-d770ff1a7e6f
---
# Installing Adobe I/O Runtime CLI and Mesh plugin

Before you begin using API Mesh for Adobe Developer App Builder, you need to install the `aio` CLI and the API Mesh plugin.
For installation instructions and prerequisites, visit the API Mesh [Getting started](https://developer.adobe.com/graphql-mesh-gateway/gateway/getting-started/){target="_blank"} page.

## Who is this video for?

* Developers new to API Mesh or [!DNL Adobe Commerce] with limited experience using [Adobe I/O Runtime](https://developer.adobe.com/runtime/docs/guides/overview/){target="_blank"} and API Mesh.

## Video content

* Introduction to API Mesh
* Installing the Adobe I/O Runtime CLI (command-line interface)
* Installing the API Mesh plugin

>[!VIDEO](https://video.tv.adobe.com/v/3414122?quality=12&learn=on)

## Installing the `aio` CLI and API Mesh plugin

After installing `node` and `npm`, run the following command to install the `aio` CLI:

```bash
npm install -g @adobe/aio-cli
```

Once the Adobe I/O Runtime CLI is installed, use the following command to install the API Mesh plugin:

```bash
aio plugins:install @adobe/aio-cli-plugin-api-mesh
```

{{$include /help/_includes/api-mesh-related-links.md}}
