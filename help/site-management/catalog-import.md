---
title: Learn about catalog import options that come native with Adobe Commerce
description: Learn how a few of the native options for importing your catalog to your Adobe Commerce store.
kt: 13634
doc-type: tutorial
audience: all
activity: use
last-substantial-update: 2023-8-15
feature: Backend Development, Data Import/Export, REST
topic: Commerce, Administration, Content Management
role: Admin, User
level: Beginner, Intermediate

---
# Options for importing a catalog

There are a few native methods for importing a catalog into Adobe Commerce. Each method has its own reasoning for usage along with pros and cons that must be considered. 

Choose from one of the options below to learn more.

>[!BEGINTABS]

>[!TAB Manual]

## Creating the products manually {#manual-import}

If you have a limited catalog and updates are infrequent, creating them manually might be the best option. It requires time to enter each product and some limited training to how to use the Commerce Admin. Manual catalog management is not the right option for most stores, but in certain situations, it may make sense. To see additional documentation for this process, visit [Create a product](https://experienceleague.adobe.com/docs/commerce-admin/catalog/products/product-create.html){target="_blank"}. Do not forget, you can use more than one method to manage your catalog, however once automation is used, manual edits must be limited. Automated updates have the opportunity to overwrite any changes performed manually, and therefore cause confusion. Once the integration with Adobe Commerce to manage the catalog is using automation and APIs, it is advised to restrict management of the catalog from the admin through [user roles and permissions](https://experienceleague.adobe.com/docs/commerce-admin/systems/user-accounts/permissions-user-roles.html){target="_blank"}. 



### When to consider this approach

- Very small catalog, for example fewer than 50 products
- Updates are infrequent 
- You have all the product details, images, videos, and you do not want to take the time to learn how to convert the data to CSV
- You want to include adding images and videos when creating the products
- Your team is `not` familiar with APIs and how OAUTH works



>[!TAB Admin CSV]

## Admin CSV import tool {#admin-csv}

This tool allows a store owner to import a catalog using a CSV right from the commerce admin. 
[Import Data from Commerce Admin](https://experienceleague.adobe.com/docs/commerce-admin/systems/data-transfer/import/data-import.html){target="_blank"}

Pros:
Uploading a CSV from the admin is a straight forward approach to catalog management. It allows for faster catalog product updates to a moderately sized catalog. 

Cons:

- Slow
- Maximum upload file sized defined on server and may not be easily adjusted by a store owner.
- Requires admin access and someone to perform the action, automation is limited 
- Schedule imports are limited to 1x a day max
- The images and videos associated must be uploaded separately



### When to consider this approach

- Catalog size is moderate 
- Updates are not more than once a day
- you have some access to server configurations in case that you must increase max file upload size
- Your team is `not` familiar with APIs and how OAUTH works



>[!TAB Bulk REST API]

## Bulk REST API {#bulk-rest-api}

The bulk REST API allows for automation and more frequent updates. This API is faster than using the admin upload of CSV.
[Bulk endpoints documentation](https://developer.adobe.com/commerce/webapi/rest/use-rest/bulk-endpoints/){target="_blank"}

Pros:
The ability to import large data sets that are not in CSV format.

Cons:

- The images and videos associated must be uploaded separately
- Can be limited by bandwidth constraints on the hosting provider
- You are required to use option attribute IDs not the labels



### When to consider this approach

- Catalog is any size
- Updates are frequent, more than 1x a day is acceptable
- Time to import is important but not 
- The data is not structured in CSV format and you are not capable of transforming it using automation



>[!TAB ASYNC REST API]

## ASYNC REST API {#async-rest-api}

An asynchronous web endpoint intercepts messages to a Web API and writes them to the message queue. Each time the system accepts such an API request, it generates a UUID identifier. Adobe Commerce includes this UUID when it adds the message to the queue. Then, a consumer reads the messages from the queue and executes them one-by-one.
[Asynchronous web endpoints documentation](https://developer.adobe.com/commerce/webapi/rest/use-rest/asynchronous-web-endpoints/){target="_blank"}

Pros:

- Fast to import data
- Store scope is supported or you can specify `all` to perform operation on all existing stores

Cons:

- GET request are not supported
- You are required to use the option attribute IDs, instead of the labels


### When to consider this approach

- Imports are frequent
- No issue with a small delay from the time they are submitted via API and then processed from the message queue.



>[!TAB CSV REST API]

## CSV REST API {#csv-rest-api}

This API option allows for extremely fast imports as compared to all other native options. 

[Import data REST CSV api](https://developer.adobe.com/commerce/webapi/rest/modules/import/){target="_blank"}
Pros:

- Fastest method to process the incoming data
- Can be performed multiple times per day
- Data can be compressed using gzip for large requests to avoid HTTP request size limits.

Cons:

- The images and videos associated must be uploaded separately
- You are required to use the option attribute IDs not the labels
- Data is needs to be in a CSV format

### When to consider this approach

- Catalog is any size
- Updates are frequent, more than 1x a day is acceptable
- Overall time to import is important
- The data is already in CSV format or can easily be transformed using automation



>[!ENDTABS]

## Additional resources

- [Import data using new REST CSV](https://developer.adobe.com/commerce/webapi/rest/modules/import/){target="_blank"}
- [Import data main documentation](https://experienceleague.adobe.com/docs/commerce-admin/systems/data-transfer/import/data-import.html){target="_blank"}
- [Adobe Commerce version 2.4.6 release notes](https://experienceleague.adobe.com/docs/commerce-operations/release/notes/adobe-commerce/2-4-6.html){target="_blank"}
- [Users, roles, and permissions](../site-management/users-roles-permissions.md){target="_blank"}
