---
title: Learn how to use conditional events in Adobe Commerce
description: Learn how to use conditional events to be used in Adobe Developer App Builder.
landing-page-description: Learn how to use Adobe Commerce conditional events.
short-description: Learn how to use Adobe Commerce conditional events.
kt: 11890
doc-type: tutorial
duration: 421
audience: all
last-substantial-update: 2023-02-21T00:00:00.000Z
feature: App Builder, Eventing, Backend Development
topic: Commerce, Architecture
old-role: Architect, Developer
role: Developer
level: Beginner, Intermediate
exl-id: 03787aa3-051b-4a35-b2e8-ecf6762b5eb4
TQID: https://experienceleague.adobe.com/GuN9--5xQaBnbFvQrkGuqMcDMMe-1tVGPk-hvqs4-UY
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
# Adobe Commerce conditional events

Learn about conditional events in Adobe Commerce that can be used in Adobe Developer App Builder. Additional documentation found at [Install Adobe I/O Events for Adobe Commerce](https://developer.adobe.com/commerce/extensibility/events/conditional-events/){target="_blank"}.

## Who is this video for?

* Developers new to Adobe Commerce and Adobe Developer App Builder using I/O events and need to create an Adobe App Builder project.

## Video content {#video-content}

* Learn about conditional events
* Learn proper usage for new XML file io_events.xml
* Learn how to configure conditional events
* Defining rules for use in conditional events
* Learn how to register events in the Commerce instances `app/etc/config.php`

>[!VIDEO](https://video.tv.adobe.com/v/3415806?learn=on)

## Useful commands {#useful-commands}

```bash
bin/magento events:subscribe plugin.magento.catalog.model.resource_model.product.save --fields=sku --fields=qty --fields=category_id

bin/magento events:subscribe plugin.magento.catalog.model.resource_model.product.save_low_stock --parent=plugin.magento.catalog.model.resource_model.product.save --fields=sku --fields=qty --fields=category_id --rules="qty|lessThan|20" --rules="category_id|in|3,4,5"

cat app/etc/config.php

bin/magento events:list

bin/magento events:list -v
```

{{$include /help/_includes/io-events-related-links.md}}
