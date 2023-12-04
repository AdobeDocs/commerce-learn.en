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


A grouped product consists of simple standalone products that are presented as a group. You can offer variations of a single product or group them by season or theme. Before creating a grouped product, verify that all the simple products to include in the group are available in Adobe Commerce, and create any that do not exist. In this tutoria you will learn how to create a grouped product using the REST API and the Adobe Commerce Admin.

Use the REST API to create a group product in the Admin:
1. Create an empty grouped product.
1. Create simple products to use in the grouped product.
1. Populate the empty grouped product with simple products. 
1. Create an empty grouped product and associate the simple products.

When creating grouped products in the Adobe Commerce Admin, It is recommended tha sitmple products are created first. When you are ready to create the grouped product, associate the simple products by assigning them to the grouped product in one batch.

The sort order attribute in the payload is required and is used by the frontend for displaying the associated products in a desired order.

## Who is this video for?

- Website managers
- eCommerce merchandisers
- New Adobe Commerce developers who want to learn how to create grouped products in Adobe Commerce using the REST API.

## Video content

>[!VIDEO](https://video.tv.adobe.com/v/3425920?learn=on)

## Setup for the grouped product

In this example, there are three simple products (created first) and a grouped product. Two simple products are associated with the grouped product, and then the third simple product is added to the grouped product.

## Create the first simple product using cURL

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

## Create the second simple product using cURL

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

## Create the third simple product using cURL

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

## Create an empty grouped product using cURL

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

Include the appropriate position number (anything except `1` or `2`), which are used for the first two products originally associated tothe grouped product. For this example, the position is `4`.

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

To [delete a simple product](https://developer.adobe.com/commerce/webapi/rest/tutorials/grouped-product/) from a grouped product, use: `DELETE /V1/products/{sku}/links/{type}/{linkedProductSku}`.

To discover what to use as `{type}`, use xdebug to capture the request and evaluate the $linkTypes: `related`, `crosssell`, `uupsell`, and `associated`.
![Grouped Product link types - alt text](/help/assets/site-management/catalog/grouped-types.png "Grouped product link types captured during xdebug session")

When linking the simple products to the grouped product, the payload contained a few sections similar to:

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

In the payload, the `link_type` value `associated` provides the `{type}` value required in the DELETE request. The request URL will be similar to `/V1/products/my-new-grouped-product/links/associated/product-sku-three`.

See the cURL request to delete the simple product with the `product-sku-three` SKU from the grouped product with the 'my-new-grouped-product` SKU:

```bash
curl --location --request DELETE '{{your.url.here}}rest/default/V1/products/my-new-grouped-product/links/associated/product-sku-three' \
--header 'Authorization: Bearer {{Your Bearer Token}}' \
--header 'Cookie: PHPSESSID=9e61396705e9c17423eca2bdf2deefb2'
```

## Get a grouped product using cURL

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
