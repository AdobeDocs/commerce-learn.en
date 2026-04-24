---
title: Create a virtual product
description: Learn how to create a virtual product using the REST API and the Commerce Admin.
kt: 14464
doc-type: video
duration: 213
audience: all
activity: use
last-substantial-update: 2023-11-15T00:00:00.000Z
feature: Catalog Management, Admin Workspace, Backend Development, Integration, REST
topic: Commerce, Integrations, Content Management
role: Developer, User
level: Beginner
exl-id: 5149b6b4-5fbf-467a-a412-6dce7188bcb9
TQID: https://experienceleague.adobe.com/OktfC13mVgaoxyfKlZYH6HPDoCqP-m07pz5VEQ4cssM
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: c18ed297-2187-4aec-affb-9d9654eca6fc
    internal-label: Catalog management
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
---
# Create a virtual product

Learn how to create a virtual product using the REST API and the Adobe Commerce Admin. 

## Who is this video for?

* Website managers
* eCommerce merchandisers
* New Adobe Commerce developers who want to learn how to create products in Adobe Commerce using the REST API.

## Video content

>[!VIDEO](https://video.tv.adobe.com/v/3425723?learn=on)

## Create a virtual product using curl

```bash
curl --location '{{your.url.here}}/rest/default/V1/products' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{Your Bearer Token}}' \
--header 'Cookie: PHPSESSID=2cd97649bcf4ee5b45b23f8eb940e3a0; private_content_version=564dde2976849891583a9a649073f01e' \
--data '{
  "product": {
    "sku": "postman-rest-virtual-product-test",
    "name": "POSTMAN virtual product test",
    "attribute_set_id": 4,
    "price": 44,
    "type_id": "virtual"
  }
}
'
```

## Get a product using curl

```bash
curl --location '{{your.url.here}}/rest/default/V1/products/Admin-created-virtual-product' \
--header 'Authorization: Bearer {{Your Bearer Token}}' \
--header 'Cookie: PHPSESSID=2cd97649bcf4ee5b45b23f8eb940e3a0; private_content_version=564dde2976849891583a9a649073f01e'
```

## Additional resources

* [Adobe Developer REST tutorials](https://developer.adobe.com/commerce/webapi/rest/tutorials/prerequisite-tasks/){target="_blank"}
* [Adobe Commerce REST ReDoc](https://adobe-commerce.redoc.ly/2.4.6-admin/tag/products#operation/PostV1Products){target="_blank"}
