---
title: Use the Native Functionality of a Retry Mechanism
description: Leverage Adobe I/O Events' retry mechanism for resilient applications, including retry conditions and visual indicators.
landing-page-description: Understand and utilize Adobe I/O Events' built-in retry mechanism to enhance application resilience and manage event activations effectively.
kt: 15872
doc-type: video
duration: 402
audience: all
last-substantial-update: 2024-7-31
feature: Best Practices, Backend Development, Integration
topic: Architecture, Commerce, Development
old-role: Architect, Developer
role: Developer
level: Intermediate
exl-id: 412060b3-76ae-4c27-bf96-8eb2a0f0d0e8
TQID: https://experienceleague.adobe.com/hrzcmSY8cAke4LBLRtqfkP8-t6jP4KMoMc7iL3WPRng
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: e8818fe6-9c8b-4bc0-9ef8-377a10b7bc75
    internal-label: Architecture
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
---
# Leverage Adobe I/O Events retry mechanism for application resilience

The video outlines a comprehensive guide on leveraging Adobe I/O Events' built-in retry mechanism to enhance application resilience. Learn how specific HTTP response status codes trigger event retries. Adobe I/O Events employs exponential and fixed back-off strategies for retries, with intervals increasing from one minute to 15 minutes. The documentation also details how retry indicators appear in the developer console, with visual cues like warning icons and circular arrows denoting failed and retried events, respectively.

Learn how the retry mechanism functions within the context of the 'consumer' runtime actions, and determine whether an event is retried. Successful responses are indicated with a 200 status code, while error responses include an error object with a 'statusCode' attribute. The 'consumer' runtime action determines the HTTP response code to return based on downstream processing outcomes, ensuring efficient event handling and eventual successful activations. 
 
## Audience 

* Developers who want to understand the specific HTTP response status codes that trigger event retries.
* Teams who want to learn about the exponential and fixed back-off strategies employed by Adobe I/O Events for retries.
* Developers who want to understand how visual indicators in the developer console represent failed and retried events.

## Video dontent

* Adobe I/O Events have a built-in out-of-the-box retry mechanism that automatically retries event activations based on specific HTTP response status codes.
* The retry mechanism implemented by Adobe I/O Events involves exponential and fixed back-off strategies. 
* Visual indicators in the developer console, such as warning icons for failed events and circular arrow icons for retried events.
* The 'consumer' runtime actions play a crucial role in determining the appropriate HTTP response status codes for event handling.

>[!VIDEO](https://video.tv.adobe.com/v/3431695?learn=on)

{{$include /help/_includes/starter-kit-related-links.md}}

## Related documentation

* [Webhook unable to handle an event](https://developer.adobe.com/events/docs/support/faq/#what-happens-if-my-webhook-is-unable-to-handle-a-specific-event-but-handles-all-other-events-gracefully)
* [Webhook down and marked as unstable](https://developer.adobe.com/events/docs/support/faq/#what-happens-if-my-webhook-is-down-why-is-my-event-registration-marked-as-unstable)
