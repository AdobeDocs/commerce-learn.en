---
title: Create a downloadable product
description: Learn how to create a downloadable product using the REST API and the Adobe Commerce Admin.
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
- New Adobe Commerce developers who want to learn how to create products in Adobe Commerce using the REST API

## Video content

>[!VIDEO](https://video.tv.adobe.com/v/3425753?learn=on)

>[!IMPORTANT]
>
>You will need to add an entry to the `env.php` for the approved downloadable domains. You can read more on the env configuration file for this topic [Configuration Reference](https://experienceleague.adobe.com/docs/commerce-operations/configuration-guide/files/config-reference-envphp.html#downloadable_domains){target="_blank"}
>
>To do so you can follow the instructions on the [CLI reference for Adobe Commerce](https://experienceleague.adobe.com/docs/commerce-operations/reference/magento-open-source.html#downloadable%3Adomains%3Aadd){target="_blank"}
>
>For the product to be created and save properly, the file needs to already be available on the commerce project or wherever it is defined in the link_file. In this example FTP was used and the image was transferred to the pub/media/ folder.

## Create a downloadable product using curl

```bash
curl --location '{{your.url.here}}/rest/default/V1/products' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{Your Bearer Token}}' \
--header 'Cookie: PHPSESSID=b78cae2338f12d846d233d4e9486607e; private_content_version=564dde2976849891583a9a649073f01e' \
--data '{
  "product": {
    "sku": "postman-rest-downloadable-product-test",
    "name": "POSTMAN downloadable product test",
    "attribute_set_id": 4,
    "price": 4.5,
    "type_id": "downloadable",
    "extension_attributes": {
      "downloadable_product_links": [
        {
          "title": "My downloadable thing",
          "sort_order": 0,
          "is_shareable": 0,
          "price": 0,
          "number_of_downloads": 0,
          "link_type": "file",
          "link_file": "{{your.url.here}}/pub/media/sample.png",
          "link_file_content": {
            "file_data": "some file content data",
            "name": "My file content name string",
            "extension_attributes": {}
          }
        }
      ]
    }
  }
}
'
```

## Get a product using curl

```bash
curl --location '{{your.url.here}}/rest/default/V1/products/postman-rest-downloadable-product-test' \
--header 'Authorization: Bearer {{Your Bearer Token}}' \
--header 'Cookie: PHPSESSID=b78cae2338f12d846d233d4e9486607e; private_content_version=564dde2976849891583a9a649073f01e'
```

## Additional resources

- [Downloadable Product Type](https://experienceleague.adobe.com/docs/commerce-admin/catalog/products/types/product-create-downloadable.html){target="_blank"}
- [Downloadable Domains Configuration Guide](https://experienceleague.adobe.com/docs/commerce-operations/configuration-guide/files/config-reference-envphp.html#downloadable_domains){target="_blank"}
- [Adding to downloadable domains in .env.php](https://experienceleague.adobe.com/docs/commerce-operations/reference/magento-open-source.html#downloadable%3Adomains%3Aadd){target="_blank}
- [Adobe Developer REST tutorials](https://developer.adobe.com/commerce/webapi/rest/tutorials/prerequisite-tasks/){target="_blank"}
- [Adobe Commerce REST ReDoc](https://adobe-commerce.redoc.ly/2.4.6-admin/tag/products#operation/PostV1Products){target="_blank"}
