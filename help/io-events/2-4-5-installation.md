---
title: Learn how to install IO events for Adobe Commerce 2.4.5
description: Learn how to install modules needed for IO events in Adobe Commerce 2.4.5 for use in Adobe Developer App Builder
jira: KT-11886
doc-type: Tutorial
duration: 179
last-substantial-update: 2023-02-22
badge: Adobe Commerce 2.4.5
feature: App Builder, Eventing
topic: Commerce, Architecture
role: Developer
level: Beginner, Intermediate
exl-id: e0adfd85-5a3d-44ba-aab5-ecd7c61715cf
TQID: https://experienceleague.adobe.com/vb-q-JXeM4KvkxzfDui1MaTOSBFXDVBwmpTeolUtKGw
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
# Adobe Commerce 2.4.5 Installation

Learn how to install several new modules in Adobe Commerce using Composer for version 2.4.5. This sets up the required modules to be used in the Adobe Commerce application. Additional documentation found at [Install Adobe I/O Events for Adobe Commerce](https://developer.adobe.com/commerce/extensibility/events/installation){target="_blank"}.

## Who is this video for?

* Developers new to Adobe Commerce and Adobe Developer App Builder using I/O Events

## Video content {#video-content}

* Installation of required modules using composer
* Commands to run for on premise hosting
* Commands to run for Adobe Commerce Cloud
* Adobe Commerce Cloud yaml required edit

>[!VIDEO](https://video.tv.adobe.com/v/3415794?learn=on)

## Available commands {#useful-commands}

There are various commands that slightly differ, depending on whether you are on a self-hosted environment or using Adobe Commerce Cloud.

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


