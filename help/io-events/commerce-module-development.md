---
title: Learn how to create a module in Adobe Commerce to use events.
description: Learn how to create Commerce module to use events.
landing-page-description: Learn how to create an Adobe Commerce module to use events.
short-description: Learn how to create an Adobe Commerce module to use events.
kt: 11891
doc-type: tutorial
duration: 348
audience: all
last-substantial-update: 2023-02-21T00:00:00.000Z
feature: App Builder, Eventing, Backend Development
topic: Commerce, Architecture
old-role: Architect, Developer
role: Developer
level: Beginner, Intermediate
exl-id: e8103fe0-116a-499c-ae0a-3ad0511f44d0
TQID: https://experienceleague.adobe.com/bRnOh6fnsyTY-21f81vIXV4-eeitLXQWsAbjg2rx-Is
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
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
---
# Adobe Commerce module development

Learn how register events, find supported events, and how to use a new XML file `io_events.xml` in custom module development. The video will also show developers how to find registered events that can used as well as unsubscribe any events that may already be defined. Additional documentation found at [Install Adobe I/O Events for Adobe Commerce](https://developer.adobe.com/commerce/events/get-started/installation/){target="_blank"}.

## Who is this video for?

* Developers new to Adobe Commerce and Adobe Developer App Builder using I/O events.

## Video content {#video-content}

* Registering events in Commerce for use in Adobe Developer App Builder
* Identify events that can be registered
* Learn how to register events in io_events.xml
* Learn how to register events in the Commerce instances `app/etc/config.php`
* Learn how to unsubscribe to an event

>[!VIDEO](https://video.tv.adobe.com/v/3415802?learn=on)

## Useful commands {#useful-commands}

```bash
bin/magento events:list:all Magento_Catalog

bin/magento events:info plugin.magento.catalog.api.category_repository.save

bin/magento events:subscribe observer.catalog_category_save_after --fields=entity_id --fields=parent_id

cat app/etc/config.php

bin/magento events:unsubscribe observer.catalog_category_save_after

bin/magento events:list
```

{{$include /help/_includes/io-events-related-links.md}}
