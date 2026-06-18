---
title: Last-mile integration in the Commerce starter kit
description: Learn about last-mile integration in Commerce using extensibility hooks for validation, transformation, preprocessing, sending, and post-processing.
doc-type: Technical Video
duration: 557
last-substantial-update: 2024-07-30
feature: Best Practices, Backend Development, Integration
topic: Architecture, Commerce, Development
role: Developer
level: Intermediate
jira: KT-15869
exl-id: e86e8c7b-d5d2-484d-90a2-9c5309c7ea1d
TQID: https://experienceleague.adobe.com/TCR23A98L8XrVDEQeqLQoOXKQPBQu-Wb7YnGUkBXgak
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: c1256247-af4b-46d8-9dca-0c654ecfa157
    internal-label: Order Management System
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
---
# Last mile integration using the Adobe Starter Kit  

Learn about items to consider when starting the last-mile integration with Adobe Commerce, focusing on extensibility hooks to enhance connectivity with third-party systems. This video outlines a structured approach where various hooks such as validation, transformation, preprocessing, sending, and post-processing ensure seamless data flow and system synchronization. Each hook serves a distinct purpose, including:

* Validating incoming data against schemas
* Transforming data objects between systems
* Performing calculations before sending relevant information
* Sending the data to the destination system

It is important to maintain separate JavaScript files for each block to uphold business logic integrity and facilitate future framework upgrades, ensuring a robust and adaptable integration setup.

Learn about the significance of post-processing activities through the post process hook, which enables users to perform additional actions after data synchronization, such as adding comments to orders or storing external IDs. The video includes best practices like encapsulating API requests within specific libraries to streamline connections with third-party systems. You will also learn typical use cases for each hook and guidance on handling different scenarios.

## Audience 

* Developers who want to learn the structure and functionality of extensibility hooks, and how these hooks can enhance connectivity with third-party systems.
* Developers who want to learn typical use cases and best practices associated with each extensibility hook, such as validation, transformation, preprocessing, sending, and post-processing, to facilitate seamless data flow, system synchronization, and efficient integration setup maintenance. ​
  
## Video Content

* Learn about the structure of the invoked actions in last-mile integration.
* Understand typical use cases within the validation hook, including validating incoming data against schemas and skipping specific events based on certain criteria. ​
* Learn the role of the transform hook in transforming data objects between the origin and destination systems.
* Learn about the significance of the send hook in facilitating the actual data send to the destination system.

>[!VIDEO](https://video.tv.adobe.com/v/3431692?learn=on)

{{$include /help/_includes/starter-kit-related-links.md}}
