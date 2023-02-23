---
title: Perform a query using GraphQL
description: Learn how to perform a query using GraphQL on Adobe Commerce and [!DNL Magento Open Source]. This is an introduction to GraphQL using GET and POST calls.
landing-page-description: Learn how to perform a query using GraphQL on Adobe Commerce and [!DNL Magento Open Source]. This is an introduction to GraphQL using GET and POST calls.
kt: 11524
doc-type: tutorial
audience: all
last-substantial-update: 2022-12-13
exl-id: 443d711d-ec74-4e07-9357-fbbe0f774853
---
# GraphQL queries

Let's dive right into GraphQL query syntax with a full-fledged example. (Remember, you can try this yourself against https://venia.magento.com/graphql.)

Observe the following GraphQL query, which is broken down piece by piece:

```graphql
{
    country (
        id: "US"
    ) {
        id
        full_name_english
    }

    categories(
        filters: {
            name: {
                match: "Tops"
            }
        }
    ) {
        items {
            name
            products(
                pageSize: 10,
                currentPage: 2
            ) {
                items {
                    sku
                }
            }
        }
    }
}
```

A plausible response from a GraphQL server for the above query could be: 

```json
{
  "data": {
    "country": {
      "id": "US",
      "full_name_english": "United States"
    },
    "categories": {
      "items": [
        {
          "name": "Tops",
          "products": {
            "items": [
              {
                "sku": "VSW06"
              },
              {
                "sku": "VT06"
              },
              {
                "sku": "VSW07"
              },
              {
                "sku": "VT07"
              },
              {
                "sku": "VSW08"
              },
              {
                "sku": "VT08"
              },
              {
                "sku": "VSW09"
              },
              {
                "sku": "VT09"
              },
              {
                "sku": "VSW10"
              },
              {
                "sku": "VT10"
              }
            ]
          }
        }
      ]
    }
  }
}
```

The above example relies on the out-of-the-box GraphQL schema for Magento, defined at the server. In this request, you
query multiple types of data at once. The query expresses exactly the fields you want, and the returned data is formatted
similarly to the query itself.

>[!NOTE]
>
>GraphQL clients obfuscate the form of the actual HTTP request being sent, but this is easy to discover. If you're using a browser-based client, observe the [!UICONTROL Network] tab when a query is sent. You see that the request contains a raw body consisting of "query: `{string}`", where `{string}` is simply the raw string of your entire query. If the request is being sent as a GET, the query might be encoded in the query string parameter "query" instead. Unlike with REST, the HTTP request type doesn't matter, only the contents of the query.


## Querying for what you want

`country` and `categories` in the example represent two different "queries," for two different kinds of data. Unlike a traditional API paradigm like REST, which would define separate and explicit endpoints for each data type, GraphQL gives you the flexibility to query a single endpoint with an expression that can fetch many types of data at once.

Likewise, the query specifies exactly the fields that are desired for both `country` (`id` and `full_name_english`) and `categories` (`items`, which itself has a sub-selection of fields), and the data you receive back mirrors that field specification. There are presumably many more fields available for these data types, but you get back only what you requested.


>[!NOTE]
>
>You may notice that the return value for `items` is actually an _array_ of values, but you are nevertheless directly selecting sub-fields for it. When a field's type is a list, GraphQL implicitly understands sub-selections to apply to each item in the list.

## Arguments

While the fields you want returned are specified within the braces of each type, named arguments and values for them are specified within parentheses after the type name. Arguments are often optional and often affect the way query results are filtered, formatted, or otherwise transformed. 

You are passing an `id` argument to `country`, specifying the particular country we want to query, and a `filters` argument for `categories`.

## Fields all the way down

While you might tend to think of `country` and `categories` as separate queries or entities, the entire tree expressed in your query actually consists of nothing but fields. The expression of `products` is syntactically no different from that of `categories`. Both are fields, and there is no difference between their construction.

Any GraphQL data graph has a single "root" type (typically referred to `Query`) to start the tree, and the types often considered to be entities are simply assigned to fields on this root. Our example query is actually making one generic query for the root type and selecting the fields `country` and `categories`. It is then selecting sub-fields of those fields, and so on, potentially several levels deep. Wherever the return type of a field is a complex type (for example, one with its own fields, rather than a scalar type), continue to select the fields you want.

This concept of nested fields is also why you can pass arguments for `products` (`pageSize` and `currentPage`) in the same way you did for the top level `categories` field.

![GraphQL Field Tree](../assets/graphql-field-tree.png)

## Variables

Let's try a different query:

```graphql
query getProducts(
    $search: String
) {
    products(
        search: $search
    ) {
        items {
            ...productDetails
            related_products {
                ...productDetails
            }
        }
    }
}

fragment productDetails on ProductInterface {
    sku
    name
}
```

The first thing to note is the added the keyword `query` before the opening brace of the query, along with an operation name (`getProducts`). This operation name is arbitrary; it doesn't correspond to anything in the server schema. This syntax was added to support the introduction of variables.

In the previous query, you hard-coded values for the arguments of your fields directly, as strings or integers. The GraphQL specification, however, has first-class support for separating user input from the main query using variables.

In the new query, you are using parentheses before the opening brace of the entire query to define a `$search` variable (variables always use the dollar sign prefix syntax), and it is this variable that is being provided to the `search` argument for `products`.

When a query contains variables, the GraphQL request is expected to include a separate JSON-encoded dictionary of values alongside the query itself. For the query above, you might send the following JSON of variable values in addition to the query body:

```json
{
    "search": "VT01"
}
```

>[!NOTE]
>
>If you're trying out these queries against the Venia example site rather than your own Magento instance, you likely will not get back any results for `related_products`.

In any GraphQL-aware client that you are using for testing (such as Altair and GraphiQL), the UI supports entering the variables JSON separately from the query.

Just as you saw that the actual HTTP request for a GraphQL query contains "query: `{string}`" in its body, any request containing a variables dictionary simply includes an additional "variables: `{json}`" in that same body, where `{json}` is the JSON string with the variable values.

The new query also uses a _fragment_ (`productDetails`) to reuse the same field selection in multiple places. [Read more about fragments](https://graphql.org/learn/queries/#fragments) in the GraphQL documentation.

{{$include /help/_includes/graphql-rest-related-links.md}}
