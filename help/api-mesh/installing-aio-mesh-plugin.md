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

Before starting, there are a few things that need to set up. First, the Adobe Developer IO command-line interface setup. Next, ensure that the API Mesh plugin is configured in each environment.
For instructions on setting up your local environment to run Node, nvm and installing the Adobe Developer IO be sure to visit [GraphQL Mesh Getting started](https://developer.adobe.com/graphql-mesh-gateway/gateway/getting-started/).

## Who is this video for?

* Developers new to Adobe App Builder or [!DNL Magento Open Source] with limited experience with Adobe Developer IO and API Mesh.

## Video content

* Introduction to API Mesh
* Installing Adobe Developer IO command-line interface
* Adding the API Mesh plugin to the AIO command line

>[!VIDEO](https://video.tv.adobe.com/v/3414122/)

## Example commands using NPM and AIO

Installing the Adobe Developer command-line interface is rather simple. After you have Node installed run this command `npm install -g @adobe/aio-cli`
Once the Adobe Developer cli is installed, it is possible to install the mesh plugin. You do this by running this command `aio plugins:install @adobe/aio-cli-plugin-api-mesh`

{{$include /help/_includes/api-mesh-related-links.md}}
