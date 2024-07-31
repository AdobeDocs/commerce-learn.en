---
title: Ensure robustness using the native functionality of a retry mechanism.
description: Leveraging Adobe I/O Events' retry mechanism for resilient applications, including retry conditions and visual indicators. ​
landing-page-description: Understand and utilize Adobe I/O Events' built-in retry mechanism to enhance application resilience and manage event activations effectively. ​   
kt: 15872
doc-type: video
duration: 314
audience: all
last-substantial-update: 2024-7-31
feature: Best Practices, Backend Development, Integration
topic: Architecture, Commerce, Development
role: Architect, Developer
level: Intermediate
---
# Leveraging Adobe I/O Events Retry Mechanism for Application Resilience ​

The video outlines a comprehensive guide on leveraging Adobe I/O Events' built-in retry mechanism to enhance application resilience. Learn how specific HTTP response status codes trigger event retries.​ Adobe I/O Events employ exponential and fixed back-off strategies for retries, with intervals increasing from one minute to 15 minutes. ​ The document also details how retry indicators appear in the developer console, with visual cues like warning icons and circular arrows denoting failed and retried events, respectively.

Learn how the retry mechanism functions within the context of 'consumer' runtime actions, and determine whether an event is retried. ​ Successful responses are indicated with a 200 status code, while error responses include an error object with a 'statusCode' attribute. ​ The 'consumer' runtime action determines the HTTP response code to return based on downstream processing outcomes, ensuring efficient event handling and eventual successful activations. ​
 

## Audience 

* Developers who need to understand the specific HTTP response status codes that trigger event retries.
* Teams who need to learn about the exponential and fixed back-off strategies employed by Adobe I/O Events for retries.
* Developers needing to understand how visual indicators in the developer console represent failed and retried events.

## Video Content

* Adobe I/O Events have a built-in out-of-the-box retry mechanism that automatically retries event activations based on specific HTTP response status codes.​
* The retry mechanism implemented by Adobe I/O Events involves exponential and fixed back-off strategies. ​
* Visual indicators in the developer console, such as warning icons for failed events and circular arrow icons for retried events.
* The 'consumer' runtime actions play a crucial role in determining the appropriate HTTP response status codes for event handling.

>[!VIDEO](https://video.tv.adobe.com/v/3431695?learn=on)

{{$include /help/_includes/starter-kit-related-links.md}}
