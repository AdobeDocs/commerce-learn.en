---
title: GraphQL introduction
description: Learn how to use GraphQL on Adobe Commerce and [!DNL Magento Open Source]. Use GraphQL GET and POST calls for Adobe Commerce and [!DNL Magento Open Source].
landing-page-description: Learn how to use GraphQL on Adobe Commerce and [!DNL Magento Open Source]. Use GraphQL GET and POST calls for Adobe Commerce and [!DNL Magento Open Source].
kt: 11524
doc-type: tutorial
audience: all
last-substantial-update: 2022-12-13
---
# GraphQL introduction

GraphQL has quickly become the industry standard for how powerful client-side applications talk to a backend. It's an increasingly relevant topic for Adobe Commerce developers, as the platform continues to expand its capabilities in the realm of headless implementations.

If you're new to GraphQL, this section orients you to the basic concepts and usage.

## What is GraphQL?

GraphQL is a specification for a unique API query language and the runtime that provides data in response to that query language.

Traditional web APIs like REST have served well for disparate systems passing data back and forth, but have provided less than peak performance for modern app-link experiences like Progressive Web Applications. In applications like this, the front-end and back-end layers of the _same_ application communicate via web API. The regimented approach of schemes like REST often does not provide the appropriate flexibility in this context, where many kinds of data need to be fetched quickly.

GraphQL allows a client to expressively describe _exactly_ the data it needs. Instead of requiring multiple network requests for fetching multiple data types, a single request can query for many types. And, responses are kept lean by including (in a format intuitively mirroring the query) only the types and fields that are asked for.

The runtime that implements the GraphQL specification can be built in any language. Adobe Commerce and [!DNL Magento Open Source] use the
[graphql-php](https://webonyx.github.io/graphql-php/) PHP implementation and builds its own layers on top of it.

[View the full GraphQL documentation](https://graphql.org/learn)

## Using a GraphQL client

You need a GUI GraphQL client to test out code samples and tutorials. There are several options:

* [Altair](https://altairgraphql.dev/) is an excellent and fully featured client built specifically for GraphQL. Adobe uses Altair in walk-through videos.
* If you don't want to install the desktop application, there are also Altair extensions that run right in your
  [Chrome](https://chrome.google.com/webstore/detail/altair-graphql-client/flnheeellpciglgpaodhkhmapeljopja), Firefox, or [Edge](https://microsoftedge.microsoft.com/addons/detail/altair-graphql-client/kpggioiimijgcalmnfnalgglgooonopa) browser.
* [GraphiQL](https://github.com/graphql/graphiql/tree/main/packages/graphiql) is an implementation of the GraphQL IDE from the GraphQL Foundation. This is not an installable tool, but rather a package you can use to build the interface yourself.
* If you're already familiar with [Postman](https://www.postman.com/), it has decent support for GraphQL queries, though it's not as fully featured as a dedicated GraphQL client.

In your GraphQL client, you should submit your requests to the URL path `/graphql` on your Adobe Commerce or [!DNL Magento Open Source] instance. If you'd prefer to use an existing instance for your tests, you can use the demo of the Venia theme (the example implementation of PWA Studio): `https://venia.magento.com/graphql`

