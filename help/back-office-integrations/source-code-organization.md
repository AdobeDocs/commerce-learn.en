---
title: Learn about the Commerce Integration Starter Kit with key folders and automation scripts explained
description: Learn about the organization of source code in the Commerce Integration starter kit. ​
landing-page-description: Exploring Source Code Organization in a Commerce Integration Starter Kit
kt: 15868
doc-type: video
duration: 420
audience: all
last-substantial-update: 2024-7-30
feature: Best Practices, Backend Development, Integration
topic: Architecture, Commerce, Development
old-role: Architect, Developer
role: Developer
level: Intermediate
exl-id: 678f4d2b-c57e-4afb-a535-1048a88bc3b1
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
