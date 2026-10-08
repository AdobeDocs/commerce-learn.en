---
title: Get started with API Mesh
description: Learn how to use API Mesh on Adobe Commerce and Adobe App Builder, including installing App Builder, working with projects, and creating a reverse proxy.
jira: KT-11802
doc-type: Tutorial
duration: 422
last-substantial-update: 2023-08-27T00:00:00.000Z
feature: API Mesh, App Builder, Extensibility, Tools and External Services, Backend Development
topic: App Builder, I/O Events, Developer Console, Commerce, Development, Integrations
role: Developer
level: Intermediate
exl-id: baae6dab-48a4-49a0-b6f6-61cbebe63d0f
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: 72863f3c-9d27-5dda-afe1-d9f934b1fba0
    internal-label: Extensibility
  - id: b48dbafb-4193-5648-b9d9-bf96e9c9a411
    internal-label: Backend Development
  - id: c4f010fa-1478-4300-a88d-706fbc036a7a
    internal-label: APIs and SDKs
  - id: cc250cf1-34eb-4863-80d0-d170d45ea067
    internal-label: Developer tools
  - id: 125c1f49-aefd-5f34-a252-288937f95f6b
    internal-label: Marketing Tools
subfeature_v2:
  - id: ce84ce08-883f-4337-ae83-6bb1855ca732
    internal-label: API Mesh
  - id: a743e5dc-8f37-4b5d-a848-03c32ca30598
    internal-label: App Builder
  - id: 618ab558-d6ad-5352-99d6-d5702c6fdf80
    internal-label: Tools and External Services
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
---
# Get started with API Mesh

If you're new to API Mesh for Adobe Developer App Builder, Adobe recommends starting with this introductory tutorial, before progressing to the other videos and tutorials.

## What is API Mesh

API Mesh combines multiple sources of data to get a single response for your application to consume.

[View the full API Mesh documentation](https://developer.adobe.com/graphql-mesh-gateway/mesh/){target="_blank"}

## Who is this video for?

* Any developer new to API Mesh or [!DNL Adobe Commerce] with limited experience using [Adobe I/O Runtime](https://developer.adobe.com/app-builder/docs/intro_and_overview/what-is-app-builder){target="_blank"} and API Mesh.

## Video content

* Overview to API Mesh
* Links to supplemental documentation
* Use case for doing real time inventory check at checkout
* Moving development efforts and resource usage away from your commerce application

>[!VIDEO](https://video.tv.adobe.com/v/3417534?learn=on)

## Example use cases

Your Commerce application has a REST API and a GraphQL endpoint. For example, use the REST API to apply special pricing or the GraphQL endpoint to handle inventory status. Using API Mesh, you can define both endpoints, retrieve the information, and return it to the requesting application as one response.

## What is a reverse proxy

As a developer using Adobe App Builder and API Mesh, it is not necessary to understand the definition of a reverse proxy. However, if you are interested in the overall functionality as it pertains to Adobe App Builder, use the following resources:

* [What is a reverse proxy](https://www.imperva.com/learn/performance/reverse-proxy/){target="_blank"}


{{$include /help/_includes/api-mesh-related-links.md}}
