---
title: Create a GraphQL single source mesh in API Mesh
description: Learn how to use API Mesh on Adobe Commerce and Adobe App Builder. Discover how to create a mesh with a single GraphQL source and access the new endpoint.
jira: KT-11804
doc-type: Tutorial
duration: 485
last-substantial-update: 2023-02-08T00:00:00.000Z
feature: API Mesh, App Builder, Extensibility, Tools and External Services, Backend Development
topic: App Builder, I/O Events, Developer Console, Commerce, Development, Integrations
role: Developer
level: Beginner
exl-id: 9a78457a-1539-49c0-ac69-4bbfc6786137
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
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
---
# Create a mesh with a single source

This video helps developers understand how to create a mesh with a single source in API Mesh for Adobe Developer App Builder. For this basic example to function, you need a publicly accessible API or GraphQL endpoint. The video also explains how to create a simple `mesh.json` file to use with your Commerce instance. For more details and code samples, visit [Create a mesh](https://developer.adobe.com/graphql-mesh-gateway/mesh/basic/create-mesh){target="_blank"}.

## Who is this video for?

* Anyone new to API mesh
* Developers interested in combining multiple GraphQL and API sources
* Anyone who needs to know how to filter the network tab and filter by GraphQL

## Video content

* Using API Mesh as a reverse proxy
* Creating a mesh from a JSON configuration file
* Accessing the newly-created GraphQL endpoint

>[!VIDEO](https://video.tv.adobe.com/v/3414124?learn=on)

## Create the JSON configuration file

API Mesh uses a JSON configuration file to define your source handlers. The JSON file contains a `sources` array that contains the sources for your mesh. The following is an example of a mesh with a single source.

```json
{
"meshConfig": {
    "sources": [
      {
        "name": "Commerce",
        "handler": {
          "graphql": {
            "endpoint": "https://venia.magento.com/graphql/"
          }
        }
      }
    ]
  }
}
```

{{$include /help/_includes/api-mesh-related-links.md}}
