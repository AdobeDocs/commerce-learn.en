---
title: Configure Adobe Commerce
description: Learn how to configure Adobe Commerce to allow events to be used in Adobe Developer App Builder.
landing-page-description: Learn how to configure Adobe Commerce to use the event mechanism for consumption by Adobe Developer App Builder.
short-description: Learn how to configure Adobe Commerce to use the event mechanism for consumption by Adobe Developer App Builder.
kt: 11889
doc-type: tutorial
audience: all
last-substantial-update: 2023-02-21
feature: App Builder, Configuration, Backend Development
topic: Commerce, Architecture
role: Architect, Developer, User
level: Beginner, Intermediate
exl-id: b8062042-2e90-4750-92ef-d55a76f2d842
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

>[!VIDEO](https://video.tv.adobe.com/v/3415799?quality=12&learn=on)

## Useful commands {#useful-commands}

```bash
bin/magento events:create-event-provider --label "my_provider" --description "Provides out-of-process extensibility for Adobe Commerce"

bin/magento events:subscribe observer.catalog_product_save_after --fields=name --fields=price
```

{{$include /help/_includes/io-events-related-links.md}}
