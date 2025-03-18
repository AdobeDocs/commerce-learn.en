---
title: Reset the Admin URI Using the CLI
description: Learn how to reset the admin URI in Adobe Commerce Cloud CLI. This method is handy when admin URL changes cause access issues.
feature: Admin Workspace, Console
topic: Administration, Commerce
role: Developer, User
level: Beginner
doc-type: Technical Video
duration: 123
last-substantial-update: 2024-10-14
jira: KT-16338
exl-id: dbc155d7-8ce9-4622-abfb-1d8077c3a975
---
# Reset the admin URI using the cli

Learn how to reset the admin URI using the Adobe Commerce Cloud cli command. This is useful if the admin URL was changed from the admin but a mistake was made and you are no longer able to access the admin.

>[!VIDEO](https://video.tv.adobe.com/v/3435066/?learn=on)

## Some commands used in the tutorial

Change the configuration to expect a custom Admin path URL to 0:

`$ php bin/magento config:set admin/url/use_custom 0`

Change the configuration for the custom Admin path URL to 0

`$ php bin/magento config:set admin/url/use_custom_path 0`
