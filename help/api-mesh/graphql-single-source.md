---
title: Create a GraphQL single source mesh in API Mesh
description: Discover how to use API Mesh on Adobe Commerce and [!DNL Adobe App Builder]. Learn about creating a mesh that has one source.
landing-page-description: Discover how to use API Mesh on Adobe Commerce and [!DNL Adobe App Builder]. Learn about creating a mesh that has one source.
short-description: Discover how to use API Mesh on Adobe Commerce and [!DNL Adobe App Builder]. Learn about creating a mesh that has one source.
kt: 11804
doc-type: tutorial
audience: all
last-substantial-update: 2023-2-8
feature: API Mesh, App Builder, Extensibility, Tools and External Services, Backend Development
topic: App Builder, I/O Events, Developer Console, Commerce, Development, Integrations
old-role: Architect, Developer
role: Developer
level: Beginner, Intermediate
exl-id: 9a78457a-1539-49c0-ac69-4bbfc6786137
---
# Create a mesh with a single source

This video helps developers understand how to create a mesh with a single source in API Mesh for Adobe Developer App Builder. For this basic example to work as expected, you need a publicly accessible API or GraphQL endpoint. The video also explains how to create a simple `mesh.json` file to use with your Commerce instance. For more details and code samples, visit [Create a mesh](https://developer.adobe.com/graphql-mesh-gateway/gateway/create-mesh/#create-a-mesh-1){target="_blank"}.

## Who is this video for?

* Anyone new to API mesh
* Developers interested in combining multiple GraphQL and API sources
* Anyone who needs to know how to filter the network tab and filter by GraphQL

## Video content

* Using API Mesh as a reverse proxy
* Creating a mesh from a JSON configuration file
* Accessing the newly created GraphQL endpoint

>[!VIDEO](https://video.tv.adobe.com/v/3414124?quality=12&learn=on)

## Create the json configuration file

API Mesh uses a JSON configuration file to define your source handlers. The JSON file contains a `sources` array that contains the sources for your mesh. Here is an example of a mesh with a single source.

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
