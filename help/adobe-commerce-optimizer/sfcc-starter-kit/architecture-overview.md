---
title: Salesforce Commerce Cloud Connector Architecture
description: Learn how the Salesforce Commerce Cloud Connector Starter Kit uses App Builder runtime actions and delta exports to sync catalogs with Adobe Commerce Optimizer.
feature: App Builder,Saas
topic: Administration,Commerce,Integrations
role: Developer
level: Beginner
doc-type: Technical Video
duration: 288
last-substantial-update: 2025-10-20T00:00:00.000Z
jira: KT-19014
exl-id: 1e0edcbb-5619-45c2-b06d-9133f23a634f
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: d3b92bef-63fa-5031-a925-d04d9362d616
    internal-label: Saas
  - id: cc250cf1-34eb-4863-80d0-d170d45ea067
    internal-label: Developer tools
subfeature_v2:
  - id: a743e5dc-8f37-4b5d-a848-03c32ca30598
    internal-label: App Builder
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
---
# Salesforce Commerce Cloud starter kit architecture

Learn about the architecture and functionality of the Commerce Optimizer Connector Starter Kit, which integrates Salesforce Commerce Cloud (SFCC) and Adobe App Builder. The starter kit is used by Adobe Commerce Optimizer to streamline catalog synchronization for Edge Delivery storefronts. It explains how a custom cartridge in SFCC detects catalog changes via delta export files and exposes them through custom APIs. These changes are consumed by App Builder runtime actions—both synchronous and asynchronous—to perform full and delta syncs, metadata updates, and product-specific synchronizations. The system also includes validation tools to ensure storefront accuracy and uses App Builder's state management to track sync status and prevent conflicts.

## Who is this video for?

* Commerce Solution Architect
* Technical Marketing Engineers
* eCommerce Platform Administrators

## Video content

* Custom SFCC cartridge and APIs detect catalog changes via delta exports, enabling efficient data synchronization with Adobe App Builder.
* App Builder runtime actions manage full and delta syncs, validation, and state tracking to ensure accurate and conflict-free updates to Commerce Optimizer.

>[!VIDEO](https://video.tv.adobe.com/v/3476046?learn=on)

