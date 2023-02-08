---
title: Create a GraphQL single source request to be used in API Mesh
description: Discover how to use API Mesh on Adobe Commerce and [!DNL Adobe App Builder]. Learn about creating a request that has one source.
landing-page-description: Discover how to use API Mesh on Adobe Commerce and [!DNL Adobe App Builder]. Learn about creating a request that has one source.
kt: 11804
doc-type: tutorial
audience: all
last-substantial-update: 2023-2-7

---
# Create single source GraphQL request

The video helps a developer understand how to create a GraphQL reverse proxy and has a single source. Remember, for GraphQL Mesh to work as expected, a publicly accessible URL with valid GraphQL schema is required. The video also explains how to set up your initial json for use with your commerce website. For basic code samples that was used in the video, visit [Create a mesh](https://developer.adobe.com/graphql-mesh-gateway/gateway/create-mesh/#create-a-mesh-1).

## Who is this video for?

* Anyone who is new to API mesh
* Developers interested using multiple graphql sources
* Anyone who needs to know how to filter the network tab and filter by graphql

## Video content

* Using API as a reverse proxy
* JSON configuration with the Adobe Developer command-line interface
* Accessing the newly created GraphQL endpoint

>[!VIDEO](https://video.tv.adobe.com/v/3414124)

## Create the json configuration file

For Adobe App Builder to know about all your sources, you define them in a JSON configuration. Each source is an element in an array and you can have one or more. Here is an example of a single source

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
