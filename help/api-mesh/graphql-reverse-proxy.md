---
title: Create a GraphQL reverse proxy to be used in API Mesh
description: Discover how to use API Mesh on Adobe Commerce and [!DNL Adobe App Builder]. Learn about creating a GraphQL reverse proxy.
landing-page-description: Discover how to use API Mesh on Adobe Commerce and [!DNL Adobe App Builder]. Learn about creating a GraphQL revers proxy.
kt: 11804
doc-type: tutorial
audience: all
last-substantial-update: 2023-2-2

---
# Create a GraphQL reverse proxy

The video helps a developer understand how to create a GraphQL reverse proxy. Remember, for GraphQL Mesh to work as expected, a publicly accessible URL with valid GraphQL schema is required. The video also explains how to set up your initial json for use with your commerce website. For basic code samples that was used in the video, visit [Create a mesh](https://developer.adobe.com/graphql-mesh-gateway/gateway/create-mesh/#create-a-mesh-1).

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

Here is an example of several sources

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
        "name": "ERP",
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

## What is a reverse proxy

As a developer using Adobe App Builder and GraphQL Mesh, it is not necessary to understand what a reverse proxy is. However you may be interested in the overall functionality as it pertains to Adobe App Builder. There are many good resources to be found on the internet.
For more information around the basic functionality of a reverse proxy here are a few external resources:

* [What is a reverse proxy](https://www.imperva.com/learn/performance/reverse-proxy/)
* [What is a reverse proxy and why does it matter](https://blog.hubspot.com/website/reverse-proxy)

## Who is this video for?

* Anyone who is new to API mesh
* Developers interested using multiple graphql sources
* Anyone who needs to know how to filter the network tab and filter by graphql

## Video content

* Using API as a reverse proxy
* JSON configuration with the Adobe Developer command-line interface
* Accessing the newly created GraphQL endpoint

PLACEHOLDER VIDEO URL needs to be updated
>[!VIDEO](https://video.tv.adobe.com/v/3414124)

{{$include /help/_includes/api-mesh-related-links.md}}
