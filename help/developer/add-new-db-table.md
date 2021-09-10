---
title: Add a table to a database
description: Commerce has a special mechanism that enables you to create database tables, modify existing ones, and even add some data into them.
topic: Development
kt: 5613
doc-type: video
activity: use
---

# Add a table to a database {#main}

Commerce has a special mechanism that enables you to create database tables, modify existing ones, and even add some data into them - like setup data, which has to be added when a module is installed. This mechanism allows those changes to be transferable between different installations.

Rather than doing manual SQL operations repeatedly when reinstalling the system, developers create an install (or upgrade) script that contains the data. The script runs every time a module is installed.

## Who is this video for?

- Developers

## Video content

- Create a module
- Create InstallSchema Script
- Create InstallData Script
- Add new module and verify that a table with data was created
- Create an UpgradeSchema script
- Create an UpgradeData script
- Run upgrade scripts and verify that the table has changed

>[!VIDEO](https://video.tv.adobe.com/v/35791?quality=12&learn=on)

## Useful resources

- [Migration commands](https://devdocs.magento.com/guides/v2.4/extension-dev-guide/declarative-schema/migration-commands.html)
