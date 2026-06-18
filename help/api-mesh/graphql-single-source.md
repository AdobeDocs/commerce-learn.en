---
title: Create a GraphQL single source mesh in API Mesh
description: Learn how to use API Mesh on Adobe Commerce and Adobe App Builder. Discover how to create a mesh with a single GraphQL source and access the new endpoint.
jira: KT-11804
doc-type: Tutorial
duration: 485
last-substantial-update: 2023-02-08
feature: API Mesh, App Builder, Extensibility, Tools and External Services, Backend Development
topic: App Builder, I/O Events, Developer Console, Commerce, Development, Integrations
role: Developer
level: Beginner
exl-id: 9a78457a-1539-49c0-ac69-4bbfc6786137
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
