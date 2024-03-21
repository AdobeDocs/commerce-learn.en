---
title: Adobe Commerce Cloud pre launch checklist
description: Learn about the Adobe Commerce Cloud pre-launch checklist.
feature: Cloud
topic: Commerce, Architecture, Development
role: Architect, Developer
level: Intermediate
doc-type: Tutorial
duration: 0
last-substantial-update: 2024-03-19
jira: KT-15180
kt: 15180
---

# Commerce Cloud Pre-Launch Checklist

>[!BEGINSHADEBOX]
> _The following is a synopsis of_ _our_ [_Site launch documentation_](https://devdocs.magento.com/cloud/live/live.html)_._
> 
> _We provide the following checklist to help you plan and execute a successful Adobe Commerce Cloud site launch. Work with the system integrator for your Adobe Commerce Cloud to complete and verify all configuration tasks and other work covered by the checklist. If you are unable to complete any of the checklist items or have questions, contact your assigned Customer Technical Advisor/Customer Success Engineer._
>
>[!ENDSHADEBOX]

> [!IMPORTANT]
> _You_ _accept_ [_responsibility_](https://www.adobe.com/content/dam/cc/en/trust-center/ungated/whitepapers/experience-cloud/adobe-commerce-shared-responsibility-guide.pdf) _for any adverse effects and associated risks to your Production launch schedule and ongoing site_ _stability, if you fail to use and complete this checklist._

# 1. Pre-Go Live
At least 4 weeks prior to launching your new Adobe Commerce Cloud site, please contact your CTA/CSE and Account Manager to notify them of your **_intention_** to launch.

- Adobe, Developer/SI, Client to review the status of the following checklist.
- Launch date and time window to be confirmed.
- If the launch date or time window changes, please notify your CTA/CSE and Account Manager.

1. [ ] Review our documentation about testing and going live ([Site launch documentation](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/launch/overview.html))
    >[!NOTE]
    > Ensure a comprehensive _"go live readiness plan"_ is fully prepared with your Partner/SI, incorporating all necessary action items. Remember, while the pre-launch checklist emphasizes Adobe's best practices, it _**does not**_ replace the need for your own go-live readiness plan.
2. [ ] [!BADGE Blocker]{type=Negative tooltip="Potential Blocker"}Review the Support Insights (SWAT) Recommendations and Information ([User Guide](https://experienceleague.adobe.com/docs/commerce-operations/tools/site-wide-analysis-tool/intro.html?lang=en))
3. [ ] End user/merchant conducted UAT (User Acceptance Testing), including backend operations.
4. [ ] System integrator team has performed end-to-end UAT on Staging and Production. Refer to the [Experience League Documentation](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/test/staging-and-production.html).
5. [ ] Confirm code deployment and testing in Staging and Production Environments ([Read more](https://devdocs.magento.com/cloud/live/stage-prod-test.html)).
6. [ ] Your production cluster has been upsized permanently to the contracted daily baseline. Speak to your CTA/CSE for more details.

# 2. Current Configurations
1. [ ] Upgrade Adobe Commerce and related packages/services to the [latest version](https://devdocs.magento.com/guides/v2.4/release-notes/bk-release-notes.html)
2. [ ] Review your current configurations and services with your SI/Partner, and [follow the best practices](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/planning/catalog-management).
3. [ ] Review your MySQL/Shared-Files [disk usage](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/storage/manage-disk-space)

# 3. Fastly Configurations
1. [ ] [!BADGE Blocker]{type=Negative tooltip="Potential Blocker"}Make sure that caching is working ([Full-Page Cache](https://developer.adobe.com/commerce/frontend-core/guide/caching/) or [GraphQL caching](https://developer.adobe.com/commerce/webapi/graphql/usage/caching/)). Read the [Fastly set up guide](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/cdn/fastly.html).
2. [ ] Use GET method for GraphQL queries on PWA/Headless websites when applicable. 
    >[!NOTE] 
    > Only the queries submitted with an HTTP GET operation can be cached (if applicable). [POST queries cannot be cached](https://developer.adobe.com/commerce/webapi/graphql/usage/caching/).
3. [ ] Ensure that Fastly Image Optimization is enabled ([See Fastly Image Optimisation](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/cdn/fastly-image-optimization.html))
4. [ ] Verify that the correct shield location is configured ([Configure cache, backends and origin shielding](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/cdn/setup-fastly/fastly-custom-cache-configuration.html)
5. [ ] Web Application Firewall (**WAF**) is working. (See [Troubleshooting blocked requests](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/cdn/fastly-waf-service.html?lang=en), if any, and limitations)
6. [ ] Update the Fastly [“Ignored URL Parameters”](https://github.com/iancassidyweb/magento2/commit/68fdecfcd26c957382b8d68b64887e0a83298524) list in the admin panel to enhance cache performance.
    >[!NOTE] 
    > In the Fastly configuration under _Admin > Stores > Configurations > System > Full Page Cache > Fastly Configuration > Advanced Configuration > Ignored URL Parameters (Global)_, you can find a comma-separated list of parameters that Fastly should disregard when searching for cached pages. Please make sure to re-upload the VCL after modifying this list

# 4. DNS and SSL
1. [ ] [!BADGE Blocker]{type=Negative tooltip="Potential Blocker"}Confirm all required domain names are requested. _(Submit a support ticket in-advance for any added or changed domains)_
2. [ ] [!BADGE Blocker]{type=Negative tooltip="Potential Blocker"}SSL (TLS) certificate has been applied to your domain(s). Read [this article](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/how-to/ssl-tls-certificates-for-magento-commerce-cloud-faq) for more information.
3. [ ] Update DNS [TTL (Time to Live)](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/launch/checklist#to-update-dns-configuration-for-site-launch) value to the minimum possible, for the go live.
4. [ ] Enable Sendgrid SPF and DKIM
   >[!NOTE] 
   > Add the SendGrid CNAME records for each domain to your DNS configuration. Read [SendGrid email service](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/project/sendgrid.html) to see how to change the sender domains and more.

# 5. Database Configurations
>[!NOTE] Adobe Commerce Cloud employs a MariaDB Galera cluster as the database for both your Staging and Production environments. Galera clusters are instrumental in enhancing performance and scalability. To gain insights into the optimal practices and constraints of Galera cluster replications, we recommend referring to the following articles.
> - [MySQL Configurations best practices](https://experienceleague.adobe.com/docs/commerce-operations/implementation-playbook/best-practices/planning/mysql-configuration.html?lang=en)
> - Managed Alerts on Adobe Commerce: [MariaDB alerts](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/support-tools/managed-alerts/managed-alerts-on-magento-commerce-mariadb-alerts.html?lang=en)
> - Best practices for [database configuration](https://experienceleague.adobe.com/docs/commerce-operations/implementation-playbook/best-practices/planning/database-on-cloud.html?lang=en)
> - Deep analysis to [Galera cluster replications and flow-control.](https://experienceleague.adobe.com/docs/commerce-learn/tutorials/backend-development/galera-db-slow-replication.html?lang=en)  

1. [ ] [MYSQL Slave connection](https://experienceleague.adobe.com/docs/commerce-operations/implementation-playbook/best-practices/planning/mysql-configuration.html?lang=en#slave-connections) is recommended for improved performance during high database loads.
2. [ ] Convert the row format from [COMPACT to DYNAMIC](https://experienceleague.adobe.com/docs/commerce-operations/implementation-playbook/best-practices/maintenance/commerce-235-upgrade-prerequisites-mariadb.html?lang=en) (Especially for on-prem to cloud migrations).
3. [ ] Change the database storage engine from [MyISAM to InnoDB](https://experienceleague.adobe.com/docs/commerce-operations/implementation-playbook/best-practices/planning/database-on-cloud.html?lang=en#convert-all-myisam-tables-to-innodb)
4. [ ] Review and optimize database tables exceeding 1 GB in size well-in-advance.
5. [ ] The database schema information is current and up to date. (Refer to [this guide](https://mariadb.com/kb/en/engine-independent-table-statistics/#collecting-statistics-with-the-analyze-table-statement))

