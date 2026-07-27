---
title: Bulk Data Migration Tool - Multi-phase Migration
description: Learn how to run a multi-phase migration with the Bulk Data Migration Tool using maintenance mode when your source must stay frozen during production cutover.
feature: Data Import/Export
topic: Migration
role: Developer
doc-type: Technical Video
duration: 211
last-substantial-update: 2026-07-27
jira: KT-22157
---

# Run a multi-phase migration with the Bulk Data Migration Tool

Run a multi-phase migration when your source environment must be frozen during extraction — ideal for production cutovers where new orders can't come in mid-migration. It uses maintenance mode and has five phases that must run in order. If your source can stay live, see the single-phase migration video in this series instead.

## Who is this video for?

* Solutions Architect
* DevOps Engineer
* Backend Developer

## Video content

* One key distinction before starting: `bin/console` commands run against the migration tool itself; `bin/magento maintenance` commands run on your source Commerce server. The tool does not enable or disable maintenance mode for you — that's a manual step.
* Phase one runs while the source is still live — `bin console migration:before-maintenance` checks configuration, initializes the environment, connects to CDMS, registers the migration, runs functional tests, and creates synthetic test data. Do not enable maintenance mode until this phase finishes.
* Phase three is the extraction from a frozen environment — `bin/console migration:during-maintenance` reopens PaaS tunnels if needed, extracts from the source, cleans up staging views, loads into the ACCS target, runs verification, and cleans up test data on the target.

>[!VIDEO](https://video.tv.adobe.com/v/3496413?learn=on)
