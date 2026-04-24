---
title: Reset the Admin URI Using the CLI
description: Learn how to reset the admin URI in Adobe Commerce Cloud CLI. This method is handy when admin URL changes cause access issues.
feature: Admin Workspace, Console
topic: Administration, Commerce
role: Developer, User
level: Beginner
doc-type: Technical Video
duration: 144
last-substantial-update: 2024-10-14T00:00:00.000Z
jira: KT-16338
exl-id: dbc155d7-8ce9-4622-abfb-1d8077c3a975
TQID: https://experienceleague.adobe.com/OgyaTHVhQSRFApJPYwkzodSyAJcBjwk8kIrw4VBXltQ
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: dac87252-6066-4d6e-a9d2-f6d84c323de7
    internal-label: Configuration
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
topic_v2:
  - id: eddd9b14-83bd-4ff4-9072-54a4a484abb7
    internal-label: Administration
---
# Reset the admin URI using the cli

Learn how to reset the admin URI using the Adobe Commerce Cloud cli command. This is useful if the admin URL was changed from the admin but a mistake was made and you are no longer able to access the admin.

>[!VIDEO](https://video.tv.adobe.com/v/3435066?learn=on)

## Some commands used in the tutorial

Change the configuration to expect a custom Admin path URL to 0:

`$ php bin/magento config:set admin/url/use_custom 0`

Change the configuration for the custom Admin path URL to 0

`$ php bin/magento config:set admin/url/use_custom_path 0`
