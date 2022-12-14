---
title: Learn about the schema involved with GraphQL
description: This is an introduction to GraphQL and we are describing the schema. Some interesting patterns and ways to read the schema are provided
landing-page-description: This is an introduction to GraphQL.  Understanding the schema and how to interpret some of the elements 
kt: 11524
doc-type: tutorial
audience: all
last-substantial-update: 2022-12-13
---

# Schema Language

The queries and mutations we've worked with rely on a specific data graph being implemented at the server, which the GraphQL runtime
consumes and uses to resolve the query. The GraphQL specification defines an agnostic language for expressing the types
and relationships of your data graph.

Let's look at an abbreviated type schema that would support the queries and mutations we've looked at so far:

```graphql
input FilterMatchTypeInput {
  match: String
}

type Money {
  value: Float
}

type Country {
  id: String
  full_name_english: String
}

interface ProductInterface {
  sku: String
  name: String
  related_products: [ProductInterface]
}

type CategoryFilterInput {
  name: FilterMatchTypeInput
}

type CategoryProducts {
  items: [ProductInterface]
}

type CategoryTree {
  name: String
  products(pageSize: Int, currentPage: Int): CategoryProducts
}

type CategoryResult {
  items: [CategoryTree]
}

type Products {
  items: [ProductInterface]
}

type Query {
  country (id: String): Country
  categories (filters: CategoryFilterInput): CategoryResult
  products (search: String): Products
}

input CartItemInput {
  sku: String!
  quantity: Float!
}

type CartPrices {
  grand_total: Money
}

type Cart {
  prices: CartPrices
  total_quantity: Float!
}

type AddProductsToCartOutput {
  cart: Cart!
}

type Mutation {
  addProductsToCart(cartId: String!, cartItems: [CartItemInput!]!): AddProductsToCartOutput
}
```

You can delve into [the GraphQL documentation](https://graphql.org/learn/schema/) to learn about the details of the 
type system, including syntax for some concepts not represented here. The above example, however, is likely fairly self-explanatory.
(And a major detail to note is how similar the syntax is to query syntax!) Defining a GraphQL schema is simply a matter
of expressing the available arguments and fields of a given type, along with the types of those fields. Each complex field
type must itself have a definition, and so on through the tree until we get to simple scalar types like `String`.

The `input` declaration is in all respects like a `type` but defines a type that can be used as input for an argument.
Also note the `interface` declaration. This serves a function more or less the same as interfaces in PHP; other types will
inherit from this interface.

The syntax `[CartItemInput!]!` looks tricky but is fairly intuitive in the end. The `!` _inside_ the bracket declares that every
value in the array must be non-null, while the one _outside_ declares that the array value itself must be non-null (e.g., an empty array).

> The logic for how data is fetched and formatted according to a schema, and how such logic is mapped to particular types,
> is up to the GraphQL runtime implementation. Any implementation, however, follows a conceptual flow that should make sense
> in light of our understanding of nested fields: A "resolve" operation associated with the root `Query` or `Mutation` type
> is performed, which examines each field specified in the request. For each field that resolves to a complex type, a similar
> "resolve" is done for that type, and so on until everything has resolved into scalar values.

>[!NOTE]
>
>[Return to Getting Started GraphQL](./getting-started-graphql.md)
