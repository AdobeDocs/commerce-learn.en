---
title: View and set admin configurations using the command line
description: Learn how to view and set admin configurations using command line.
feature: Configuration,Console,System
topic: Administration,Commerce
role: Developer
level: Beginner
doc-type: Technical Video
duration: 510
last-substantial-update: 2024-01-31T00:00:00.000Z
jira: KT-14877
exl-id: 6cecba51-8d39-46f5-9864-80126d8ca3da
TQID: https://experienceleague.adobe.com/W0kaFd-DJAPA1kFO0hWaBZXsSarojbt5Hnv3QkW85hA
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: ba9e5be9-7de1-4f71-a5d2-baead0e425ee
    internal-label: Security
  - id: dac87252-6066-4d6e-a9d2-f6d84c323de7
    internal-label: Configuration
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
topic_v2:
  - id: d095671a-1355-40aa-8b5f-06c33c68080b
    internal-label: Security
  - id: eddd9b14-83bd-4ff4-9072-54a4a484abb7
    internal-label: Administration
---
# View and set admin configurations using the command line

A demonstration for how to view, set, and find config values with the Commerce CLI. Understand where the values are saved and also where the default values come from.

## Who is this video for?

* Adobe Commerce developers

## Video content

>[!VIDEO](https://video.tv.adobe.com/v/3427123?learn=on)

## Some commands used in the tutorial

Change the password security setting to recommended:

`$ php bin/magento config:set admin/security/password_is_forced 0`

Show the email address for the sales order auto copy functionality

`$ php bin/magento config:show sales_email/order/copy_to`

Show the empty result for a configuration that has a value in the admin

`php bin/magento config:show trans_email/ident_sales/email`

## Mysql queries used in the tutorial

```
SELECT * FROM core_config_data WHERE path = 'sales_email/order/copy_to';

SELECT * FROM core_config_data WHERE path = 'sales_email/order_comment/copy_to';

SELECT * FROM core_config_data WHERE path = 'trans_email/ident_sales/email';
```

## Where to find the default sales email

How to find the configuration value that is defined somewhere in codebase?
`grep -rnw vendor/magento/ -e 'sales@example.com'`

To view a page in terminal and show line numbers `cat -n vendor/magento/module-email/etc/config.xml`

## Additional resources

* [Command Line Tool](https://experienceleague.adobe.com/docs/commerce-operations/configuration-guide/cli/config-cli.html){target="_blank"}
* [Configure Admin security](https://experienceleague.adobe.com/docs/commerce-admin/systems/security/security-admin.html){target="_blank"}
