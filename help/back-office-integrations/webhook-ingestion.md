---
title: Configure, Deploy, and Customize an Ingestion Webhook
description: Learn how to configure, deploy, and customize an ingestion webhook to connect Adobe Commerce with a third-party back office system and handle event translation.
doc-type: Technical Video
duration: 697
last-substantial-update: 2024-07-30
feature: Best Practices, Backend Development, Integration
topic: Architecture, Commerce, Development
role: Developer
level: Intermediate
jira: KT-15870
exl-id: f2654873-256e-4c1b-abed-8bfbc4db3fbb
TQID: https://experienceleague.adobe.com/nUXdrsjzeD939jOjZS8ywPV3OeOaxpZCmeuveACtYrY
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: ba9e5be9-7de1-4f71-a5d2-baead0e425ee
    internal-label: Security
  - id: dac87252-6066-4d6e-a9d2-f6d84c323de7
    internal-label: Configuration
  - id: e8818fe6-9c8b-4bc0-9ef8-377a10b7bc75
    internal-label: Architecture
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: b5ce8718-c3af-4fdb-a1a9-fca32f83a87c
    internal-label: Implementation
  - id: d095671a-1355-40aa-8b5f-06c33c68080b
    internal-label: Security
---
# Configure, deploy, and customize an ingestion webhook

Learn about the setup and customization of an ingestion webhook for integrating Commerce with a third-party back office system.​ This video explains how the webhook can address limitations in event communication between systems by providing a publicly available endpoint to adapt messages from the third party system to the Adobe IO Eventing API. The process involves configuring the webhook in the `actions.config.yaml` file, enabling it in the `app.config.yaml` file, and deploying it to ensure proper functionality. 

The video covers the steps to modify the webhook code to translate third-party events into formats compatible with the integration's subscribed event types. It discusses adding an `event-mapping.json` file to facilitate this translation and emphasizes the importance of redeploying the runtime action after making changes.​ The video also highlights the significance of validating and transforming incoming event payloads to align with the expected schema, ensuring successful processing and integration with the Commerce API for creating customers.

## Audience 

* Developers who want to set up an ingestion webhook
* Anyone who wants to customize code for event translation
* Developers and architects who want to understand the importance of authentication and payload management

## Video Content

* Configuration and Deployment: The video emphasizes the importance of configuring the ingestion webhook in the `actions.config.yaml` file and enabling it in the `app.config.yaml` file. It also highlights the need to redeploy the project after making changes to ensure the webhook functions correctly.
* Customization for Compatibility: It is crucial to customize the webhook code to translate third-party events into formats that align with the integration's subscribed event types. ​ This customization ensures seamless communication between systems and successful event processing.
* Authentication Implementation: Businesses are responsible for implementing authentication mechanisms suitable for their needs to prevent unauthorized requests when using the ingestion webhook. This step is essential for maintaining the security and integrity of the integration.
* Payload Validation and Transformation: Validating and transforming incoming event payloads to match the expected schema is vital for successful processing and integration with the Commerce API. ​ By trimming and mapping fields appropriately, the integration can operate efficiently with the necessary data.

>[!VIDEO](https://video.tv.adobe.com/v/3431694?learn=on)

{{$include /help/_includes/starter-kit-related-links.md}}

## Code Samples

* [Custom ingestion webhook](https://github.com/adobe/adobe-commerce-samples/tree/main/starter-kit/customize-ingestion-webhook)
* [Add ingestion scheduler](https://github.com/adobe/adobe-commerce-samples/tree/main/starter-kit/add-ingestion-scheduler)
