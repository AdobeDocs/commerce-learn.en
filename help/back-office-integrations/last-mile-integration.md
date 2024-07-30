---
title: Last mile integration in the Commerce integration starter kit. 
description: Last mile integration in Commerce, highlighting extensibility hooks like validation, transformation, preprocessing, sending, and post-processing.​
landing-page-description: Learn the structure and functions of extensibility hooks in last mile integration for Commerce systems.   
kt: 15869
doc-type: video
duration: 465
audience: all
last-substantial-update: 2024-7-30
feature: Best Practices, Backend Development, Integration
topic: Architecture, Commerce, Development
role: Architect, Developer
level: Intermediate
---
# Last mile integration using the Adobe Starter Kit  

Learn about the intricacies of last mile integration within Commerce systems, focusing on the utilization of extensibility hooks to enhance connectivity with third-party systems. This video outlines a structured approach where various hooks such as validation, transformation, preprocessing, sending, and post-processing are employed to ensure seamless data flow and system synchronization. Each hook serves a distinct purpose, from validating incoming data against schemas to transforming data objects between systems, and from performing calculations before sending relevant information to executing the actual data send to the destination system. The document emphasizes the importance of maintaining separate JavaScript files for each block to uphold business logic integrity and facilitate future framework upgrades, ensuring a robust and adaptable integration setup.

Learn about the significance of post-processing activities through the post process hook, enabling users to conduct additional actions after data synchronization, such as adding comments to orders or storing external IDs. ​ It also advocates for best practices like encapsulating API requests within specific libraries to streamline connections with third-party systems. Learn a few typical use cases for each hook and offering guidance on handling various scenarios.   

## Audience 

* Developers who need to learn the structure and functionality of extensibility hooks, and how these hooks can be used to enhance connectivity with third-party systems.
* Developers needing to learn typical use cases and best practices associated with each extensibility hook, such as validation, transformation, preprocessing, sending, and post-processing, to facilitate seamless data flow, system synchronization, and efficient integration setup maintenance. ​
  
## Video Content

* Learn about the structure of the invoked actions in last mile integration.
* Understand typical use cases within the validation hook, including validating incoming data against schemas and skipping specific events based on certain criteria. ​
* Learn the role of the transform hook in transforming data objects between the origin and destination systems.
* Learn about the significance of the send hook in facilitating the actual data send to the destination system.

>[!VIDEO](https://video.tv.adobe.com/v/3431694?learn=on)

{{$include /help/_includes/starter-kit-related-links.md}}
