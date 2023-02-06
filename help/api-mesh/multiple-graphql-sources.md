---
title: Multiple GraphQL sources
description: Discover how to use several GraphQL sources to enhance your Commerce application experience.
landing-page-description: Discover how to use 2 or more sources to bring dynamic content to your Commerce application.
kt: 11813
doc-type: tutorial
audience: all
last-substantial-update: 2023-2-1

---

# Configure multiple GraphQL Sources

Stitching data across several sources provides a robust mechanism to take complex data from several data sources and return them to the front-end application. This allows the front end to display the complex data quickly and only making one request.


## Learn how to update a config

If the project has an existing json schema setup in Adobe App Builder, it is required to `update` the json. The command would be similar to this

```
aio api-mesh update some-config-name.json
```

## Who is this video for?

* Developers with multiple GraphQL sources.
* Developers new to API mesh troubleshooting errors.

## Video content

* Two sources and a single GraphQL endpoint
* Modifying the API Mesh configurations
* Schema stitching 
* Rebuild the API Mesh after fixing the schema
* Meshed schema results of two sources

>[!VIDEO](https://video.tv.adobe.com/v/3414125)

## Sample code provided in the video

Here are some of the code samples used in the video

{{$include /help/_includes/api-mesh-related-links.md}}
