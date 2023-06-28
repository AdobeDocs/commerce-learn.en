---
title: Create a multiple source GraphQL to be used in API Mesh
description: Discover how to use multiple sources for API Mesh on Adobe Commerce and [!DNL Adobe App Builder]. Learn about some common errors and how to resolve them.
landing-page-description: Discover how to use API Mesh on Adobe Commerce and [!DNL Adobe App Builder]. Learn about creating a mesh that has multiple sources and how to resolve some common errors.
short-description: Discover how to use API Mesh on Adobe Commerce and [!DNL Adobe App Builder]. Learn about creating a mesh that has multiple sources and how to resolve some common errors.
kt: 11804
doc-type: tutorial
audience: all
last-substantial-update: 2023-2-8
feature: API Mesh, App Builder, Extensibility, Tools and External Services, Backend Development
topic: App Builder, I/O Events, Developer Console, Commerce, Development, Integrations
role: Architect, Developer
level: Beginner, Intermediate
exl-id: d788a068-9d20-4db0-a0eb-fd897873253d
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

>[!VIDEO](https://video.tv.adobe.com/v/3414125?quality=12&learn=on)

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
