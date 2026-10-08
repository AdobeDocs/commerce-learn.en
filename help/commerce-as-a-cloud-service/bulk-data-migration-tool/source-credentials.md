---
title: Bulk Data Migration Tool - Source Credentials
description: Learn how to configure the source instance URL and authentication credentials in your .env file before running the Bulk Data Migration Tool.
role: Developer
level: Intermediate
doc-type: Technical Video
topic: Migration
feature: Data Import/Export
duration: 238
last-substantial-update: 2026-07-21T00:00:00.000Z
jira: KT-22095
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
# Configure source credentials for the Bulk Data Migration Tool

Set the source instance URL and authentication credentials in your `.env` file before you run the Bulk Data Migration Tool. The authentication steps differ slightly depending on whether your source environment is on-premises or Adobe Commerce as a Cloud Service (PaaS).

## Who is this video for?

* Solutions Architect
* DevOps Engineer
* Backend Developer

## Video content

* Set the source instance URL and the REST and GraphQL URLs in the `.env` file.
* Retrieve or create integration keys from **System** > **Extensions** > **Integrations** in the Adobe Commerce Admin.
* To generate the four required tokens, activate the integration.
* Retrieve the Magento CLI token from account.magento.cloud if your source is Adobe Commerce as a Cloud Service (PaaS).

>[!VIDEO](https://video.tv.adobe.com/v/3496142?learn=on)
