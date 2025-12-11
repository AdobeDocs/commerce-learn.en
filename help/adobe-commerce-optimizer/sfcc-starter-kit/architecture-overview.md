---
title: Architecture Overview for the Salesforce Commerce Cloud Connector
description: Lean about the architecture for the Salesforce Commerce Cloud with Adobe Commerce Optimizer.
feature: App Builder,Saas
topic: Administration,Commerce,Integrations
old-role: Architect, Developer
role: Developer
level: Beginner
doc-type: Technical Video
duration: 243
last-substantial-update: 2025-10-20
jira: KT-19014
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
