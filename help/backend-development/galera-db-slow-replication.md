---
title: Learn how to find slow queries in mysql slow query logs and why the Galera DB replication design method may be the reason
description: Galera DB has a design method that makes the replication of data to secondary databases take longer than the primary. Learn how to find these events in mysql slow query log, and the underlying reason why this happens, and perhaps how to prevent them in the future.
kt: 13635
doc-type: video
activity: use
last-substantial-update: 2023-7-18
feature: Backend Development, Logs, Services
topic: Commerce, Development
role: Architect, Developer
level: Intermediate

---
# Learn about Galera DB replication and related MySQL slow queries

Galera clusters helps with performance and scalability. When considering secondary databases it is important to understand the way the data replication happens is different than on the primary.  The primary database can perform bulk operations. When the replication happens for all the secondary databases, they do actions one at a time. For example, if you have 67,000,000 items in a delete, on the secondary databases each one happens one at a time. When reviewing the Mysql slow query logs, you will find this can take a very long time. Because the secondary databases are performing things one at a time, is a reason for things to not be in sync and performance impacts can be detected.

As a solution, if possible, batch your large operations to help the secondary databases keep in sync with the primary.  This will allow the actions to be executed in a timely manner and performance impacts will be kept down to a minimum.

## Who is this video for?

- Architects
- Developers

## Video content

- Galera replication to secondary database
- Learn about flow control
- Finding thread numbers in mysql slow query logs
- Bulk executions only happen on the primary. Replications happen 1 at a time
- Batch your large commits to help the replication keep up with the primary

>[!VIDEO](https://video.tv.adobe.com/v/3421688?learn=on)

## Useful resources

- [Galera Cluster](https://galeracluster.com/)
