---
title: Bulk Data Migration Tool - Single-phase Migration
description: Learn how to run a single-phase migration with the Bulk Data Migration Tool for dry runs and environments where the source can stay live during extraction.
role: Developer
level: Intermediate
doc-type: Technical Video
topic: Migration
feature: Data Import/Export
duration: 737
last-substantial-update: 2026-07-24
jira: KT-22139
---
# Run a single-phase migration with the Bulk Data Migration Tool

Run a single-phase migration when your source environment can stay live during extraction — ideal for dry runs, and dev or sandbox environments. If you need a frozen source, such as a production cutover where new orders can't come in mid-migration, see the phased migration video in this series instead.

## Who is this video for?

* Solutions Architect
* DevOps Engineer
* Backend Developer

## Video content

* Build the Docker image with `bin console build` — only re-run this if the Dockerfile changes.
* To launch the CDMS CLI container manager, run `bin console start`, then open a shell in the container once to download its dependencies.
* To execute the full ten-step pipeline, run `bin console migration`: check configuration, initialize the environment, open PaaS tunnels, run integration tests, register with CDMS, analyze target schema, generate test data, extract source data, load into ACCS, verify checksums, clean up, and summarize.
* Check the migration summary report — step 8 (data integrity verification) logs failures without halting the pipeline, so a completed run does not guarantee a clean verification.
* This single-phase command is a complete, self-contained pipeline — do not use it as a step inside the maintenance-mode (phased migration) workflow, which has its own dedicated commands.

>[!VIDEO](https://video.tv.adobe.com/v/3496316?learn=on)
