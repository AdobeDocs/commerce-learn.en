---
title: Learn about the quality patch tool
description: Enhance your e-commerce platform's stability and security by applying quality patches. Stay up-to-date, address issues, and optimize performance with this essential tool.
feature: Cloud, Configuration, Logs, System, Tools and External Services
topic: Architecture, Commerce, Development
role: Admin, Architect, User
level: Beginner, Intermediate
doc-type: Technical Video
duration: 771
last-substantial-update: 2024-07-17
jira: KT-15836
---
# What to expect from watching this video

Learn how to triage an issue, then use some basic techniques to find a quality patch to apply a fix.

## Who is this video for?

* Developers learning how to find issues and leverage this tool for applying GIT patches for known issues

## Video content
 
The Quality Patches Tool is a command-line utility for Adobe Commerce and Magento Open Source. Here's what it allows you to do:

* View general information about the latest quality patches.
* Apply quality patches to your installation.
* Revert applied patches if needed 

These patches are developed from Adobe Developers the Magento Open Source community to enhance stability and performance. Keep in mind that it's not recommended for applying large numbers of patches, as it can complicate future upgrades.

>[!VIDEO](https://video.tv.adobe.com/v/3431436?learn=on)

## Why use the quality patch tool?

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