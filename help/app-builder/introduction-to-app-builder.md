---
title: Out-of-process extensibility for Adobe Commerce
description: Learn about Adobe App Builder and why it is an important aspect of out-of-process extensibility.
landing-page-description: Learn what is App Builder and how it can help with Adobe Commerce development strategies.
short-description: Learn what is App Builder and how it can help with Adobe Commerce development strategies.
kt: 11433
doc-type: tutorial
audience: all
last-substantial-update: 2023-2-16
feature: API Mesh, App Builder, Extensibility, Tools and External Services, Backend Development
topic: App Builder, I/O Events, Developer Console, Commerce, Development, Integrations
role: Architect, Developer
level: Beginner, Intermediate
exl-id: 94f8d82a-4a95-46ea-8eed-edf9bed5760c
---
# Introduction to App Builder

Historically, Adobe Commerce development has used in-process extensibility. The in-process model requires any new code to be compatible with upgrades, the server's PHP version, and many other essential server applications and services that Commerce uses. Adobe Developer App Builder uses out-of-process extensibility to avoid these compatibility issues.

## App Builder for Adobe Commerce {#app-builder}

>[!VIDEO](https://video.tv.adobe.com/v/3412839?quality=12&learn=on)

Adobe Developer App Builder is a serverless extensibility platform for integrating and creating custom experiences to extend Adobe solutions, and it's now available for Adobe Commerce. With App Builder, you can build secure and scalable apps that extend Commerce-native functionality and integrate with third-party solutions. As a developer, you can now take advantage of out-of-process extensibility with Adobe Commerce and that in turn provides immediate and long-term benefits.

App Builder provides a unified third-party extensibility framework for integrating and creating custom applications that extend [!DNL Adobe Commerce]. Since this extensibility framework is built on Adobe's infrastructure, developers can build custom microservices, and extend and integrate [!DNL Adobe Commerce] across other Adobe solutions and third-party integrations.

App Builder provides a way for customers to extend [!DNL Adobe Commerce] in various use cases:

* middleware extensibility - Connect external systems with Adobe applications by building custom connectors or take advantage of a suite of pre-built integrations.
* core services extensibility - Extend core application capabilities by extending the default behavior with custom features and business logic.
* user experience extensibility - Extend core experience to support business requirements or build customer-specific digital properties, storefronts, and back-office applications.

Adobe Developer App Builder is a cloud-based solution, which means that it automatically scales. This service is also globally distributed to allow the best performance regardless of your geographic location.

## Why should you learn more about App Builder

Since Adobe Commerce is not a fully SAAS product, the code you develop can add complexity and upgrade issues. By using out-of-process extensibility, such as App Builder, you can provide custom, unique functionality to your Adobe Commerce store without requiring in-process methods.

Other benefits include:

* Decoupled features allow for faster time to launch.
* Upgrades are now easier. The custom features are outside the Commerce codebase, which prevents  compatibility issues when upgrading.
* Moving features and logic outside of Commerce frees up resources that are normally used by in-process development methods.

## Architecture {#architecture}

Instead of an out-of-the-box solution, Adobe Developer App Builder provides a common, consistent, and standardized development platform for extending Adobe Cloud solutions such as Adobe Commerce including:

* Adobe Developer Console used for custom microservice and extension development. Build and manage projects while accessing all the tools and APIs needed to create plugins and integrations. 
* Open-source tools, SDKs, and libraries to build custom extensions and integrations. Use  React Spectrum (Adobe's UI toolkit) to have one common UI for all Adobe apps. 
* services such as I/O Runtime for hosting infrastructure on Adobe's serverless platform and I/O Events for event-based integrations. Adobe also provides out-of-the-box support for storing data and files. 
* Adobe Experience Cloud where you submit extensions and integrations to publish in your Experience Cloud Org. System admins can review, manage, and approve these extensions. Once published, your custom App Builder extensions and tools are available alongside other Adobe Experience Cloud apps.

The following diagram illustrates how a standard application built on App Builder uses these functionalities:

![Architecture](/help/assets/app-builder/app-builder-architecture.jpeg)

For more details about the App Builder architecture, see the [Architecture Overview](https://developer.adobe.com/app-builder/docs/guides/){target="_blank"}.

## Amazon Sales Channel extension {#amazon-sales-channel-extension}

>[!IMPORTANT]
>
>The Amazon Sales Channel extension is still under development and has not been officially released.  These videos and tutorials are meant to show you how to use Adobe Developer App Builder for a practical use case.

The following tutorials demonstrate how to connect Adobe Commerce to Amazon Sales Channel using an App Builder extension. 

* [technical overview App Builder](../app-builder/app-builder-technical-overview.md)
* [extensibility framework](../app-builder/extensibility-framework-commerce-eventing.md)
* [functional demonstration App Builder](../app-builder/app-builder-functional-demonstration.md)

## Get Started with App Builder {#additional-resources}

A n overview of composable commerce strategy, that includes the initial set-up can be found by reading the following blog post:

[How App Builder helps drive business agility for your commerce platform](https://business.adobe.com/blog/how-to/how-app-builder-helps-you-implement-a-composable-commerce-strategy){target="_blank"}

To help you get started with App Builder, Adobe has created the following documentation:

* [App Builder Getting Started](https://developer.adobe.com/app-builder/docs/getting_started/){target="_blank"}

## Continue learning with Documentation {#appbuilder-documentation}

App Builder provides videos and documentation for developers, including guides and reference documentation to help develop your own custom applications:

* [App Builder documentation](https://developer.adobe.com/app-builder/docs/overview/){target="_blank"}
* [App Builder videos](https://www.youtube.com/playlist?list=PLcVEYUqU7VRfDij-Jbjyw8S8EzW073F_o){target="_blank"}

## Try Out One of the Sample Applications {#appbuilder-codesamples}

Ready to start developing? The following link contains sample applications to help get you started:

* [App Builder Code Labs on Adobe Developer Website](https://developer.adobe.com/app-builder/docs/resources/){target="_blank"}

## Support {#support}

For developer support requests, use the [Experience League forum](https://experienceleaguecommunities.adobe.com/t5/app-builder/ct-p/project-firefly){target="_blank"} for assistance.

{{$include /help/_includes/app-builder-related-links.md}}
