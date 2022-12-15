---
title: Learn how to perform a mutation using GraphQL on Adobe Commerce and Magento Open Source
description: This is an introduction to GraphQL. We are doing a mutation using POST calls for Adobe Commerce and Magento Open source
landing-page-description: This is an introduction to GraphQL. This section we show you how to perform your first mutation to an Adobe Commerce and Magento Open Source project.
kt: 11524
doc-type: tutorial
audience: all
last-substantial-update: 2022-12-13
---
# Mutations

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

We could imagine the above mutation being sent in a request along with the following variables dictionary:

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

And finally, we might receive a response like this:

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
the syntax is identical to a query! Just like queries, the mutation includes:

* An arbitrary operation name (`doAddToCart`)
* A list of variables (e.g., `$cartId`)
* An initial field (`addProductsToCart`) with arguments (e.g., `cartId`, set to the value of `$cartId`) in parentheses
* A sub-selection of fields in braces

The fields sub-selection allows you to flexibly define the fields you would like returned (from the type assigned as the
return value of `addProductsToCart` - `AddProductsToCartOutput`) after the mutation is completed. 

We've noted how fields defined in a GraphQL schema start on a root type for queries (typically referred to as a `Query`). Similarly,
another root type exists for mutations (typically referred to, unsurprisingly, `Mutation`). `addProductsToCart` is a field
on that root type.

A few other notes about the above example:

* The `!` character suffixing `String` and `CartItemInput` indicates that the variable is required.
* The square brackets (`[]`) around the `CartItemInput` type specified for `$cartItems` indicate a list
  of that type rather than a single value.
