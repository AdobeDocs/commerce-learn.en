---
title: Analyze MySQL queries with Percona Toolkit pt-query-digest
description: Learn how to use pt-query-digest to analyze MySQL queries from slow, general, and binary log files, SHOW PROCESSLIST, and MySQL protocol data from tcpdump.
doc-type: Technical Video
duration: 506
last-substantial-update: 2023-08-28
feature: Backend Development, Tools and External Services, Logs
topic: Commerce, Development
role: Developer
level: Intermediate
jira: KT-13846
exl-id: 77e91f1b-b3ae-4c6d-bb6d-4fd7ebbb0baf
TQID: https://experienceleague.adobe.com/lh-fBjlhZO6W-K08KNb-KaG-N2slLZVpNOSg6LAp0n8
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: bd989d82-1e15-4534-88db-f1f51dd77ffa
    internal-label: Accounts
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
---
# Percona Toolkit pt-query-digest

Learn why to use pt-query-digest and some practical examples to help improve the analysis.

## Intended audience

* Architects
* Developers
* DevOps

## Video content

* Learn about pt-query-digest usage
* Learn about the benefits and shortcomings of this Percona Toolkit feature
* Understand the results and learn what possible performance steps should be considered

>[!VIDEO](https://video.tv.adobe.com/v/3423480?learn=on)

## Code references

```MYSQL
Be sure to change to match your logs and time frame

$ pt-query-digest mysql-slow.log.7 > mysql-slow.log.7.DIGEST

```

## Useful resources

* [Percona Toolkit](https://docs.percona.com/percona-toolkit/pt-query-digest.html){target="_blank"}
