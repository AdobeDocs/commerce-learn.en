---
title: Learn how the Percona Toolkit pt-query-digest works and why it is used
description: Analyze MySQL queries from slow, general, and binary log files. It can also analyze queries from `SHOW PROCESSLIST` and MySQL protocol data from tcpdump.
kt: 13846
doc-type: video
activity: use
last-substantial-update: 2023-8-28
feature: Backend Development, Tools and External Services, Logs
topic: Commerce, Development
role: Architect, Developer
level: Intermediate
exl-id: 77e91f1b-b3ae-4c6d-bb6d-4fd7ebbb0baf
---
# Percona Toolkit pt-query-digest

Learn why you use the pt-query-digest and some real-world examples to help deepen the reasoning.

## Who is this video for?

- Architects
- Developers
- DevOps

## Video content

- Learn about pt-query-digest usage
- Learn about the benefits and shortcomings of this Percona Toolkit feature
- Understand the results and learn what possible performance steps should be considered

>[!VIDEO](https://video.tv.adobe.com/v/3423480?learn=on)

## Code references

```MYSQL
Be sure to change to match your logs and time frame

$ pt-query-digest mysql-slow.log.7 > mysql-slow.log.7.DIGEST

```

## Useful resources

- [Percona Toolkit](https://docs.percona.com/percona-toolkit/pt-query-digest.html){target="_blank"}
- [Deadlocks in MySQL](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/troubleshooting/database/deadlocks-in-mysql.html){target="_blank"}
