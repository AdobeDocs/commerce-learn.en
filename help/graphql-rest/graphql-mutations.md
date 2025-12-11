---
title: Perform a mutation using GraphQL
description: Get an introduction about performing a mutation using GraphQL on Adobe Commerce and [!DNL Magento Open Source]. Perform your first mutation using POST calls.
landing-page-description: Get an introduction about performing a mutation using GraphQL on Adobe Commerce and [!DNL Magento Open Source]. Perform your first mutation using POST calls.
short-description: Get an introduction about performing a mutation using GraphQL on Adobe Commerce and [!DNL Magento Open Source]. Perform your first mutation using POST calls.
kt: 13938
doc-type: video
audience: all
last-substantial-update: 2023-10-12
feature: GraphQL
topic: Commerce, Architecture, Headless
old-role: Architect, Developer
role: Developer
level: Beginner, Intermediate
exl-id: 6b82ffda-925f-4a81-8ca5-49a2b8ab4929
---
# Mutations

This is part 3 of the series for GraphQL and Adobe Commerce. Mutations are the ability to save, update, and return values using GraphQL.


>[!VIDEO](https://video.tv.adobe.com/v/3424121?learn=on)

## Related videos and tutorials on GraphQL in this series

* [Part 1 GraphQL - Introduction](../graphql-rest/intro-graphql.md)
* [Part 2 GraphQL - Queries](../graphql-rest/graphql-queries.md)
* [Part 4 GraphQL - Schema](../graphql-rest/graphql-schema.md) 

## Example mutation

Any complete API specification needs to offer the ability not only to query data, but also to create and update it. 

REST distinguishes between requests that change data and those that do not with the request type or "verb" (GET vs. POST or PUT).
When using GraphQL, data-modifying queries are distinguished by the `mutation` keyword that corresponds with a different 
root type in the schema defined at the server.

Look at this example mutation for adding a product to a user's cart. (This requires a cart ID that was generated
for the logged-in customer's session or using the `createEmptyCart` mutation.)

```graphql
mutation doAddToCart(
    $cartId: String!,
    $cartItems: [CartItemInput!]!
) {
    addProductsToCart(
        cartId: $cartId
        cartItems: $cartItems
    ) {
        cart {
            total_quantity
            prices {
                grand_total {
                    value
                }
            }
        }
    }
}
```

You can imagine the above mutation being sent in a request along with the following variables dictionary:

```json
{
  "cartId": "{cart-id}",
  "cartItems": [
    {
      "quantity": 1,
      "sku": "VT01-RN-XS"
    }
  ]
}
```

And finally, you might receive a response like this:

```json
{
  "data": {
    "addProductsToCart": {
      "cart": {
        "total_quantity": 1,
        "prices": {
          "grand_total": {
            "value": 35.2
          }
        }
      }
    }
  }
}
```

The chief thing to note that about the above example is that, apart from the use of the `mutation` keyword instead of `query`,
the syntax is identical to a query. Like queries, the mutation includes:

* An arbitrary operation name (`doAddToCart`)
* A list of variables (for example, `$cartId`)
* An initial field (`addProductsToCart`) with arguments (for example, `cartId`, set to the value of `$cartId`) in parentheses
* A subselection of fields in braces

The fields subselection allows you to flexibly define the fields you would like returned (from the type assigned as the
return value of `addProductsToCart` - `AddProductsToCartOutput`) after the mutation is completed. 

As explained previously, fields defined in a GraphQL schema start on a root type for queries (typically referred to as a `Query`). Similarly,
another root type exists for mutations (typically referred to as `Mutation`). `addProductsToCart` is a field
on that root type.

A few other notes about the above example:

*   The `!` character suffixing `String` and `CartItemInput` indicates that the variable is required.
*   The square brackets (`[]`) around the `CartItemInput` type specified for `$cartItems` indicate a list
  of that type rather than a single value.

{{$include /help/_includes/graphql-rest-related-links.md}}
