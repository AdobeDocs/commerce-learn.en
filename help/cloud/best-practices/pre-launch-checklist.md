---
title: Adobe Commerce Cloud pre-launch checklist
description: Learn about the Adobe Commerce Cloud pre-launch checklist.
feature: Cloud
topic: Commerce, Architecture, Development
role: Architect, Developer
level: Intermediate
doc-type: Tutorial
duration: 0
last-substantial-update: 2024-04-17
jira: KT-15180
kt: 15180
---

# Commerce Cloud Pre-Launch Checklist

The following is a synopsis of the Adobe Commerce [Site launch documentation](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/launch/overview){target="_blank"}.

This checklist aims to assist in planning and executing a successful launch of the Adobe Commerce Cloud site. Collaborate with your system integrator for Adobe Commerce Cloud to ensure all configuration tasks and checklist items are completed and verified. If you encounter difficulties with any checklist items or have questions, please reach out to the designated Customer Technical Advisor or Customer Success Engineer. If your account does not have an assigned CTA/CSE, you may create a support ticket for assistance.

If you have a CTA/CSE assigned, we recommend contacting them and the Account Manager at least 4 weeks prior to launching the new Adobe Commerce Cloud site to notify them of your **intention** to launch.

- Some checks are highlighted with [!BADGE Blocker]{type=caution tooltip="Potential Blocker"} as they may potentially block your go-live if not carefully reviewed.
- Ensure to collaborate with your developer or system integration partner to align with your implementation approach.

>[!IMPORTANT]
> You accept [responsibility](https://www.adobe.com/content/dam/cc/en/trust-center/ungated/whitepapers/experience-cloud/adobe-commerce-shared-responsibility-guide.pdf){target="_blank"} for any adverse effects and associated risks to the production launch schedule and ongoing site stability, if you fail to use and complete this checklist.

## 1. Pre-Go Live

1. Review the documentation about testing and going live ([Site launch documentation](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/launch/overview){target="_blank"})
    >[!NOTE]
    >Ensure a comprehensive _"go live readiness plan"_ is fully prepared with your Partner/SI, incorporating all necessary action items. Remember, while the pre-launch checklist emphasizes Adobe's best practices, it _**does not**_ replace the need for your own go-live readiness plan.

2. [!BADGE Blocker]{type=caution tooltip="Potential Blocker"} Review the Support Insights (SWAT) Recommendations and Information ([User Guide](https://experienceleague.adobe.com/en/docs/commerce-operations/tools/site-wide-analysis-tool/intro){target="_blank"})
3. End user/merchant conducted UAT (User Acceptance Testing), including backend operations.
4. System integrator team has performed end-to-end UAT on Staging and Production. Refer to the [Experience League Documentation](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/test/staging-and-production){target="_blank"}.
5. Confirm code deployment and testing in Staging and Production Environments ([Read more](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/test/staging-and-production){target="_blank"}).
6. The production cluster has been upsized permanently to the contracted daily baseline. Speak to the assigned CTA/CSE for more details, or raise a support ticket.

## 2. Current Configurations

1. Upgrade Adobe Commerce and related packages/services to the [latest version](https://experienceleague.adobe.com/en/docs/commerce-operations/release/notes/overview){target="_blank"}
2. Review the current configurations and services with your SI/Partner, and [follow the best practices](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/planning/catalog-management){target="_blank"}.
3. Review the MySQL/Shared-Files [disk usage](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/storage/manage-disk-space){target="_blank"}

## 3. Fastly Configurations

1. [!BADGE Blocker]{type=caution tooltip="Potential Blocker"} Make sure that caching is working ([Full-Page Cache](https://developer.adobe.com/commerce/frontend-core/guide/caching/){target="_blank"} or [GraphQL caching](https://developer.adobe.com/commerce/webapi/graphql/usage/caching/){target="_blank"}). Read the [Fastly set up guide](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/cdn/fastly){target="_blank"}.
2. Use GET method for GraphQL queries on PWA/Headless websites when applicable. 
    >[!NOTE] 
    > Only the queries submitted with an HTTP GET operation can be cached (if applicable). [POST queries cannot be cached](https://developer.adobe.com/commerce/webapi/graphql/usage/caching/){target="_blank"}.

3. Ensure that Fastly Image Optimization is enabled ([See Fastly Image Optimisation](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/cdn/fastly-image-optimization){target="_blank"})
4. Verify that the correct shield location is configured ([Configure cache, backends and origin shielding](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/cdn/setup-fastly/fastly-custom-cache-configuration){target="_blank"}).
5. Web Application Firewall (**WAF**) is working. (See [Troubleshooting blocked requests](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/cdn/fastly-waf-service){target="_blank"}, if any, and limitations)
6. Update the Fastly [“Ignored URL Parameters”](https://github.com/iancassidyweb/magento2/commit/68fdecfcd26c957382b8d68b64887e0a83298524){target="_blank"} list in the admin panel to enhance cache performance.
    >[!NOTE] 
    > In the Fastly configuration under _Admin > Stores > Configurations > System > Full Page Cache > Fastly Configuration > Advanced Configuration > Ignored URL Parameters (Global)_, you can find a comma-separated list of parameters that Fastly should disregard when searching for cached pages. Please make sure to re-upload the VCL after modifying this list

## 4. DNS and SSL

1. [!BADGE Blocker]{type=caution tooltip="Potential Blocker"} Confirm all required domain names are requested. _(Submit a support ticket in-advance for any added or changed domains)_
2. [!BADGE Blocker]{type=caution tooltip="Potential Blocker"} SSL (TLS) certificate has been applied to the domain(s). Read [this article](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/how-to/ssl-tls-certificates-for-magento-commerce-cloud-faq){target="_blank"} for more information.
3. Update DNS [TTL (Time to Live)](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/launch/checklist#to-update-dns-configuration-for-site-launch){target="_blank"} value to the minimum possible, for the go live.
4. Enable Sendgrid SPF and DKIM
   >[!NOTE] 
   > Add the SendGrid CNAME records for each domain to the DNS configuration. Read [SendGrid email service](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/project/sendgrid){target="_blank"} to see how to change the sender domains and more.

## 5. Database Configurations

Adobe Commerce Cloud employs a MariaDB Galera cluster as the database for both the Staging and Production environments. Galera clusters are instrumental in enhancing performance and scalability. To gain insights into the optimal practices and constraints of Galera cluster replications, we recommend referring to the following articles.
- [MySQL Configurations best practices](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/planning/mysql-configuration){target="_blank"}
- Managed Alerts on Adobe Commerce: [MariaDB alerts](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/support-tools/managed-alerts/managed-alerts-on-magento-commerce-mariadb-alerts){target="_blank"}
- Best practices for [database configuration](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/planning/database-on-cloud){target="_blank"}
- Deep analysis to [Galera cluster replications and flow-control.](https://experienceleague.adobe.com/en/docs/commerce-learn/tutorials/backend-development/galera-db-slow-replication){target="_blank"}  

1. [MYSQL Slave connection](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/planning/mysql-configuration#slave-connections){target="_blank"} is recommended for improved performance during high database loads.
2. Ensure that the row format for all database tables is set to [DYNAMIC instead of COMPACT](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/maintenance/mariadb-upgrade#convert-database-table-storage-format){target="_blank"} (Especially for on-prem to cloud migrations).
3. Change the database storage engine from [MyISAM to InnoDB](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/planning/database-on-cloud#convert-all-myisam-tables-to-innodb){target="_blank"} for all the tables.
4. Review and optimize database tables exceeding 1 GB in size well-in-advance.
5. The database schema information is current and up to date. (Refer to [this guide](https://mariadb.com/kb/en/engine-independent-table-statistics/#collecting-statistics-with-the-analyze-table-statement){target="_blank"}).

## 6. Deployments

1. Review the Static Content Deployment (SCD) ideal state to reduce maintenance time during deployments on Production. Review [Static Content Deployment (SCD) Strategies](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/deploy/static-content){target="_blank"} and [Store configuration management](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/configure-store/store-settings){target="_blank"} guide.
2. Review minification settings for HTML, Javascript, and CSS. (This does not apply to PWA/Headless websites).
3. Confirm that the utilization of the following cloud variables aligns with their intended purposes. ([SCD_MATRIX](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/configure/env/stage/variables-build#scd_matrix){target="_blank"}, [SCD_ON_DEMAND](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/configure/env/stage/variables-global#scd_on_demand){target="_blank"} and [SKIP_SCD](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/configure/env/stage/variables-deploy#skip_scd){target="_blank"})

## 7. Testing and Troubleshooting

1. Test the outgoing transactional emails. Read more about [Adobe Commerce Cloud - SendGrid Mail functionality](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/project/sendgrid){target="_blank"}.
2. [!BADGE Blocker]{type=caution tooltip="Potential Blocker"} Any blockers with Adobe?
3. [!BADGE Blocker]{type=caution tooltip="Potential Blocker"} Perform Load and Stress testing on Production instance before going live and share results with the assigned CTA/CSE.
    >[!NOTE]
    > A [load and stress test serves the purpose](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/test/guidance#:~:text=A%20load%20test%20can%20help,Scan%20Tool%20for%20your%20sites.){target="_blank"} of identifying bottlenecks and uncovering performance issues within the application. It plays a crucial role in managing expectations regarding cluster size and determining the necessary scaling adjustments to meet the business requirements effectively.
    
    >[!IMPORTANT]
    > **_WARNING:_** When preparing a load test please_ **_do not_** send out live transaction emails (even to dummy addresses). Sending emails during testing can cause the project to reach the default send limit (12k) configured for SendGrid prior to launch. 
    > 
    > - How to disable email communication:
    >   Go to _Store > Configuration > Advanced > System > Email Sending Settings_.

4. Conduct security penetration testing on the production instance as part of the [shared responsibility security model](https://business.adobe.com/products/magento/secure-ecommerce.html){target="_blank"}. For PCI (Payment Card Industry) compliance, the customized site requires penetration testing.

## 8. Other Configurations

1. Switch indexing to _“update on schedule_”, except the **_customer_grid_** which remains on “SAVE” (see [Indexing modes](https://developer.adobe.com/commerce/php/development/components/indexing/#indexing-modes){target="_blank"}).
2. Are you using any third-party search engines or extensions?
3. Confirm that [SEO (Search Engine Optimization) configurations are properly set up](https://experienceleague.adobe.com/en/docs/commerce-admin/marketing/seo/seo-overview){target="_blank"} to enable indexers/crawlers to scan the website, if relevant.
4. Add redirects and routes (see [Configure routes](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/configure/routes/routes-yaml){target="_blank"})
    >[!NOTE]
    >Add redirects and routes to the routes.yaml file in the Integration environment and verify the configuration in this environment before deploying to Staging and Production.
   
        "http://{all}/":
            type: upstream
            upstream: "mymagento:http"
        
        "http://{all}/":
            type: upstream
            upstream: "mymagento:http"

5. Ensure XDebug is disabled if enabled during development (see [Configure Xdebug](https://developer.adobe.com/commerce/cloud-tools/docker/test/configure-xdebug/){target="_blank"}).
6. Verify that op-cache and other configurations have been accurately updated in the php.ini file ([refer to this sample](https://github.com/magento/magento-cloud/blob/master/php.ini#L41){target="_blank"}).
7. Subscribe to the [**Adobe Commerce status page**](https://status.adobe.com/cloud/experience_cloud#/){target="_blank"}.
8. Subscribe to New Relic “[Managed Alerts for Adobe Commerce](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/support-tools/managed-alerts/managed-alerts-for-magento-commerce){target="_blank"}” notification channels to monitor the given performance metrics ([read more](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/monitor/new-relic/new-relic-service){target="_blank"}).  

## 9. Security

1. Setup the Adobe Commerce Security Scan
    >[!NOTE]
    > [Adobe Commerce Security Scan is a useful tool](https://experienceleague.adobe.com/en/docs/commerce-admin/systems/security/security-scan){target="_blank"} that helps discover outdated software versions, incorrect configuration, and potential malware on the site. Sign up, schedule it to run often, and make sure emails are sent to the right technical security contact.
    > 
    > Complete this task during UAT. If you use the periodic scans option, be sure to schedule scans at low demand times. See the [Security Scan](https://account.magento.com/scanner/index/dashboard/){target="_blank"} page in the Adobe Commerce Account. You must log in to Adobe Commerce account to access the Security Scan.

2. Change default settings for the Adobe Commerce Admin.
3. Change the admin password (see [Configuring Admin Security](https://experienceleague.adobe.com/en/docs/commerce-admin/systems/security/security-admin){target="_blank"}).
4. Change the admin URL (see [Using a custom Admin URL](https://experienceleague.adobe.com/en/docs/commerce-admin/stores-sales/site-store/store-urls#use-a-custom-admin-url){target="_blank"}).
5. Remove any users no longer on the project (see [Create and manage users](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/project/user-access){target="_blank"}).
6. Passwords for administrators configured (see [Admin Password Requirements](https://experienceleague.adobe.com/en/docs/commerce-admin/systems/security/security-admin){target="_blank"}).
7. Configure two-factor authentication (see [Two-Factor Authentication](https://developer.adobe.com/commerce/testing/functional-testing-framework/two-factor-authentication/){target="_blank"}).

## 10. Go Live

When it is time to cutover, please perform the following steps (for more information, see [DNS Configurations](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/launch/checklist){target="_blank"}):

1. Access your DNS service and update A and CNAME records for each of your domains and hostnames:
   1. Add CNAME record for _<<www.yourdomain.com>>_, pointing at **prod.magentocloud.map.fastly.net**
   2. Set four A records for _<<yourdomain.com>>_, pointing at:  
      151.101.1.124  
      151.101.65.124  
      151.101.129.124  
      151.101.193.124
2. Change Adobe Commerce Base URLs to _<<www.yourdomain.com>>_
3. Wait for the TTL time to pass, then restart web browser.
4. Test the website.

### If you have an issue blocking the go-live:

If you encounter any problems any issues preventing you from launching during the cutover, the fastest method to get proper timely support is to utilize the help desk and open a ticket with the reason “Unable to launch my store” and calling a hotline support number (see [the list of Adobe Commerce P1 (Priority 1) hotline numbers](https://support.magento.com/hc/en-us/articles/360042536151){target="_blank"}):

- US Toll Free: (+1) 877 282 7436 (Direct to Adobe Commerce P1 hotline)
- US Toll Free: (+1) 800 685 3620 (At first menu, press 7 for Adobe Commerce P1 hotline)
- US Local: (+1) 408 537 8777

## 11. Post Go-Live

Once the site is live, email the assigned CTA (Customer Technical Advisory), CSE (Customer Success Engineer) and AM (Account Manager). The CTA/CSE will perform the following tasks as soon as the site is verified to be launched with Fastly enabled and caching:

- Tag the cluster as live and create a support ticket to activate High SLA (Service Level Agreements) monitoring.
- Activate Pingdom checks for uptime monitoring.

However, if you do not have an account manager assigned to the project, you can create a support ticket asking for High SLA monitoring to be enabled once the site has gone live.


>[!MORELIKETHIS]
> 
> - [Launch Readiness Overview - Implementation Playbook](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/launch/overview){target="_blank"}
> - [Launch Checklist - User Guide](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/launch/checklist){target="_blank"}
> - [Prelaunch Checklist - Site Manager/Commerce Admin's Guide](https://experienceleague.adobe.com/en/docs/commerce-admin/start/setup/prelaunch-checklist){target="_blank"}
> - [Shared responsibility security model](https://experienceleague.adobe.com/en/docs/commerce-operations/security-and-compliance/shared-responsibility){target="_blank"}


