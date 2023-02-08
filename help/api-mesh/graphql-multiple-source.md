---
title: Create a multiple source GraphQL to be used in API Mesh
description: Discover how to use multiple sources for API Mesh on Adobe Commerce and [!DNL Adobe App Builder]. Learn about some common errors and how to resolve them.
landing-page-description: Discover how to use API Mesh on Adobe Commerce and [!DNL Adobe App Builder]. Learn about creating a request that has multiple sources and how to resolve some common errors.
kt: 11804
doc-type: tutorial
audience: all
last-substantial-update: 2023-2-7

---
# Create multiple source GraphQL request

The video helps a developer understand how to create a GraphQL reverse proxy with multiple sources. This video shows how to stitch different sources, identifying errors and saving changes to git. For basic code samples that was used in the video, visit [Create a mesh](https://developer.adobe.com/graphql-mesh-gateway/gateway/create-mesh/#create-a-mesh-1).

## Who is this video for?

* Anyone who is new to API mesh
* Developers interested using multiple graphql sources
* Anyone who needs to know how to filter the network tab and filter by graphql

## Video content

* How Complex Custom Attributes API schema from a second source can override the default source schema
* Modifying the api mesh configuration to account for the second overriding schema
* How to troubleshoots errors that might occur in the process like naming conflict, schema availability and other SDL syntax
* Example of common errors after attempts to stitch schemas
* Rebuilding the api mesh after edits
* Saving changes to git after modifying API Mesh config

>[!VIDEO](https://video.tv.adobe.com/v/3414125)

## Create the json configuration file

For Adobe App Builder to know about all your sources, you define them in a JSON configuration. Each source is an element in an array and you can have one or more. Here is an example of a multiple source request that are meshed together to form a single response.

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

{{$include /help/_includes/api-mesh-related-links.md}}
