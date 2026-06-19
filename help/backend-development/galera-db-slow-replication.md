---
title: Diagnose Galera DB replication in MySQL slow query logs
description: Learn how Galera DB's replication design slows secondary database syncs, how to identify these events in MySQL slow query logs, and ways to minimize the impact.
doc-type: Technical Video
duration: 452
last-substantial-update: 2023-07-18
feature: Backend Development, Logs, Services
topic: Commerce, Development
role: Developer
level: Intermediate
jira: KT-13635
exl-id: 4a8a2df1-8cac-4bd9-851f-0eaae011b76c
TQID: https://experienceleague.adobe.com/NYapiIjnRv5RAS1glm8do16M4jUPmbgfVCs6ICQwbUc
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
---
# Learn about Galera DB replication and related MySQL slow queries

Galera clusters help with performance and scalability. When considering replica databases, it is important to understand that the way the data replication happens is different than on the primary. The primary database can perform bulk operations. When the replication happens for all the replica databases, they do actions one at a time. For example, if you have 67,000,000 items in a delete, on the replica databases each one happens one at a time. When reviewing the MySQL slow query logs, you find this action can take a long time. The fact that the replica databases are performing operations sequentially is a reason for things not to be in sync, and performance impacts can be detected.

To help the replica databases keep in sync with the primary, batch your large operations when possible. By doing things in batch, it allows the actions to be executed in a timely manner and performance impacts are kept down to a minimum.

## Intended audience

* Architects
* Developers
* DevOps

## Video content

* Galera replication to replica database
* Learn about flow control
* Finding thread numbers in mysql slow query logs
* Bulk executions only happen on the primary. Replications happen 1 at a time
* To help the replication keep up with the primary, batch your large commits.

>[!VIDEO](https://video.tv.adobe.com/v/3421688?learn=on)

## Useful resources

* [Galera Cluster](https://mariadb.com/products/enterprise/galera-cluster/)
