---
title: Create a simple product
description: Learn how to create a simple product using the REST API and the Commerce admin.
kt: 14446
doc-type: video
audience: all
activity: use
last-substantial-update: 2023-11-13
feature: Catalog Management, Admin Workspace, Backend Development, Integration, REST
topic: Commerce, Integrations, Content Management
role: Developer, User
level: Beginner

---
# Create a simple product

Learn how to create a simple product using the REST API and the commerce admin. 

## Who is this video for?

- Website managers
- eCommerce merchandisers
- New developers to Adobe Commerce who are needing to learn how to use REST to create a product in Adobe Commerce

## Video content

>[!VIDEO](https://video.tv.adobe.com/v/3425650?learn=on)

## Curl code sample to create a product

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

## Curl code sample to get a product

```bash
curl --location '{{your.url.here}}rest/default/V1/products/some-product-sku' \
--header 'Authorization: Bearer {{Your Bearer Token}}' \
--header 'Cookie: private_content_version=3b797a6cc3c5c71f2193109fb9838b12'
```

## Additional resources

- [Adobe Developer REST tutorials](https://developer.adobe.com/commerce/webapi/rest/tutorials/prerequisite-tasks/){target="_blank"}
- [Adobe Commerce REST ReDoc](https://adobe-commerce.redoc.ly/2.4.6-admin/tag/products#operation/PostV1Products){target="_blank"}
