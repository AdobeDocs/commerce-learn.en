---
title: Create a downloadable product
description: Learn how to create a downloadable product using the REST API and the Commerce Admin.
kt: 14464
doc-type: video
audience: all
activity: use
last-substantial-update: 2023-11-16
feature: Catalog Management, Admin Workspace, Backend Development, Integration, REST
topic: Commerce, Integrations, Content Management
role: Developer, User
level: Beginner

---
# Create a downloadable product

Learn how to create a downloadable product using the REST API and the Adobe Commerce Admin. 

## Who is this video for?

- Website managers
- eCommerce merchandisers
- New Adobe Commerce developers who want to learn how to create products in Adobe Commerce using the REST API.

## Video content

>[!VIDEO](https://video.tv.adobe.com/v/3425753?learn=on)

>[!IMPORTANT]
>
>You will need to add an entry to the `env.php` for the approved downloadable domains. You can read more on the env configuration file for this topic [Configuration Reference](https://experienceleague.adobe.com/docs/commerce-operations/configuration-guide/files/config-reference-envphp.html#downloadable_domains){target="_blank"}
>
>To do so you can follow the instructions on the [CLI reference for Adobe Commerce](https://experienceleague.adobe.com/docs/commerce-operations/reference/magento-open-source.html#downloadable%3Adomains%3Aadd){target="_blank"}

## Create a downloadable product using curl

```bash
curl --location '{{your.url.here}}/rest/default/V1/products' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{Your Bearer Token}}' \
--header 'Cookie: PHPSESSID=e7768803d6b2428d2ab0f5ea2abbb38e; private_content_version=564dde2976849891583a9a649073f01e' \
--data '{
  "product": {
    "sku": "postman-rest-virtual-product-test",
    "name": "POSTMAN virtual product test",
    "attribute_set_id": 4,
    "price": 44,
    "type_id": "downloadable"
  }
}
'
```

## Get a product using curl

```bash
curl --location '{{your.url.here}}/rest/default/V1/products/postman-rest-virtual-product-test' \
--header 'Authorization: Bearer {{Your Bearer Token}}' \
--header 'Cookie: PHPSESSID=e7768803d6b2428d2ab0f5ea2abbb38e; private_content_version=564dde2976849891583a9a649073f01e'
```

## Additional resources

- [Downloadable Product Type](https://experienceleague.adobe.com/docs/commerce-admin/catalog/products/types/product-create-downloadable.html){target="_blank"}
- [Downloadable Domains Configuration Guide](https://experienceleague.adobe.com/docs/commerce-operations/configuration-guide/files/config-reference-envphp.html#downloadable_domains){target="_blank"}
- [Adding to downloadable domains in .env.php](https://experienceleague.adobe.com/docs/commerce-operations/reference/magento-open-source.html#downloadable%3Adomains%3Aadd){target="_blank}
- [Adobe Developer REST tutorials](https://developer.adobe.com/commerce/webapi/rest/tutorials/prerequisite-tasks/){target="_blank"}
- [Adobe Commerce REST ReDoc](https://adobe-commerce.redoc.ly/2.4.6-admin/tag/products#operation/PostV1Products){target="_blank"}
