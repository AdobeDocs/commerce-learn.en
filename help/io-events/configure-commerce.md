---
title: Configure Adobe Commerce
description: Learn how to configure Adobe Commerce to allow events to be used in Adobe Developer App Builder.
landing-page-description: Learn how to configure Adobe Commerce to use the event mechanism for consumption by Adobe Developer App Builder.
short-description: Learn how to configure Adobe Commerce to use the event mechanism for consumption by Adobe Developer App Builder.
kt: 11889
doc-type: tutorial
duration: 299
audience: all
last-substantial-update: 2023-02-21T00:00:00.000Z
feature: App Builder, Configuration, Backend Development
topic: Commerce, Architecture
old-role: Architect, Developer
role: Developer, User
level: Beginner, Intermediate
exl-id: b8062042-2e90-4750-92ef-d55a76f2d842
TQID: https://experienceleague.adobe.com/6FBcDMDst5LBS7EyqA8zINr2Vs3bC--M7CXzIKf6EeQ
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: dac87252-6066-4d6e-a9d2-f6d84c323de7
    internal-label: Configuration
  - id: e8818fe6-9c8b-4bc0-9ef8-377a10b7bc75
    internal-label: Architecture
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
---
# Configure Adobe Commerce

Learn how to configure Adobe Commerce to expose the events. Additional documentation found at [Install Adobe I/O Events for Adobe Commerce](https://developer.adobe.com/commerce/events/get-started/installation/){target="_blank"}.

## Who is this video for?

* Developers new to Adobe Commerce and Adobe Developer App Builder using I/O events and need to create an Adobe App Builder project.

## Video content {#video-content}

* Configuration of the Adobe I/O events in the Commerce admin
* Saving a private key in the Commerce admin
* Saving the unique identifier in the Commerce admin
* Create an event provider

>[!VIDEO](https://video.tv.adobe.com/v/3415799?learn=on)

## Useful commands {#useful-commands}

```bash
bin/magento events:create-event-provider --label "my_provider" --description "Provides out-of-process extensibility for Adobe Commerce"

bin/magento events:subscribe observer.catalog_product_save_after --fields=name --fields=price
```

{{$include /help/_includes/io-events-related-links.md}}
