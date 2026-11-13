---
title: Native catalog import options in Adobe Commerce
description: Learn how a few of the native options for importing your catalog to your Adobe Commerce store.
jira: KT-13634
doc-type: Tutorial
duration: 211
audience: all
activity: use
last-substantial-update: 2023-08-15
feature: Backend Development, Data Import/Export, REST
topic: Commerce, Administration, Content Management
role: Admin, User
level: Beginner, Intermediate
exl-id: 18713a44-df39-4b94-91ce-c7efeb4ce2b3
TQID: 'https://experienceleague.adobe.com/-JG7blrxImSXjA2DP9soZfsicISW0hkP2zJeWdMpVBU'
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: bd989d82-1e15-4534-88db-f1f51dd77ffa
    internal-label: Accounts
  - id: c18ed297-2187-4aec-affb-9d9654eca6fc
    internal-label: Catalog management
  - id: dac87252-6066-4d6e-a9d2-f6d84c323de7
    internal-label: Configuration
  - id: b48dbafb-4193-5648-b9d9-bf96e9c9a411
    internal-label: Backend Development
  - id: 601e4abe-d9bf-58de-a779-32ed6794dcbe
    internal-label: Data Import/Export
  - id: c4f010fa-1478-4300-a88d-706fbc036a7a
    internal-label: APIs and SDKs
subfeature_v2:
  - id: e0ca0e7a-9738-48d1-b98b-615468ab4aaf
    internal-label: REST API
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
topic_v2:
  - id: eddd9b14-83bd-4ff4-9072-54a4a484abb7
    internal-label: Administration
---
# Options for importing a catalog

There are a few native methods for importing a catalog into Adobe Commerce. Each method has its own reasoning for usage along with pros and cons that must be considered. 

Choose from one of the options below to learn more.

>[!BEGINTABS]

>[!TAB Manual]

## Creating the products manually {#manual-import}

Consider manual product creation for a small catalog with infrequent updates. Entering each product takes time and requires basic training on the Commerce Admin. Manual catalog management suits specific situations rather than most stores. For instructions, see [Create a product](https://experienceleague.adobe.com/en/docs/commerce-admin/catalog/products/product-create){target="_blank"}. If you combine catalog management methods, limit manual edits once you introduce automation. Automated updates risk overwriting manual changes and causing confusion. When an integration manages the catalog through automation and APIs, restrict catalog management in the Admin through [user roles and permissions](https://experienceleague.adobe.com/en/docs/commerce-admin/systems/user-accounts/permissions-user-roles){target="_blank"}.

### When to consider this approach

* Very small catalog, fewer than 50 products
* Updates are infrequent 
* You have all the product details, images, videos, and you do not want to take the time to learn how to convert the data to CSV
* You want to include adding images and videos when creating the products
* Your team is `not` familiar with APIs and how OAUTH works

>[!TAB Admin CSV]

## Admin CSV import tool {#admin-csv}

This tool allows a store owner to import a catalog using a CSV right from the commerce admin. 
[Import Data from Commerce Admin](https://experienceleague.adobe.com/en/docs/commerce-admin/systems/data-transfer/import/data-import){target="_blank"}

Pros:
Uploading a CSV from the admin is a straight forward approach to catalog management. It allows for faster catalog product updates to a moderately sized catalog. 

Cons:

* Slow
* The server defines the maximum upload file size, and store owners do not always have an easy way to adjust it.
* Requires admin access and someone to perform the action, automation is limited 
* Schedule imports are limited to 1x a day max
* The images and videos associated must be uploaded separately

### When to consider this approach

* Catalog size is moderate 
* Updates are not more than once a day
* You have access to server configuration if you need to increase the maximum upload file size
* Your team is `not` familiar with APIs and how OAUTH works

>[!TAB Bulk REST API]

## Bulk REST API {#bulk-rest-api}

The bulk REST API allows for automation and more frequent updates. This API is faster than using the admin upload of CSV.
[Bulk endpoints documentation](https://developer.adobe.com/commerce/webapi/rest/use-rest/bulk-endpoints){target="_blank"}

Pros:
The ability to import large data sets that are not in CSV format.

Cons:

* The images and videos associated must be uploaded separately
* Bandwidth constraints at the hosting provider limit import throughput

### When to consider this approach

* Catalog is any size
* Updates are frequent, more than 1x a day is acceptable
* Time to import is important but not critical and a short delay in processing the import data is acceptable
* The data is not structured in CSV format and you are not capable of transforming it using automation

>[!TAB ASYNC REST API]

## ASYNC REST API {#async-rest-api}

An asynchronous web endpoint intercepts messages to a Web API and writes them to the message queue. Each time the system accepts such an API request, it generates a UUID identifier. Adobe Commerce includes this UUID when it adds the message to the queue. Then, a consumer reads the messages from the queue and executes them one-by-one.
[Asynchronous web endpoints documentation](https://developer.adobe.com/commerce/webapi/rest/use-rest/asynchronous-web-endpoints){target="_blank"}

Pros:

* Fast to import data
* Store scope is supported or you can specify `all` to perform operation on all existing stores

Cons:

* GET requests are not supported

### When to consider this approach

* Imports are frequent
* No issue with a small delay from the time they are submitted via API and then processed from the message queue.


>[!TAB CSV REST API]

## CSV REST API {#csv-rest-api}

This API imports data faster than the other native options.

[Import data REST CSV api](https://developer.adobe.com/commerce/webapi/rest/modules/import/){target="_blank"}
Pros:

* Fastest method to process the incoming data
* Can be performed multiple times per day
* Data can be compressed using gzip for large requests to avoid HTTP request size limits.

Cons:

* The images and videos associated must be uploaded separately
* Data needs to be in CSV format

### When to consider this approach

* Catalog is any size
* Updates are frequent, more than 1x a day is acceptable
* Overall time to import is important
* The data is already in CSV format or can easily be transformed using automation

>[!ENDTABS]

## Additional resources

* [Import data using new REST CSV](https://developer.adobe.com/commerce/webapi/rest/modules/import/){target="_blank"}
* [Import data main documentation](https://experienceleague.adobe.com/en/docs/commerce-admin/systems/data-transfer/import/data-import){target="_blank"}
* [Adobe Commerce version 2.4.6 release notes](https://experienceleague.adobe.com/en/docs/commerce-operations/release/notes/adobe-commerce/2-4-6){target="_blank"}
* [Users, roles, and permissions](../store-administration/users-roles-permissions.md){target="_blank"}
