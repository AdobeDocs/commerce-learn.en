---
title: Quality Patch Tool
description: Learn how to use the quality patch tool when diagnosing a problem, finding a solution and applying a patch found in the existing list of patches available.
feature: Cloud, Configuration, Logs, System, Tools and External Services
topic: Architecture, Commerce, Development
role: Admin, Developer, User
level: Beginner, Intermediate
doc-type: Technical Video
duration: 903
last-substantial-update: 2024-07-17T00:00:00.000Z
jira: KT-15836
exl-id: 16710f27-1232-4c6a-aac3-9838308d1267
TQID: https://experienceleague.adobe.com/GpcJqSCn3XqLZtm-QdQ-ka9c-RdkG-C6Hd3FpXrh8-I
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: ba9e5be9-7de1-4f71-a5d2-baead0e425ee
    internal-label: Security
  - id: dac87252-6066-4d6e-a9d2-f6d84c323de7
    internal-label: Configuration
  - id: e8818fe6-9c8b-4bc0-9ef8-377a10b7bc75
    internal-label: Architecture
  - id: f42e0a1a-0d79-488d-a83f-f2c30672b137
    internal-label: Reporting
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
  - id: d095671a-1355-40aa-8b5f-06c33c68080b
    internal-label: Security
---
# Quality patch tool

Learn how to use the quality patch tool when diagnosing a problem, finding a solution and applying a patch found in the existing list of patches available.

## What you'll learn

Learn how to triage an issue, then use some basic techniques to find a quality patch to apply a fix.

## Audience

* Developers learning how to find issues and leverage this tool for applying GIT patches for known issues

## Video content

The Quality Patches Tool is a command-line utility for Adobe Commerce and Magento Open Source. Here's what it allows you to do:

* View general information about the latest quality patches.
* Apply quality patches to your installation.
* Revert applied patches if needed 

These patches are developed from Adobe Developers the Magento Open Source community to enhance stability and performance. Keep in mind that it's not recommended for applying large numbers of patches, as it can complicate future upgrades.

>[!VIDEO](https://video.tv.adobe.com/v/3431436?learn=on)

## Why use the quality patch tool

You might want to use the Quality Patches Tool for Adobe Commerce or Magento Open Source if you're looking to:

Enhance stability and performance: Quality patches address issues, improve security, and optimize your installation.
Stay up-to-date: Applying patches ensures that your system is current and protected.
Revert changes: If a patch causes unexpected issues, you can revert it using the tool. Remember, it's best suited for applying a limited number of patches to avoid complicating future upgrades.  

## Limitations or concerns with using the quality patch tool

While the Quality Patches Tool offers benefits, there are a few considerations to keep in mind:

* Compatibility: Ensure that the patches are compatible with your specific version of Adobe Commerce or Magento Open Source.
* Testing: Always test patches in a staging environment before applying them to production. Unexpected issues can arise.
* Patch Dependencies: Some patches may depend on others. Be aware of any prerequisites.
* Customizations: If you've made custom code changes, patches might conflict. Review the changes carefully.
* Back up: Back up your installation before applying patches to avoid data loss. 

While the Quality Patches Tool is useful for applying a limited number of patches, it's not recommended for handling a large volume of patches. Applying too many patches can complicate future upgrades and maintenance. If you have numerous patches to apply, consider alternative approaches or consult with a Magento specialist. 

## Summary

The Quality Patches Tool allows e-commerce platforms to enhance stability and security by applying patches. These patches address issues, improve performance, and optimize the system. Keeping your installation up-to-date ensures protection against vulnerabilities.

Before applying patches, it's crucial to test them in a staging environment. Ensure compatibility with your specific version of Adobe Commerce or Magento Open Source. Some patches may have dependencies, so review the prerequisites carefully.

 Back up your installation before applying patches to prevent data loss. If you've made custom code changes, be aware that patches might conflict. Follow best practices and monitor the impact of each patch.

## Related articles and videos

* [Quality Patch Tools search](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html)
* [Release notes](https://experienceleague.adobe.com/en/docs/commerce-operations/tools/quality-patches-tool/release-notes)
* [Github for patches](https://github.com/magento/quality-patches/blob/master/patches/os/)
* [Usage of quality patch tool](https://experienceleague.adobe.com/en/docs/commerce-operations/tools/quality-patches-tool/usage)
* [Technical video on QPT](https://experienceleague.adobe.com/en/docs/commerce-learn/tutorials/tools/quality-patch-tool)
