---
title: Source code organization in the Commerce starter kit
description: Learn about source code organization in the Commerce Integration starter kit, including key folders like actions and scripts, automation scripts, and event handling.
doc-type: Technical Video
duration: 534
last-substantial-update: 2024-07-30
feature: Best Practices, Backend Development, Integration
topic: Architecture, Commerce, Development
role: Developer
level: Intermediate
jira: KT-15868
exl-id: 678f4d2b-c57e-4afb-a535-1048a88bc3b1
TQID: https://experienceleague.adobe.com/P6-sK18TcpC91YXJcXohIvzmii3N66ZKh3nZha-RYQY
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
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
  - id: e1e0219c-f879-479f-8427-888ed2a6e9c2
    internal-label: Insights
---
# Source code organization for the Adobe Starter Kit  

Learn about the source code organization within the Adobe Commerce Integration starter kit.​ Explore the structure of the project, highlighting key folders such as `actions` and `scripts`, and their respective contents.​ The 'actions' folder contains subfolders like `ingestion` and `webhook` that contain essential code for event handling and tracking. You will also learn about the `starter-kit-info` and `scripts` folders. The `scripts` folder focuses on automation scripts like `commerce-event-subscribe` and `onboarding` that streamline event configuration and provider setup within the project.
 ​
Explore the logic behind the source code structure, detailing how the `commerce` and `external` folders under each entity folder handle events originating from different systems. The video explains the role of the `consumer` folder in dispatching events to the appropriate event handler runtime action, ensuring seamless processing. The video also covers the retry mechanism implemented in the runtime actions to handle failing events effectively. ​Understand the organization and functionality of source code in the Adobe Commerce Integration starter kit, offering valuable insights into event handling, automation scripts, and configuration setups.

## Audience 

* Developers who want to understand how the source code is organized into key folders such as `actions` and `scripts`.
* Learn about the `actions` folder contains subfolders like `ingestion` and` webhook` that contain essential code for handling events and tracking deployments.
* Developers who want to learn about the `actions` folder that includes folders for entities like `customer`, `order`, `product`, and `stock`.

## Video Content

* Understand that the four main folders: `actions`, `scripts`, `test`, and `utils`, with a focus on the `actions` and `scripts` folders during the session. ​
* Learn about the `actions` folder and how it contains crucial subfolders like `ingestion` and `webhook`.
* Explore the `actions` folder and why there are specific folders for entities like `customer`, `order`, `product`, and `stock`, each containing runtime actions structured into `commerce` and `external` folders to manage events from Commerce and third-party systems effectively. ​
* Learn the importance of not altering the code in the `starter-kit-info` folder, which contains a runtime action used by Adobe to track project deployments based on the starter kit. ​
* Understand the `scripts` folder that contains automation scripts like `commerce-event-subscribe` and `onboarding`, which automate event configuration, provider setup, and the configuration of the Adobe I/O Events module in Commerce. ​

>[!VIDEO](https://video.tv.adobe.com/v/3431691?learn=on)

{{$include /help/_includes/starter-kit-related-links.md}}
