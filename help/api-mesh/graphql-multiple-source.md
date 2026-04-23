---
title: Create a multiple source GraphQL to be used in API Mesh
description: Discover how to use multiple sources for API Mesh on Adobe Commerce and [!DNL Adobe App Builder]. Learn about some common errors and how to resolve them.
jira: KT-11804
doc-type: Tutorial
duration: 409
last-substantial-update: 2023-02-08T00:00:00.000Z
feature: API Mesh, App Builder, Extensibility, Tools and External Services, Backend Development
topic: App Builder, I/O Events, Developer Console, Commerce, Development, Integrations
role: Developer
level: Beginner, Intermediate
exl-id: d788a068-9d20-4db0-a0eb-fd897873253d
TQID: https://experienceleague.adobe.com/O6ONn4NzMP-VqN0nsCoD-OPkZGMBelLWB-KNP1fZqmA
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: dac87252-6066-4d6e-a9d2-f6d84c323de7
    internal-label: Configuration
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
topic_v2:
  - id: a004cc84-67b9-4a33-a3a7-8ec7273ef4dc
    internal-label: Metadata
---
# Create a mesh with multiple sources

This video helps developers understand how to create a mesh with multiple sources in API Mesh for Adobe Developer App Builder. This video shows how to create a mesh with multiple sources and identify errors. For more details and code samples, visit [Create a mesh](https://developer.adobe.com/graphql-mesh-gateway/gateway/create-mesh/#create-a-mesh-1){target="_blank"}.

## Who is this video for?

* Anyone who is new to API mesh
* Developers interested in combining multiple API and GraphQL sources

## Video content

* How to use [transforms](https://developer.adobe.com/graphql-mesh-gateway/gateway/transforms/){target="_blank"} to modify the default source schema
* How to troubleshoot errors, such as name conflicts, schema availability, and other schema syntax issues
* Updating your mesh with a modified configuration

>[!VIDEO](https://video.tv.adobe.com/v/3414125?learn=on)

## Create the json configuration file

API Mesh uses a JSON configuration file to define your source handlers. The JSON file contains a `sources` array that contains the sources for your mesh. Here is an example of a mesh with multiple sources.

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
      },
      {
        "name": "Example",
        "handler": {
          "graphql": {
            "endpoint": "https://www.example.com/graphql/"
          }
        }
      }
    ]
  }
}
```

{{$include /help/_includes/api-mesh-related-links.md}}
