---
title: Learn how to install IO events for Adobe Commerce 2.4.5
description: Learn how to install modules needed for IO events in Adobe Commerce 2.4.5 for use in Adobe Developer App Builder
landing-page-description: Learn how to install several modules needed for Adobe Commerce 2.4.5 using composer.
short-description: Learn how to install several modules needed for Adobe Commerce 2.4.5 using composer.
kt: 11886
doc-type: tutorial
audience: all
last-substantial-update: 2023-02-22
badge: Adobe Commerce 2.4.5
feature: App Builder, Eventing
topic: Commerce, Architecture
role: Architect, Developer
level: Beginner, Intermediate
exl-id: e0adfd85-5a3d-44ba-aab5-ecd7c61715cf
---
# Adobe Commerce 2.4.5 Installation

Learn how to install several new modules in Adobe Commerce using Composer for version 2.4.5. This sets up the required modules to be used in the Adobe Commerce application. Additional documentation found at [Install Adobe I/O Events for Adobe Commerce](https://developer.adobe.com/commerce/events/get-started/installation/){target="_blank"}.

## Who is this video for?

* Developers new to Adobe Commerce and Adobe Developer App Builder using I/O Events

## Video content {#video-content}

* Installation of required modules using composer
* Commands to run for on premise hosting
* Commands to run for Adobe Commerce Cloud
* Adobe Commerce Cloud yaml required edit

>[!VIDEO](https://video.tv.adobe.com/v/3415794?quality=12&learn=on)

## Useful commands {#useful-commands}

There are various commands that slightly differ, depending if you are on a self-hosted environment or using Adobe Commerce Cloud.

### On Premise hosting {#on-premise}

```bash
composer require magento/commerce-eventing=^1.0 --no-update

composer update

bin/magento events:generate:module

bin/magento module:enable --all

bin/magento setup:upgrade && bin/magento setup:di:compile
```

### Adobe Commerce on Cloud {#adobe-commerce-cloud}

```bash
composer require magento/commerce-eventing=^1.0 --no-update

composer update

composer info magento/ece-tools
```

Commerce Cloud `.magento.env.yaml`:

```yaml
stage:
  global:
    ENABLE_EVENTING: true
```

{{$include /help/_includes/io-events-related-links.md}}
