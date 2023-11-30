---
title: Create a grouped product
description: Learn how to create a grouped product using the REST API and the Commerce Admin.
kt: 14585
doc-type: video
audience: all
activity: use
last-substantial-update: 2023-11-30
feature: Catalog Management, Admin Workspace, Backend Development, Integration, REST
topic: Commerce, Integrations, Content Management
role: Developer, User
level: Beginner

---
# Create a grouped product

Learn how to create a grouped product using the REST API and the Adobe Commerce Admin. When using REST API for this process, first an empty grouped product is created, then populate the empty grouped product with simple products. So a key thing to remember is, the simple products must be created before being used. Typically this means all the simple products are created first, then a configurable product is created. Once the empty grouped product is created, associate the simple products. 

When creating grouped products in the Adobe Commerce Admin, it is advisable to have the simple products created first. When you are ready to create the grouped product, the association of the simple products can be done at the same time. Unlike the REST api, where this is a two-step process, from the Commerce Admin the grouped product can be created and the simple products assigned at one time.

One other unique item with grouped products is the simple products have a position to help with the frontend experience. This position provides the sort order for the simple products. In conjunction, the frontend uses these values when organizing the product detail page for this grouped product.

## Who is this video for?

- Website managers
- eCommerce merchandisers
- New Adobe Commerce developers who want to learn how to create grouped products in Adobe Commerce using the REST API.

## Video content

>[!VIDEO](https://video.tv.adobe.com/v/3425650?learn=on)

## Setup for the grouped product

In this example, there will be three simple products and a grouped product. The simple products are created first. Next, the grouped product is created. Finally, two simple products are associated to the grouped product. The final task adds the third simple product to the grouped product.

## Create the first simple product using curl

```bash
curl --location '{{your.url.here}}/rest/default/V1/products' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{Your Bearer Token}}' \
--header 'Cookie: PHPSESSID=a42da0096288718c9556f77549c6305f; private_content_version=564dde2976849891583a9a649073f01e' \
--data '{
  "product": {
    "sku": "product-sku-one",
    "name": "Simple product one",
    "attribute_set_id": 4,
    "price": 1.11,
    "type_id": "simple"
  }
}
```

## Create the second simple product using curl

```bash
curl --location '{{your.url.here}}/rest/default/V1/products' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{Your Bearer Token}}' \
--header 'Cookie: PHPSESSID=a42da0096288718c9556f77549c6305f; private_content_version=564dde2976849891583a9a649073f01e' \
--data '{
  "product": {
    "sku": "product-sku-two",
    "name": "Simple Product two",
    "attribute_set_id": 4,
    "price": 2.22,
    "type_id": "simple"
  }
}
```

## Create the third simple product using curl

```bash
curl --location '{{your.url.here}}/rest/default/V1/products' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{Your Bearer Token}}' \
--header 'Cookie: PHPSESSID=a42da0096288718c9556f77549c6305f; private_content_version=564dde2976849891583a9a649073f01e' \
--data '{
  "product": {
    "sku": "product-sku-three",
    "name": "Simple product three",
    "attribute_set_id": 4,
    "price": 3.33,
    "type_id": "simple"
  }
}
```

## Create an empty grouped product using curl

```bash
curl --location '{{your.url.here}}/rest/default/V1/products' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{Your Bearer Token}}' \
--header 'Cookie: PHPSESSID=28a020734488eef2600f8d5c7f302b53; private_content_version=564dde2976849891583a9a649073f01e' \
--data '{
    "product":{
        "sku":"my-new-grouped-product",
        "name":"This is my New Grouped Product",
        "attribute_set_id":4,
        "type_id":"grouped",
        "visibility":4
    }
}
'
```

## Add the first and second simple products to the grouped product

```bash
curl --location '{{your.url.here}}/rest/default/V1/products/my-new-grouped-product/links' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{Your Bearer Token}}' \
--header 'Cookie: PHPSESSID=28a020734488eef2600f8d5c7f302b53; private_content_version=564dde2976849891583a9a649073f01e' \
--data '{
    "items":[
        {
            "sku":"my-new-grouped-product",
            "link_type":"associated",
            "linked_product_sku":"product-sku-one",
            "linked_product_type":"simple",
            "position":1,
            "extension_attributes":{
            "qty":1
            }
        },
        {
            "sku":"my-new-grouped-product",
            "link_type":"associated",
            "linked_product_sku":"product-sku-two",
            "linked_product_type":"simple",
            "position":2,
            "extension_attributes":{
            "qty":1
            }
        }
    ]
}
'
```

## Add the third simple product to the existing grouped product

Do not forget to have the appropriate position number, for this it can be anything except `1` or `2`. Those were used with the first two products that were originally associated to this grouped product. For this example, it is position `4`.

```bash
curl --location --request PUT '{{your.url.here}}/rest/default/V1/products/my-new-grouped-product/links' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{Your Bearer Token}}' \
--header 'Cookie: PHPSESSID=9e61396705e9c17423eca2bdf2deefb2' \
--data '{
    "entity":{
        "sku":"my-new-grouped-product",
        "link_type":"associated",
        "linked_product_sku":"product-sku-three",
        "linked_product_type":"simple",
        "position":4,
        "extension_attributes":{
            "qty":1
        }
    }
}

'
```

## Delete a simple product from a grouped product

According to the [Adobe Developer documentation](https://developer.adobe.com/commerce/webapi/rest/tutorials/grouped-product/), to delete you are to use this pattern: `DELETE /V1/products/{sku}/links/{type}/{linkedProductSku}`

However, it may not be clear what to use for {type}. Using xdebug, it is possible capture the request and evaluate the $linkTypes. When evaluating the options, there is four: `related`, `crosssell`, `uupsell`, and `associated`. See the image below:
![Grouped Product link types - alt text](/help/assets/site-management/catalog/grouped-types.png "Grouped product link types captured during xdebug session")

If you recall what was used in linking the simple products to the grouped product, the payload contained a few sections similar to one below

```bash
        {
            "sku":"my-new-grouped-product",
            "link_type":"associated",
            "linked_product_sku":"product-sku-two",
            "linked_product_type":"simple",
            "position":2,
            "extension_attributes":{
            "qty":1
            }
        }

```

The third line it contains `"link_type":"associated",`. This word `associated` is needed in the DELETE request for {type}. This means that the URL would be similar to `/V1/products/my-new-grouped-product/links/associated/product-sku-three`.

Here is the curl request to delete the simple product with the sku `product-sku-three` from the grouped product with the sku `my-new-grouped-product`.

```bash
curl --location --request DELETE '{{your.url.here}}rest/default/V1/products/my-new-grouped-product/links/associated/product-sku-three' \
--header 'Authorization: Bearer {{Your Bearer Token}}' \
--header 'Cookie: PHPSESSID=9e61396705e9c17423eca2bdf2deefb2'
```

## Get a grouped product using curl

```bash
curl --location '{{your.url.here}}rest/default/V1/products/some-grouped-product-sku' \
--header 'Authorization: Bearer {{Your Bearer Token}}' \
--header 'Cookie: private_content_version=3b797a6cc3c5c71f2193109fb9838b12'
```

## Additional resources

- [Create and manage grouped products](https://developer.adobe.com/commerce/webapi/rest/tutorials/grouped-product/){target="_blank"}
- [Grouped Product](https://experienceleague.adobe.com/docs/commerce-admin/catalog/products/types/product-create-grouped.html){target="_blank"}
- [Adobe Developer REST tutorials](https://developer.adobe.com/commerce/webapi/rest/tutorials/prerequisite-tasks/){target="_blank"}
- [Adobe Commerce REST ReDoc](https://adobe-commerce.redoc.ly/2.4.6-admin/tag/products#operation/PostV1Products){target="_blank"}
