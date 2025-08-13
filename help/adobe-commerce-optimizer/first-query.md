---
title: How to query data
description: Learn how to query data for an Adobe Commerce Optimizer instance.
feature: Saas, Storefront
topic: Commerce
role: Developer
level: Beginner
doc-type: Tutorial
duration: 182
last-substantial-update: 2025-08-13
jira: KT-18548
exl-id: bad3d926-2952-4bac-b685-adb16f009f8d
---
# Query data Adobe Commerce Optimizer

Learn how to query data using GraphQL on an Adobe Commerce Optimizer instance. 

## Who is this video for?

* Commerce Solution Architect and developers

## Video content

* Query data using GraphQL
* Using jq to make json easier to read

>[!VIDEO](https://video.tv.adobe.com/v/3470800?learn=on&enablevpops)

## Code Samples

Be sure to exchange values like`{{insert-your-graphql-endpoint-url}}`, `{{insert-your-ac-source-locale}}` and `{{your-search-query-string}}` with the values needed on your query. 

Basic sample query

```bash
curl '{{insert-your-graphql-endpoint-url}}' \
-H 'Content-Type: application/json' \
-H 'AC-Source-Locale: {{insert-your-ac-source-locale}}' \
-d '{"query": "query ProductSearch($search: String!) { productSearch( phrase: $search, page_size: 10, current_page: 2) { items { productView { sku name description shortDescription images { url } ... on SimpleProductView { attributes { label name value } price { regular { amount { value currency } } roles } } } } } }", "variables": { "search": "{{your-search-query-string}}"}}'
```

Basic sample query using `jq` to pretty-print the output

```bash
curl '{{insert-your-graphql-endpoint-url}}' \
-H 'Content-Type: application/json' \
-H 'AC-Source-Locale: {{insert-your-ac-source-locale}}' \
-d '{"query": "query ProductSearch($search: String!) { productSearch( phrase: $search, page_size: 10, current_page: 2) { items { productView { sku name description shortDescription images { url } ... on SimpleProductView { attributes { label name value } price { regular { amount { value currency } } roles } } } } } }", "variables": { "search": "{{your-search-query-string}}"}}' | jq .
```

## Related Content

* [Getting started with Merchandising API](https://developer.adobe.com/commerce/services/optimizer/merchandising-services/using-the-api/#make-your-first-request){target="_blank"}
* [[!DNL Adobe Commerce Optimizer] Guide](https://experienceleague.adobe.com/en/docs/commerce/optimizer/overview){target="_blank"}
