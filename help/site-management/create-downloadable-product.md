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

## Create a downloadable product using curl with a file that exists on the website

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

## Create a downloadable product that has a url for the download link

```json
{
  "product": {
    "sku": "admin created url downloadable product - 8",
    "name": "admin created url downloadable product - 8",
    "attribute_set_id": 4,
    "price": 5.58,
    "status": 1,
    "visibility": 4,
    "type_id": "downloadable",
    "extension_attributes": {
        "downloadable_product_links": [
            {
                "title": "My admin created downloadable url - 8",
                "sort_order": 1,
                "is_shareable": 1,
                "price": 0,
                "number_of_downloads": 0,
                "link_type": "url",
                "link_url": "{{your.url.here}}/russell.jpg",
                "sample_type": null
            }
        ]
    }
  }
}
```

## Get a product using curl

```bash
curl --location '{{your.url.here}}/rest/default/V1/products/postman-rest-downloadable-product-test' \
--header 'Authorization: Bearer {{Your Bearer Token}}' \
--header 'Cookie: PHPSESSID=b78cae2338f12d846d233d4e9486607e; private_content_version=564dde2976849891583a9a649073f01e'
```

## Update the product using Postman {#update-downloadable-links}

Use the endpoint `rest/all/V1/products/{sku}/downloadable-links`

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
"link_url": "https://app.dx.test/some-file.zip",
    "link_file_content": {
      "file_data": "{{your.url.here}}/some-file.zip",
      "extension_attributes": {}
    }
  },
  "isGlobalScopeContent": true
}
```

## Update a product download link using CURL

```bash
curl --location '{{your.url.here}}/rest/all/V1/products/My-admin-download-product-4/downloadable-links' \
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
