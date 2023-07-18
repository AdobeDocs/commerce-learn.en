---
title: Learn about catalog import options that come native with Adobe Commerce
description: Learn how a few of the native options for importing your catalog to your Adobe Commerce store.
kt: 13634
doc-type: tutorial
audience: all
activity: use
last-substantial-update: 2023-7-14
feature: Backend Development, Catalogs, Data Import/Export, REST
topic: Commerce, Administration, Content Management
role: Admin, User
level: Beginner, Intermediate
---
# Learn options for importing a catalog

There are a few native methods for importing a catalog into Adobe Commerce.

- Using the admin CSV importer
- using the Bulk REST API
- Starting in Adobe Commerce 2.4.6 the CSV REST API

## Admin CSV import tool

This tool allows a store owner to import a catalog using a CSV right from the commerce admin.
Pros:

Cons:
Slow
limited to upload size on server
requires admin access and someone to perform the action, automation is limited 
Schedule imports are limited to 1x a day max

## Bulk REST API

The bulk REST API allows for automation to kick in and more frequent updates. This API is faster than using the admin upload of CSV

Pros:

Cons:

## CSV REST API

This API option allows for extremely fast imports as compared to all other native options. 

Pros:

Cons:



## Additional resources

- [Import data using new REST CSV](https://developer.adobe.com/commerce/webapi/rest/modules/import/)
- [Import data main documentation](https://experienceleague.adobe.com/docs/commerce-admin/systems/data-transfer/import/data-import.html)
- [Adobe Commerce version 2.4.6 release notes](https://experienceleague.adobe.com/docs/commerce-operations/release/notes/adobe-commerce/2-4-6.html)

