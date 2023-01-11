---
title: Extending [!DNL Adobe Commerce] and [!DNL Magento Open Source] using Adobe Developer App Builder.
description: Learn about Adobe App Builder and why it is an important aspect of out of process extensibility
landing-page-description: Learn what is app builder and how it can help with Adobe Commerce and [!DNL Magento Open Source] development strategies.
kt: 11433
doc-type: tutorial
audience: all
last-substantial-update: 2023-01-11

---

# Out of process extensibility for [!DNL Adobe Commerce] and [!DNL Magento Open Source] using Adobe Developer App Builder {#adobe-developer-app-builder}

## What is App Builder for Adobe Commerce {#project-firefly}

Adobe Developer App Builder provides an extensibility framework for a developer to easily extend [!DNL Adobe Commerce] and [!DNL Magento Open Source] to provide out of process extensibility. 

App Builder provides a unified third-party extensibility framework for integrating and creating custom experiences that extend [!DNL Adobe Commerce]. With this complete extensibility framework, built on Adobe's infrastructure, developers can build custom microservices, extend, and integrate [!DNL Adobe Commerce] and [!DNL Magento Open Source] across Adobe solutions and any other 3rd party integration.

App Builder provides a way for customers to easily extend [!DNL Adobe Commerce] in various use cases:

* Middleware Extensibility - Connect external systems with Adobe applications building custom connectors or leverage a suite of pre-built integrations.
* Core Services Extensibility - Extend core application capabilities by extending the default behavior with custom features & business logic.
* User Experience Extensibility - Extend core experience to support business requirements or build customer-specific digital properties, storefronts & back-office apps.

App Builder (previously known as Project Firefly) is a cloud based solution, which means that it will automatically scale.  This service is also globally distributed to allow the best performance regardless of your geographic location.

## Why should you learn more about App Builder

There are numerous benefits to using an out of process option such as App Builder.  Because Adobe Commerce is not a fully offered SAAS offering, the code you develop or install instantly adds complexity and potential upgrade issues.  By leveraging out of process extensibility such as App builder, you can still provide custom, unique functionality to your Adobe Commerce store without being required to in process methods.  Other benefits include:

* De-coupled features allow for faster time to launch
* Upgrades will be easier because of the de-coupled approach, meaning the custom features live outside the commerce codebase and there are no compatibility issues to be overcome.
* Moving features and logic outside of commerce frees up resources and complicated logic that would normally occur using in process development methods.

## Architecture {#architecture}

Instead of an out-of-the-box solution, Adobe Developer App Builder provides a common, consistent, standardized development platform for extending Adobe Cloud solutions such as Adobe Commerce including:

* Adobe Developer Console — For custom microservice and extension development, letting developers build and manage projects while accessing all the tools and APIs they need to create plugins and integrations. 
* Developer Tools — Open-source tools, SDKs, and libraries to allow developers to easily build custom extensions and integrations. Use  React Spectrum (Adobe's UI toolkit) to have one common UI for all Adobe apps. 
* Services — I/O Runtime for hosting infrastructure on our serverless platform, and I/O Events for event-based integrations. We also provide out-of-the-box support for storing data and files. 
* Adobe Experience Cloud — Developers can submit extensions and integrations to be published within their Experience Cloud Org. System admins can then review, manage, and approve these extensions. Once published, your custom App Builder extensions and tools can be found alongside other Adobe Experience Cloud apps.

The following diagram illustrates how a standard application built on App Builder leverages these functionalities:

![Architecture](/help/assets/app-builder/firefly-architecture.jpeg)

For more details about the App Builder architecture, have a look at [Architecture Overview](https://www.adobe.io/app-builder/docs/guides/).

## Get Started with App Builder {#additional-resources}

To help you get started with App Builder we created a series of documentation to help you start:

* [App Builder Getting Started](https://www.adobe.io/app-builder/docs/getting_started/)

## Continue learning with Documentation {#appbuilder-documentation}

App Builder provides videos and documentation for developers including guides, and reference documentation to help you begin developing your own custom applications:

* [App Builder documentation](https://www.adobe.io/app-builder/docs/overview/)
* [App Builder videos](https://www.youtube.com/playlist?list=PLcVEYUqU7VRfDij-Jbjyw8S8EzW073F_o)

## Try Out One of the Sample Applications {#appbuilder-codesamples}

Ready to start developing? We have lots of sample applications to help you get going quickly:

* [App Builder Code Labs on Adobe Developer Website](https://www.adobe.io/app-builder/docs/resources/)

## Support {#support}

For developer support type of requests, we encourage developers to use our [Experience League forum](https://experienceleaguecommunities.adobe.com/t5/project-firefly/ct-p/project-firefly).







