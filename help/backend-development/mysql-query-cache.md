---
title: Learn how mysql query caching
description: Sometimes mysql queries get backed up waiting for a lock. This tutorial explains what is query caching and some recommendations for settings if you have issues.
kt: 13690
doc-type: video
activity: use
last-substantial-update: 2023-7-27
feature: Backend Development, Cache, Logs
topic: Commerce, Development
role: Architect, Developer
level: Intermediate
exl-id: 8d3b0ec2-e80c-4457-b924-69e8b8cedf03
---
# Learn about mysql query caching

Learn what MySQL query cache is and some basic understanding for how it works. Learn how to detect an issue with mysql query caching, by finding "waiting for query cache lock" appearing in a high volume in the mysql slow query logs.

## Who is this video for?

- Architects
- Developers
- DevOps

## Video content

- Learn about query caching
- How to detect if your query cache settings may be an issue by finding "waiting for query cache lock"
- See how the SQL is saved and used in finding a matching query cache
- Some tips on configuration settings

>[!VIDEO](https://video.tv.adobe.com/v/3422015?learn=on)

## Useful resources

- [General MySQL guidelines](https://experienceleague.adobe.com/docs/commerce-operations/installation-guide/prerequisites/database-server/mysql.html?lang=en){target="_blank"}
- [Deadlocks in MySQL](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/troubleshooting/database/deadlocks-in-mysql.html){target="_blank"}
- [Galera replication and slow queries](https://experienceleague.adobe.com/docs/commerce-learn/tutorials/backend-development/galera-db-slow-replication.html){target="_blank"}
