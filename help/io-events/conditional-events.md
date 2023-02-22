---
title: Learn how to use conditional events in Adobe Commerce
description: Learn how to use conditional events to be used in Adobe Developer App Builder.
landing-page-description: Learn how to use Adobe Commerce conditional events.
kt: 11890
doc-type: tutorial
audience: all
last-substantial-update: 2023-02-21

---

# Adobe Commerce conditional events

Learn about conditional events in Adobe Commerce that can be used in Adobe Developer App Builder. Additional documentation found at [Install Adobe I/O Events for Adobe Commerce](https://developer.adobe.com/commerce/events/get-started/installation/){target="_blank"}.

## Who is this video for?

* Developers new to Adobe Commerce and Adobe Developer App Builder using I/O events and need to create an Adobe App Builder project.

## Video content {#video-content}

* Learn about conditional events
* Learn proper usage for new XML file io_events.xml
* Learn how to configure conditional events
* Defining rules for use in conditional events
* Learn how to register events in the Commerce instances `app/etc/config.php`

>[!VIDEO](https://video.tv.adobe.com/v/3415806)

## Useful commands {#useful-commands}

```bash
bin/magento events:subscribe plugin.magento.catalog.model.resource_model.product.save --fields=sku --fields=qty --fields=category_id

bin/magento events:subscribe plugin.magento.catalog.model.resource_model.product.save_low_stock --parent=plugin.magento.catalog.model.resource_model.product.save --fields=sku --fields=qty --fields=category_id --rules="qty|lessThan|20" --rules="category_id|in|3,4,5"

cat app/etc/config.php

php bin/magento events:list

php bin/magento events:list -v
```

{{$include /help/_includes/io-events-related-links.md}}
