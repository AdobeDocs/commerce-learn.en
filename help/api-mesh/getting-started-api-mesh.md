---
title: Get started with API Mesh
description: Discover how to use API Mesh on Adobe Commerce and [!DNL Adobe App Builder]. Learn about installing Adobe Developer, working with projects, creating a graphql reverse proxy and much more.
landing-page-description: Discover how to use API Mesh on Adobe Commerce and [!DNL Adobe App Builder]. Learn about installing Adobe IO, working with projects, creating a graphql reverse proxy and much more.
kt: 11802
doc-type: tutorial
audience: all
last-substantial-update: 2023-1-31

---
# Get started with API Mesh

If you're new to API Mesh, Adobe recommends starting with this introductory tutorial before digging in to the accompanying videos and tutorials.

## What is API Mesh

API Mesh allows for multiple sources of data to be used to provide a single response for your commerce application to consume. 

[View the full API Mesh documentation](https://developer.adobe.com/graphql-mesh-gateway/gateway/overview/)

## Example use cases

The backend system for your Commerce application has a REST API you can use to get special pricing. Another backend system that has a GraphQL endpoint handles inventory status. Using API Mesh, you can define both endpoints, retrieve the information, and return it to the requesting application as one response.

## What is a reverse proxy

As a developer using Adobe App Builder and GraphQL Mesh, it is not necessary to understand what a reverse proxy is. However you may be interested in the overall functionality as it pertains to Adobe App Builder. There are many good resources to be found on the internet.
For more information around the basic functionality of a reverse proxy here are a few external resources:

* [What is a reverse proxy](https://www.imperva.com/learn/performance/reverse-proxy/)
* [What is a reverse proxy and why does it matter](https://blog.hubspot.com/website/reverse-proxy)

{{$include /help/_includes/api-mesh-related-links.md}}
