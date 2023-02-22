---
title: Learn how to configure Adobe Commerce to expose events
description: Learn how to configure Adobe Commerce to allow events to be used in Adobe Developer App Builder.
landing-page-description: Learn how to configure Adobe Commerce to use the event mechanism for consumption by Adobe Developer App Builder.
kt: 11889
doc-type: tutorial
audience: all
last-substantial-update: 2023-02-21

---

# Adobe Commerce configuration

Learn how to configure Adobe Commerce to expose the events.

## Who is this video for?

* Developers new to Adobe Commerce and Adobe Developer App Builder using I/O events and need to create an Adobe App Builder project.

## Video content {#video-content}

* Configuration of the Adobe I/O events in the Commerce admin
* Saving private key in Commerce admin
* Saving unique identifier in Commerce admin
* Create an events provider

>[!VIDEO](https://video.tv.adobe.com/v/3415799)

## Useful commands {#useful-commands}

```bash
bin/magento events:create-event-provider --label "my_provider" --description "Provides out-of-process extensibility for Adobe Commerce"

bin/magento events:subscribe observer.catalog_product_save_after --fields=name --fields=price
```


{{$include /help/_includes/io-events-related-links.md}}
