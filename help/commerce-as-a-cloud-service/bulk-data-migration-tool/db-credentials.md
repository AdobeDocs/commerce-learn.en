---
title: Bulk Data Migration Tool - DB Credentials
description: Learn how to configure the source database connection in your .my.cnf file using the Magento Cloud CLI or a project ID before running the migration tool.
role: Developer
level: Intermediate
doc-type: Technical Video
topic: Migration
feature: Data Import/Export
duration: 161
last-substantial-update: 2026-07-21
jira: KT-22105
---
# Configure database credentials for the Bulk Data Migration Tool

Set up the source database connection in your `.my.cnf` file before you run the Bulk Data Migration Tool. The steps differ depending on whether your source environment is on-premises or Adobe Commerce as a Cloud Service (PaaS).

## Who is this video for?

* Solutions Architect
* DevOps Engineer
* Backend Developer

## Video content

* Copy `.my.cnf.example` to `.my.cnf` and create a new section named for your source connection.
* Set the project ID in `.my.cnf` if your source is Adobe Commerce as a Cloud Service (PaaS).
* Use the Magento Cloud CLI tunnel commands to obtain the host, user, password, port, and database values.
* Confirm host and port connectivity before running the tool if your source is on-premises.

>[!VIDEO](https://video.tv.adobe.com/v/3496152?learn=on)
