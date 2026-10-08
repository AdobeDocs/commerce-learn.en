---
title: Bulk Data Migration Tool - DB Credentials
description: Learn how to configure the source database connection in your .my.cnf file using the Magento Cloud CLI or a project ID before running the migration tool.
role: Developer
level: Intermediate
doc-type: Technical Video
topic: Migration
feature: Data Import/Export
duration: 161
last-substantial-update: 2026-07-21T00:00:00.000Z
jira: KT-22105
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: 601e4abe-d9bf-58de-a779-32ed6794dcbe
    internal-label: Data Import/Export
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
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
