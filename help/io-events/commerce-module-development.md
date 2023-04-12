---
title: Learn how to create a module in Adobe Commerce to use events.
description: Learn how to create Commerce module to use events.
landing-page-description: Learn how to create an Adobe Commerce module to use events.
short-description: Learn how to create an Adobe Commerce module to use events.
kt: 11891
doc-type: tutorial
audience: all
last-substantial-update: 2023-02-21
exl-id: e8103fe0-116a-499c-ae0a-3ad0511f44d0
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

>[!VIDEO](https://video.tv.adobe.com/v/3415802?quality=12&learn=on)

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
