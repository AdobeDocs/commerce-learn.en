---
title: Create a configurable product
description: Learn how to create a configurable product using the REST API and the Commerce Admin.
kt: 14586
doc-type: video
audience: all
activity: use
last-substantial-update: 2023-12-15
feature: Catalog Management, Admin Workspace, Backend Development, Integration, REST
topic: Commerce, Integrations, Content Management
role: Developer, User
level: Beginner
exl-id: 112bec9a-0f8e-4252-8c52-f486a5e663b5
---
# Create a configurable product

A configurable product is a parent product of multiple simple products. Define a configurable product to require the buyer to make one or more choices to select a specific product variation. For example, if the product is a shirt, the buyer must choose the size and color options to select the shirt.

Although a configurable product uses more SKUs and may initially take a little longer to set up, it can save you time in the end. If you plan to grow your business, the configurable product type is a good choice for products with multiple options.

Before creating a configurable product, verify that all the simple products to include in the configurable product are available in Adobe Commerce. Create any that do not exist.

In this tutorial, learn how to create a configurable product using the REST API and the Adobe Commerce Admin.

Use the REST API to create a configurable product:

1. Get the attributes for an [attribute set](https://experienceleague.adobe.com/docs/commerce-admin/catalog/product-attributes/create/attribute-sets.html) to use the ID numbers for subsequent API calls.
1. Create simple products for use in the configurable product.
1. Create an empty configurable product and associate the simple products.
1. Set the product attributes for the configurable product.
1. Populate the empty configurable product with simple products. 
1. Get the configurable product and all the attributes.
1. Get the assigned children products for the configurable product.
1. Delete the association of simple products to configurable products.

When creating configurable products from the Adobe Commerce Admin, you can either create the simple products first, or use the automated tool that creates new simple products for use using the wizard. 

## Who is this video for?

- Website managers
- eCommerce merchandisers
- New Adobe Commerce developers who want to learn how to create configurable products in Adobe Commerce using the REST API

## Video content

>[!VIDEO](https://video.tv.adobe.com/v/3426381?learn=on)

## Get the color attributes using cURL

In this example, the entire attribute set with all the individual attributes is returned for attribute set 10. It can be long, hundreds of lines are not uncommon. When reviewing the response, the attribute ID for color will likely be in the middle. Expedite the search for these values by using grep or other methods to search the results. My response was near line 665 and is included in the following snippet from the JSON response.

```json
...
{
        "attribute_id": 93,
        "attribute_code": "color",
        "frontend_input": "select",
        "entity_type_id": "4",
        "is_required": false,
        "options": [
            {
                "label": " ",
                "value": ""
            },
            {
                "label": "Red",
                "value": "13"
            },
            {
                "label": "Blue",
                "value": "14"
            },
            {
                "label": "Green",
                "value": "15"
            }
        ],
...
```


To retrieve the attribute IDs to set up your configurable product, update the `attribute-sets/10/attributes` portion of the following cURL request to replace `10` with the attribute set ID in your environment. This request uses the GET method.

```bash
curl --location '{{your.url.here}}rest/V1/products/attribute-sets/10/attributes' \
--header 'Authorization: Bearer {{Your Bearer Token}}'
```

## Create the first simple product using cURL

### Adjust environment IDs and product details

Create the first simple product by using the API to send the following POST request using cURL.

Before submitting the request, update the example with values for your environment.

- Change `"attribute-set": 10` to replace `10` with the attribute set ID from your environment.
- Change `"value": "13"` to replace `13` with the value from your environment.

```bash
curl --location '{{your.url.here}}/rest/default/V1/products' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{Your Bearer Token}}' \
--header 'Cookie: PHPSESSID=aff63a1634f6f1a773e7a4894bf1a55c' \
--data '{
  "product": {
    "sku": "Kids-Hawaiian-Ukulele-red",
    "name": "Kids Hawaiian Ukulele Red",
    "attribute_set_id": 10,
    "price": 12.50,
    "status": 1,
    "visibility": 1,
    "type_id": "simple",
    "weight": "0.5",
    "extension_attributes": {
        "stock_item": {
            "qty": "10",
            "is_in_stock": true
        }
    },
    "custom_attributes": [
        {
            "attribute_code": "color",
            "value": "13"
        }
    ]
  }
}
'
```

## Create the second simple product using cURL

Create the second simple product by using the API to send the following POST request using cURL.

Before submitting the request, update the example with values for your environment.

- Change `"attribute_set_id": 10,` and replace `10` with the attribute set id from in your environment.
- Change `"value": "14"` and replace `14` with the value from your environment.

```bash
curl --location '{{your.url.here}}/rest/default/V1/products' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{Your Bearer Token}}' \
--header 'Cookie: PHPSESSID=aff63a1634f6f1a773e7a4894bf1a55c' \
--data '{
  "product": {
    "sku": "Kids-Hawaiian-Ukulele-Blue",
    "name": "Kids Hawaiian Ukulele Blue",
    "attribute_set_id": 10,
    "price": 15,
    "status": 1,
    "visibility": 1,
    "type_id": "simple",
    "weight": "0.5",
    "extension_attributes": {
        "stock_item": {
            "qty": "20",
            "is_in_stock": true
        }
    },
    "custom_attributes": [
        {
            "attribute_code": "color",
            "value": "14"
        }
    ]
  }
}
'
```

## Create the third simple product using cURL

Create the third simple product by sending the following POST request using cURL.

Before submitting the request, update the example with values for your environment.

- Change `"attribute_set_id": 10,` to replace `10` with the attribute set ID from your environment.
- Change `"value": "15"` and replace `15` with the value from your environment.

```bash
curl --location '{{your.url.here}}/rest/default/V1/products' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{Your Bearer Token}}' \
--header 'Cookie: PHPSESSID=aff63a1634f6f1a773e7a4894bf1a55c' \
--data '{
  "product": {
    "sku": "Kids-Hawaiian-Ukulele-Green",
    "name": "Kids Hawaiian Ukulele Green",
    "attribute_set_id": 10,
    "price": 25,
    "status": 1,
    "visibility": 1,
    "type_id": "simple",
    "weight": "0.5",
    "extension_attributes": {
        "stock_item": {
            "qty": "30",
            "is_in_stock": true
        }
    },
    "custom_attributes": [
        {
            "attribute_code": "color",
            "value": "15"
        }
    ]
  }
}
'
```

## Create an empty configurable product using cURL

Create an empty configurable product by sending the following POST request using cURL.

Before submitting the request, update the example with values for your environment.

- Change `"attribute_set_id": 10,` and replace `10` with the attribute set id from your environment.
- Change `"value": "93"` and replace `93` with the value from your environment.

```bash
curl --location '{{your.url.here}}/rest/default/V1/products' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{Your Bearer Token}}' \
--header 'Cookie: PHPSESSID=aff63a1634f6f1a773e7a4894bf1a55c' \
--data '{
  "product": {
    "sku": "Kids-Hawaiian-Ukulele",
    "name": "Kids Hawaiian Ukulele",
    "attribute_set_id": 10,
    "status": 1,
    "visibility": 4,
    "type_id": "configurable",
    "weight": "0.5",
    "custom_attributes": [
        {
            "attribute_code": "color",
            "value": "93"
        }
    ]
  }
}'
```

## Set the options available for the configurable product

Set the options available for the configurable product by sending the following POST request using cURL.

Before submitting the request, change `"attribute_id": 93,` to replace `93` with the attribute id from your environment.

```bash
curl --location '{{your.url.here}}/rest/default/V1/configurable-products/Kids-Hawaiian-Ukulele/options' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{Your Bearer Token}}' \
--header 'Cookie: PHPSESSID=aff63a1634f6f1a773e7a4894bf1a55c' \
--data '{
  "option": {
    "attribute_id": "93",
    "label": "Color",
    "position": 0,
    "is_use_default": true,
    "values": [
      {
        "value_index": 9
      }
    ]
  }
}'
```

If you forget to set the options for the configurable product (parent), you get an error when you try to associate a child product to the configurable product. The error message is similar to the following example:

`{"message":"The parent product doesn't have configurable product options.","trace":"#0 [internal function]: Magento\\ConfigurableProduct\\Model\\LinkManagement->addChild('Kids-Hawaiian-U...'}`

## Link the child product to the configurable

Now, you have created three simple products:

- `"Kids Hawaiian Ukulele Red"`,
- `"Kids-Hawaiian-Ukulele-Blue"`
- `"Kids-Hawaiian-Ukulele-Green"`

Add these simple products as children of the configurable product by sending the following POST request. Submit a separate request for each product.

For each request, update the `childSKU` value with the value for the child product you are adding. The following example assigns the simple product `kids-Hawaiian-Ukulele-red` to the configurable product with the SKU `Kids-Hawaiian-Ukulele-red`.


```bash
curl --location '{{your.url.here}}rest/default/V1/configurable-products/Kids-Hawaiian-Ukulele/child' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{Your Bearer Token}}' \
--header 'Cookie: PHPSESSID=aff63a1634f6f1a773e7a4894bf1a55c' \
--data '{
  "childSku": "Kids-Hawaiian-Ukulele-red"
}
'
```

## Get a configurable product using cURL

Now that you have created a configurable product with three assigned child SKUs. You can see the linked IDs for the assigned products by sending the following GET request using cURL. This request returns detailed information about the configurable product.

```json
...
        "configurable_product_links": [
            155,
            157,
            156
        ]
...
```

The following uses the GET method

```bash
curl --location '{{your.url.here}}/rest/default/V1/products/Kids-Hawaiian-Ukulele' \
--header 'Authorization: Bearer {{Your Bearer Token}}'
```

## Get the children product associated to a configurable product

Return only the children associated with the configurable product by sending the following GET request. The response will include all the attributes for the child product including SKU and price.

The following uses the GET method

```bash
curl --location '{{your.url.here}}/rest/default/V1/configurable-products/kids-hawaiian-ukulele/children' \
--header 'Authorization: Bearer {{Your Bearer Token}}'
```

## Delete or remove a child product from the parent configurable

You can remove a child product from a configurable product without deleting the product from the catalog by sending the following DELETE request using cURL.

```bash
curl --location --request DELETE '{{your.url.here}}/rest/default/V1/configurable-products/Kids-Hawaiian-Ukulele/children/Kids-Hawaiian-Ukulele-Blue' \
--header 'Authorization: Bearer {{Your Bearer Token}}'
```

## Additional resources

- [Create a configurable product tutorial](https://developer.adobe.com/commerce/webapi/rest/tutorials/configurable-product/){target="_blank"}
- [Configurable Product](https://experienceleague.adobe.com/docs/commerce-admin/catalog/products/types/product-create-configurable.html){target="_blank"}
- [Adobe Developer REST tutorials](https://developer.adobe.com/commerce/webapi/rest/tutorials/prerequisite-tasks/){target="_blank"}
- [Adobe Commerce REST ReDoc](https://adobe-commerce.redoc.ly/2.4.6-admin/tag/products#operation/PostV1Products){target="_blank"}
