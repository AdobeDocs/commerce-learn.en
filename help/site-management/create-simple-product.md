---
title: Create a simple product
description: Learn how to create a simple product using the REST API and the Commerce Admin.
kt: 14446
doc-type: video
audience: all
activity: use
last-substantial-update: 2023-11-14
feature: Catalog Management, Admin Workspace, Backend Development, Integration, REST
topic: Commerce, Integrations, Content Management
role: Developer, User
level: Beginner
exl-id: 62ba8e71-dcff-4c72-8850-029be2c42620
---
# Create a simple product

Learn how to create a simple product using the REST API and the Adobe Commerce Admin. 

## Who is this video for?

- Website managers
- eCommerce merchandisers
- New Adobe Commerce developers who want to learn how to create products in Adobe Commerce using the REST API.

## Video content

>[!VIDEO](https://video.tv.adobe.com/v/3425650?learn=on)

## Create a product using curl

```bash
curl --location '{{your.url.here}}/rest/default/V1/products' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{Your Bearer Token}}' \
--header 'Cookie: PHPSESSID=a42da0096288718c9556f77549c6305f; private_content_version=564dde2976849891583a9a649073f01e' \
--data '{
  "product": {
    "sku": "some-product-sku",
    "name": "My curl created product test",
    "attribute_set_id": 4,
    "price": 222,
    "type_id": "simple"
  }
}
```

## Get a product using curl

```bash
curl --location '{{your.url.here}}rest/default/V1/products/some-product-sku' \
--header 'Authorization: Bearer {{Your Bearer Token}}' \
--header 'Cookie: private_content_version=3b797a6cc3c5c71f2193109fb9838b12'
```

## Additional resources

- [Adobe Developer REST tutorials](https://developer.adobe.com/commerce/webapi/rest/tutorials/prerequisite-tasks/){target="_blank"}
- [Adobe Commerce REST ReDoc](https://adobe-commerce.redoc.ly/2.4.6-admin/tag/products#operation/PostV1Products){target="_blank"}
