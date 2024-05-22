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
exl-id: 90753b8d-eca0-4868-b40e-9563d2b0e1e8
---
# Create a downloadable product

Learn how to create a downloadable product using the REST API and the Adobe Commerce Admin. 

## Who is this video for?

- Website managers
- eCommerce merchandisers
- New Adobe Commerce developers who want to learn how to create products in Adobe Commerce using the REST API

## Video content

>[!VIDEO](https://video.tv.adobe.com/v/3425753?learn=on)

## Allowed downloadable domains

You must specify which domains are permitted to allow downloads. Domains are added to the project's `env.php` file via the command line. The `env.php` file details the domains allowed to contain downloadable content. An error occurs if a downloadable product is created using the REST API _before_  the `php.env` file is updated:

```bash
{
    "message": "Link URL's domain is not in list of downloadable_domains in env.php."
}

```

To set the domain, connect to the server: `bin/magento downloadable:domains:add www.example.com`

Once that is complete, the `env.php` is modified inside the _downloadable_domains_ array.

```php
    'downloadable_domains' => [
        'www.example.com'
    ],
```

Now that the domain is added to the `env.php`, you can create a downloadable product in the Adobe Commerce Admin or by using the REST API.

See [Configuration Reference](https://experienceleague.adobe.com/docs/commerce-operations/configuration-guide/files/config-reference-envphp.html#downloadable_domains) to learn more.

>[!IMPORTANT]
>On some versions of Adobe Commerce, you might get the following error when a product is edited in the Adobe Commerce Admin. The product is created using the REST API but the linked download has a `null` price. 

`Deprecated Functionality: number_format(): Passing null to parameter #1 ($num) of type float is deprecated in /app/vendor/magento/module-downloadable/Ui/DataProvider/Product/Form/Modifier/Data/Links.php on line 228`. 

To fix this error, use the update link API: `POST V1/products/{sku}/downloadable-links.`

See the [Update a product download link using cURL](#update-downloadable-links) section for more info.

## Create a downloadable product using cURL (download from remote server)

This example shows how to create a downloadable product using cURL when the file to download is not on the same server. This use case is typical if the file is stored in an S3 bucket or other digital asset manager.

```bash
curl --location '{{your.url.here}}/rest/default/V1/products' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{Your Bearer Token}}' \
--header 'Cookie: PHPSESSID=b78cae2338f12d846d233d4e9486607e; private_content_version=564dde2976849891583a9a649073f01' \
--data '{
  "product": {
    "sku": "POSTMAN-download-product-1",
    "name": "POSTMAN download product-1",
    "attribute_set_id": 4,
    "price": 9.9,
    "status": 1,
    "visibility": 4,
    "type_id": "downloadable",
    "extension_attributes": {
        "website_ids": [
            1
        ],
        
        "downloadable_product_links": [
            {
                "title": "My url link",
                "sort_order": 1,
                "is_shareable": 1,
                "price": 0,
                "number_of_downloads": 0,
                "link_type": "url",
                "link_url": "{{location.url.where.file.exists}}/some-file.zip",
                "sample_type": "url",
                "sample_url": "{{location.url.where.file.exists}}/sample-file.zip"
            }
        ],
        "downloadable_product_samples": []
    },
    "product_links": [],
    "options": [],
    "media_gallery_entries": [],
    "tier_prices": []
  }
}
'
```

## Create a downloadable product using cURL (download from Commerce application server) 

This example demonstrates how to use cURL to create a downloadable product from the Adobe Commerce Admin when the file is stored on the same server as the Adobe Commerce application.

In this use case, when the administrator managing the catalog chooses `upload file`, the file is transferred to the `pub/media/downloadable/files/links/` directory.  Automation creates and moves the files to their respective locations based on the following pattern:

- Each uploaded file is stored in a folder based on the first two characters of the file name.
- When the upload is initiated, the Commerce application creates or uses existing folders to transfer the file. 
- When downloading the file, the `link_file` section of the path uses the portion of the path appended to the `pub/media/downloadable/files/links/` directory.

For example, if the uploaded file is named `download-example.zip`:

- The file is uploaded to the path `pub/media/downloadable/files/links/d/o/`.
   The subdirectories `/d` and `/d/o` are created if they do not exist.

- The final path to the file is `/pub/media/downloadable/files/links/d/o/download-example.zip`. 

- The `link_url` value for this example is `d/o/download-example.zip`

```bash
curl --location '{{your.url.here}}/rest/default/V1/products' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{Your Bearer Token}}' \
--header 'Cookie: PHPSESSID=571f5ebe48857569cd56bde5d65f83a2; private_content_version=9f3286b427812be6aec0b04cae33ba35' \
--data '{
  "product": {
    "sku": "sample-local-download-file",
    "name": "A downloadable product with locally hosted download file",
    "attribute_set_id": 4,
    "price": 33,
    "status": 1,
    "visibility": 4,
    "type_id": "downloadable",
    "extension_attributes": {
        "website_ids": [
            1
        ],
        "downloadable_product_links": [
            {
                "title": "an api version of already upload file",
                "sort_order": 1,
                "is_shareable": 1,
                "price": 0,
                "number_of_downloads": 0,
                "link_type": "file",
                "link_file": "/d/o/downloadable-file-demo-file-upload.zip",
                "sample_type": null
            }
        ],
        "downloadable_product_samples": []
    },
    "product_links": [],
    "options": [],
    "media_gallery_entries": [],
    "tier_prices": []
  }
}'
```

## Get a product using curl

```bash
curl --location '{{your.url.here}}/rest/default/V1/products/POSTMAN-download-product-1' \
--header 'Authorization: Bearer {{Your Bearer Token}}' \
--header 'Cookie: PHPSESSID=b78cae2338f12d846d233d4e9486607e; private_content_version=564dde2976849891583a9a649073f01e'
```

## Update the product using Postman {#update-downloadable-links}

Use the endpoint `rest/all/V1/products/{sku}/downloadable-links`
The `SKU` is the product ID that was generated when the product was created. For example in the code sample below, it is the number 39, but make sure it is updated to use the ID from your website. This updates the links for the downloadable products. 

```json
{
  "link": {
    "id": 39,
    "title": "My swagger update",
    "sort_order": 0,
    "is_shareable": 0,
    "price": 0,
    "number_of_downloads": 0,
    "link_type": "url",
    "link_file": "{{your.url.here}}/some-file.zip",
    "link_url": "{{your.url.here}}/some-file.zip",
    "link_file_content": {
      "file_data": "{{your.url.here}}/some-file.zip",
      "extension_attributes": {}
    }
  },
  "isGlobalScopeContent": true
}
```

## Update a product download link using CURL

When you update a product download link using cURL, the URL includes the SKU for the product that is being updated.  In the following code example, the SKU is `abcd12345`. When you submit the command, change value to match the SKU for the product you want to update.

```bash
curl --location '{{your.url.here}}/rest/all/V1/products/abcd12345/downloadable-links' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{Your Bearer Token}}' \
--header 'Cookie: PHPSESSID=fa5d76f4568982adf369f758e8cb9544; private_content_version=564dde2976849891583a9a649073f01e' \
--data '{
  "link": {
    "id": {{The ID of the download link for example 39}},
    "title": "My update",
    "sort_order": 0,
    "is_shareable": 0,
    "price": 0,
    "number_of_downloads": 0,
    "link_type": "url",
    "link_file": "{{your.url.here}}/some-file.zip",
    "link_url": "{{your.url.here}}/some-file.zip",
    "link_file_content": {
      "file_data": "{{your.url.here}}/some-file.zip",
      "extension_attributes": {}
    }
  },
  "isGlobalScopeContent": true
}'
```

## Additional resources

- [Downloadable Product Type](https://experienceleague.adobe.com/docs/commerce-admin/catalog/products/types/product-create-downloadable.html){target="_blank"}
- [Downloadable Domains Configuration Guide](https://experienceleague.adobe.com/docs/commerce-operations/configuration-guide/files/config-reference-envphp.html#downloadable_domains){target="_blank"}
- [Adobe Developer REST tutorials](https://developer.adobe.com/commerce/webapi/rest/tutorials/prerequisite-tasks/){target="_blank"}
- [Adobe Commerce REST ReDoc](https://adobe-commerce.redoc.ly/2.4.6-admin/tag/products#operation/PostV1Products){target="_blank"}
