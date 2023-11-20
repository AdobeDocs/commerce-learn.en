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

## Allowed downloadable domains

This is unique to downloadable products. For Adobe Commerce to allow for downloads, it is required to specify what domains are permitted. For this reason, the domains are added to the projects' `env.php`. This is accomplished by using a command line to specify the domain that is allowed to be a linkable source for the downloadable content. If you try to create a downloadable product using the REST API before this is done, an error is returned:

```bash
{
    "message": "Link URL's domain is not in list of downloadable_domains in env.php."
}

```

To set the domain, connect to the server using terminal. The command is similar to this: `bin/magento downloadable:domains:add www.example.com`

Once that is complete, the `env.php` is modified inside the downloadable_domains array and look similar to this section

```php
    'downloadable_domains' => [
        'www.example.com'
    ],
```

Now that the domain is added to the `env.php` you can create a downloadable product in the Adobe Commerce Admin or using a REST API.

To learn more about this topic, review the Experience League page dedicated to this topic [Configuration Reference](https://experienceleague.adobe.com/docs/commerce-operations/configuration-guide/files/config-reference-envphp.html#downloadable_domains){target="_blank"} as even more details can be found at [CLI reference for Adobe Commerce](https://experienceleague.adobe.com/docs/commerce-operations/reference/magento-open-source.html#downloadable%3Adomains%3Aadd){target="_blank"}

>[!IMPORTANT]
>Depending on your version of Adobe Commerce, there have been reports of an error when trying to edit the product in the Adobe Commerce Admin. Using the REST API it creates the product, but the linked download has a price of `null`. When you use the Adobe Commerce Admin to edit the product, an error message is shown: `Deprecated Functionality: number_format(): Passing null to parameter #1 ($num) of type float is deprecated in /app/vendor/magento/module-downloadable/Ui/DataProvider/Product/Form/Modifier/Data/Links.php on line 228`. The easiest fix is to use the update link API - POST V1/products/{sku}/downloadable-links. The code example is described [Update a product download link using CURL](#update-downloadable-links).

## Create a downloadable product using curl with a URL and a remote location for the download

This example shows how to create a downloadable product with the URL for the download that is NOT on the same server. This is typical if the file is in an S3 bucket or other digital asset manager.

```bash
curl --location '{{your.url.here}}/rest/default/V1/products' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{Your Bearer Token}}' \
--header 'Cookie: PHPSESSID=b78cae2338f12d846d233d4e9486607e; private_content_version=564dde2976849891583a9a649073f01e' \
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

## Create a downloadable product using curl with a URL and the location for the download is on this server

For this example, the intent is to mimic that process if the product would be created from the Adobe Commerce Admin. In this use case, when the administrator managing the catalog chooses `upload file`, the expectation is the file resides on the same server as the Adobe Commerce application. When this happens, the file is uploaded to `pub/media/downloadable/files/links/`. Inside this directory, using the first two characters of the file name, the application creates or uses existing folders. For Example, if the uploaded file is named `download-example.zip`. If the folder `pub/media/downloadable/files/links/d/` does not exist, it is created. If the folder `pub/media/downloadable/files/links/d/o/` does not exist, it is created  The Adobe Commerce Application transfers the file inside the directory `pub/media/downloadable/files/links/d/o/` to have the path `/pub/media/downloadable/files/links/d/o/download-example.zip`. It is important to understand this process and recognize the pattern. When establishing an integration to the Adobe Commerce application, the automation can create and move the files to their respective locations. It is also an important point to realize that the file path of the uploaded file in the product configuration is the information found after `/pub/media/downloadable/files/links/`. This is what will be used in the link_url section of the json. In this example, it is `/d/o/downloadable-file-demo-file-upload.zip`.

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
The id is the ID that was generated when the product was created. For example in the code sample below, it is the number 39, but make sure it is updated to use the ID from your website. This updates the links for the downloadable products. 

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

Part of the URL is the sku that is being updated, in this example it is `abcd12345`. This needs to be changed to match the product SKU you want to update.

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
- [Adding to downloadable domains in .env.php](https://experienceleague.adobe.com/docs/commerce-operations/reference/magento-open-source.html#downloadable%3Adomains%3Aadd){target="_blank}
- [Adobe Developer REST tutorials](https://developer.adobe.com/commerce/webapi/rest/tutorials/prerequisite-tasks/){target="_blank"}
- [Adobe Commerce REST ReDoc](https://adobe-commerce.redoc.ly/2.4.6-admin/tag/products#operation/PostV1Products){target="_blank"}
