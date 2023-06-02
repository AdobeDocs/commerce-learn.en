---
title: Create a module
description: Create a page that returns json with one parameter.
topic: Development
kt: 5614
doc-type: video
activity: use
last-substantial-update: 2023-6-2
exl-id: 941c04ee-54b8-4b81-b77d-fff5875927f0
---
# Create a module

Module is a structural element of [!DNL Commerce] – the whole system is built upon modules. Typically, the first step in creating a customization is building a module.

## Who is this video for?

- Developers

## Steps to add a module

- Create the module folder.
- Create the etc/module.xml file.
- Create the registration.php file.
- Run the bin/magento setup.
- Upgrade script to install the new module.
- Check that the module is working.

>[!VIDEO](https://video.tv.adobe.com/v/35792?learn=on)

### module.xml

```xml
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:noNamespaceSchemaLocation="urn:magento:framework:Module/etc/module.xsd">
    <module name="Training_Sales">
        <sequence>
            <module name="Magento_Sales"/>
        </sequence>
    </module>
</config>
```

### registration.php

```PHP
<?php

use Magento\Framework\Component\ComponentRegistrar;

ComponentRegistrar::register(
    ComponentRegistrar::MODULE,
    'Training_Sales',
    __DIR__);
```

## Useful resources

- [Module Reference guide](https://developer.adobe.com/commerce/php/module-reference/)
