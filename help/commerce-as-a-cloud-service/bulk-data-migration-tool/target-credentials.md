---
title: Bulk Data Migration Tool - Target Credentials
description: Learn how to configure the target instance URLs, Adobe IMS credentials, and CDMS settings in your .env file before running the Bulk Data Migration Tool.
role: Developer
level: Intermediate
doc-type: Technical Video
topic: Migration
feature: Data Import/Export
duration: 226
last-substantial-update: 2026-07-21
jira: KT-22107
---
# Configure target credentials for the Bulk Data Migration Tool

Set the target instance URLs, Adobe IMS credentials, and CDMS settings in your `.env` file before you run the Bulk Data Migration Tool. Make sure your Adobe IMS URL, target URL, and CDMS host all match the same environment tier — stage or production.

## Who is this video for?

* Solutions Architect
* DevOps Engineer
* Backend Developer

## Video content

* Set the target instance REST and GraphQL URLs and target tenant ID in the `.env` file, using values from the instance info panel on experience.adobe.com.
* Set the Adobe IMS URL to match your environment tier (stage or production) and region.
* Retrieve the Adobe IMS client ID and client secret from **Project** > **OAuth Server-to-Server** in the Adobe Developer Console.
* Copy the target org ID and configure the CDMS host, port, and local server settings to match your environment.

>[!VIDEO](https://video.tv.adobe.com/v/3496167?learn=on)
