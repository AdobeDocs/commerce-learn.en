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

>[!IMPORTANT]
>_You_ _accept_ [_responsibility_](https://www.adobe.com/content/dam/cc/en/trust-center/ungated/whitepapers/experience-cloud/adobe-commerce-shared-responsibility-guide.pdf) _for any adverse effects and associated risks to your Production launch schedule and ongoing site_ _stability, if you fail to use and complete this checklist._

## 1. Pre-Go Live

At least 4 weeks prior to launching your new Adobe Commerce Cloud site, please contact your CTA/CSE and Account Manager to notify them of your **_intention_** to launch.

- Adobe, Developer/SI, Client to review the status of the following checklist.
- Launch date and time window to be confirmed.
- If the launch date or time window changes, please notify your CTA/CSE and Account Manager.

1. [ ] Review our documentation about testing and going live ([Site launch documentation](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/launch/overview.html))
    >[!NOTE]
    >Ensure a comprehensive _"go live readiness plan"_ is fully prepared with your Partner/SI, incorporating all necessary action items. Remember, while the pre-launch checklist emphasizes Adobe's best practices, it _**does not**_ replace the need for your own go-live readiness plan.
2. [ ] [!BADGE Blocker]{type=Negative tooltip="Potential Blocker"}Review the Support Insights (SWAT) Recommendations and Information ([User Guide](https://experienceleague.adobe.com/docs/commerce-operations/tools/site-wide-analysis-tool/intro.html?lang=en))
3. [ ] End user/merchant conducted UAT (User Acceptance Testing), including backend operations.
4. [ ] System integrator team has performed end-to-end UAT on Staging and Production. Refer to the [Experience League Documentation](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/test/staging-and-production.html).
5. [ ] Confirm code deployment and testing in Staging and Production Environments ([Read more](https://devdocs.magento.com/cloud/live/stage-prod-test.html)).
6. [ ] Your production cluster has been upsized permanently to the contracted daily baseline. Speak to your CTA/CSE for more details.

## 2. Current Configurations

1. [ ] Upgrade Adobe Commerce and related packages/services to the [latest version](https://devdocs.magento.com/guides/v2.4/release-notes/bk-release-notes.html)
2. [ ] Review your current configurations and services with your SI/Partner, and [follow the best practices](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/planning/catalog-management).
3. [ ] Review your MySQL/Shared-Files [disk usage](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/storage/manage-disk-space)

## 3. Fastly Configurations

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

## 4. DNS and SSL

1. [ ] [!BADGE Blocker]{type=Negative tooltip="Potential Blocker"}Confirm all required domain names are requested. _(Submit a support ticket in-advance for any added or changed domains)_
2. [ ] [!BADGE Blocker]{type=Negative tooltip="Potential Blocker"}SSL (TLS) certificate has been applied to your domain(s). Read [this article](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/how-to/ssl-tls-certificates-for-magento-commerce-cloud-faq) for more information.
3. [ ] Update DNS [TTL (Time to Live)](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/launch/checklist#to-update-dns-configuration-for-site-launch) value to the minimum possible, for the go live.
4. [ ] Enable Sendgrid SPF and DKIM
   >[!NOTE] 
   > Add the SendGrid CNAME records for each domain to your DNS configuration. Read [SendGrid email service](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/project/sendgrid.html) to see how to change the sender domains and more.

## 5. Database Configurations

Adobe Commerce Cloud employs a MariaDB Galera cluster as the database for both your Staging and Production environments. Galera clusters are instrumental in enhancing performance and scalability. To gain insights into the optimal practices and constraints of Galera cluster replications, we recommend referring to the following articles.
- [MySQL Configurations best practices](https://experienceleague.adobe.com/docs/commerce-operations/implementation-playbook/best-practices/planning/mysql-configuration.html?lang=en)
- Managed Alerts on Adobe Commerce: [MariaDB alerts](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/support-tools/managed-alerts/managed-alerts-on-magento-commerce-mariadb-alerts.html?lang=en)
- Best practices for [database configuration](https://experienceleague.adobe.com/docs/commerce-operations/implementation-playbook/best-practices/planning/database-on-cloud.html?lang=en)
- Deep analysis to [Galera cluster replications and flow-control.](https://experienceleague.adobe.com/docs/commerce-learn/tutorials/backend-development/galera-db-slow-replication.html?lang=en)  

1. [ ] [MYSQL Slave connection](https://experienceleague.adobe.com/docs/commerce-operations/implementation-playbook/best-practices/planning/mysql-configuration.html?lang=en#slave-connections) is recommended for improved performance during high database loads.
2. [ ] Convert the row format from [COMPACT to DYNAMIC](https://experienceleague.adobe.com/docs/commerce-operations/implementation-playbook/best-practices/maintenance/commerce-235-upgrade-prerequisites-mariadb.html?lang=en) (Especially for on-prem to cloud migrations).
3. [ ] Change the database storage engine from [MyISAM to InnoDB](https://experienceleague.adobe.com/docs/commerce-operations/implementation-playbook/best-practices/planning/database-on-cloud.html?lang=en#convert-all-myisam-tables-to-innodb)
4. [ ] Review and optimize database tables exceeding 1 GB in size well-in-advance.
5. [ ] The database schema information is current and up to date. (Refer to [this guide](https://mariadb.com/kb/en/engine-independent-table-statistics/#collecting-statistics-with-the-analyze-table-statement))

## 6. Deployments

1. [ ] Review minification settings for HTML, Javascript, and CSS. (This does not apply to PWA/Headless websites). [Static Content Deployment (SCD) Strategies](https://devdocs.magento.com/cloud/deploy/static-content-deployment.html)
2. [ ] Review the Static Content Deployment (SCD) ideal state to reduce maintenance time during deployments on Production.
3. [ ] Confirm that the utilization of the following cloud variables aligns with their intended purposes. [SCD_MATRIX](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/configure/env/stage/variables-build.html?lang=en#scd_matrix), [SCD_ON_DEMAND](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/configure/env/stage/variables-global.html?lang=en#scd_on_demand) and [SKIP_SCD](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/configure/env/stage/variables-deploy.html?lang=en#skip_scd)

## 7. Testing and Troubleshooting

1. [ ] Test Outgoing Emails. Read more about [Adobe Commerce Cloud - SendGrid Mail functionality](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/project/sendgrid.html).
2. [ ] Any blockers with Adobe?
3. [ ] Perform Load and Stress testing on Production instance before going live and share results with your CTA/CSE.
    >[!NOTE]
    > A [load and stress test serves the purpose](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/test/guidance.html?lang=en#:~:text=A%20load%20test%20can%20help,Scan%20Tool%20for%20your%20sites.) of identifying bottlenecks and uncovering performance issues within the application. It plays a crucial role in managing expectations regarding cluster size and determining the necessary scaling adjustments to meet the business requirements effectively.
    
    >[!IMPORTANT]
    > **_WARNING:_** _When preparing a load test please_ **_do not_** _send out live transaction emails (even to dummy addresses). Sending emails during testing can cause your project to reach the default send limit (12k) configured for SendGrid prior to launch. 
    > 
    > How to disable email communication:
    > Go to _Store > Configuration > Advanced > System > Email Sending Settings_.

4. [ ] Conduct security penetration testing on the production instance as part of our [shared responsibility security model](https://magento.com/trust/shared-responsibility). For PCI (Payment Card Industry) compliance, the customized site requires penetration testing.

## 8. Other Configurations

1. [ ] Switch indexing to _“update on schedule__”,_ except the **_customer_grid_** which remains on “SAVE” (see [Indexing modes](https://devdocs.magento.com/guides/v2.4/extension-dev-guide/indexing.html#m2devgde-indexing-modes)).
2. [ ] Are you using any third-party search engines or extensions?
3. [ ] Confirm that [SEO (Search Engine Optimization) configurations are properly set up](https://experienceleague.adobe.com/docs/commerce-admin/marketing/seo/seo-overview.html?lang=en) to enable indexers/crawlers to scan your website, if relevant.
4. [ ] Add redirects and routes (see [Configure routes](https://devdocs.magento.com/cloud/project/routes.html))
    
    >[!NOTE]
    >Add redirects and routes to the routes.yaml file in the Integration environment and verify the configuration in this environment before deploying to Staging and Production.
    
        ```yaml
        "http://{all}/":
            type: upstream
            upstream: "mymagento:http"
        
        "http://{all}/":
            type: upstream
            upstream: "mymagento:http"
        ```

5. [ ] Ensure XDebug is disabled if enabled during development (see [Configure Xdebug](https://devdocs.magento.com/cloud/howtos/howtos/debug.html)).
6. [ ] Verify that op-cache and other configurations have been accurately updated in the php.ini file ([refer to this sample](https://github.com/magento/magento-cloud/blob/master/php.ini#L41)).
7. [ ] Subscribe to the [**Adobe Commerce status page**](https://status.adobe.com/cloud/experience_cloud#/).
8. [ ] Subscribe to New Relic “[Managed Alerts for Adobe Commerce](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/support-tools/managed-alerts/managed-alerts-for-magento-commerce.html?lang=en)” notification channels to monitor the given performance metrics ([read more](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/monitor/new-relic/new-relic-service.html)).  

## 9. Security

1. [ ] Setup your Adobe Commerce Security Scan
    >[!NOTE]
    > [Adobe Commerce Security Scan is a useful tool](https://experienceleague.adobe.com/docs/commerce-admin/systems/security/security-scan.html) that helps discover outdated software versions, incorrect configuration, and potential malware on your site. Sign up, schedule it to run often, and make sure emails are sent to the right technical security contact.
    > 
    > Complete this task during UAT. If you use the periodic scans option, be sure to schedule scans at low demand times. See the [Security Scan](https://account.magento.com/scanner/index/dashboard/) page in your Adobe Commerce Account. You must log in to Adobe Commerce account to access the Security Scan.

2. [ ] Change default settings for the Adobe Commerce admin
3. [ ] Change the admin password (see [Configuring Admin Security](https://docs.magento.com/user-guide/stores/security-admin.html)).
4. [ ] Change the admin URL (see [Using a custom Admin URL](https://docs.magento.com/user-guide/stores/store-urls-custom-admin.html)).
5. [ ] Remove any users no longer on the project (see [Create and manage users](https://devdocs.magento.com/cloud/project/user-admin.html)).
6. [ ] Passwords for administrators configured (see [Admin Password Requirements](https://docs.magento.com/user-guide/stores/security-admin.html#admin-password-requirements)).
7. [ ] Configure two-factor authentication (see [Two-Factor Authentication](https://devdocs.magento.com/guides/v2.4/security/two-factor-authentication.html)).

## 10. Go Live

When it is time to cutover, please perform the following steps (for more information, see [DNS Configurations](https://devdocs.magento.com/cloud/live/site-launch-checklist.html)):

1. Access your DNS service and update A and CNAME records for each of your domains and hostnames:
   1. Add CNAME record for <www.yourdomain.com>, pointing at prod.magentocloud.map.fastly.net
   2. Set four A records for _yourdomain.com_, pointing at:  
      151.101.1.124  
      151.101.65.124  
      151.101.129.124  
      151.101.193.124
2. Change Adobe Commerce Base URLs to _<www.yourdomain.com>_
3. Wait for the TTL time to pass, then restart web browser.
4. Test your website.

### If you have an issue blocking your go-live:

If you encounter any problems any issues preventing you from launching during your cutover, the fastest method to get proper timely support is to utilize our help desk and open a ticket with the reason “Unable 
to launch my store” and calling a hotline support number (see [the list of Adobe Commerce P1 (Priority 1) hotline numbers](https://support.magento.com/hc/en-us/articles/360042536151)):

- US Toll Free: (+1) 877 282 7436 (Direct to Adobe Commerce P1 hotline)
- US Toll Free: (+1) 800 685 3620 (At first menu, press 7 for Adobe Commerce P1 hotline)
- US Local: (+1) 408 537 8777

## 11. Post Go-Live

Once your site is live, email your CTA (Customer Technical Advisory) and CSM (Customer Success Manager). The CTA will perform the following tasks as soon as the site

is verified to be launched with Fastly enabled and caching:

- Tag the cluster as live and create a support ticket to activate High SLA (Service Level Agreements) monitoring.
- Activate Pingdom checks for uptime monitoring.
- Enable Adobe Commerce Business Intelligence (for Commerce Pro Only). For Commerce Starter please follow our documentation on enabling MBI (Magento Business Intelligence) Essentials for [Adobe Commerce Commerce Starter](https://support.magento.com/hc/en-us/articles/360016504752-How-to-setup-MBI-Essentials-for-Magento-Commerce-Starter).

>[!BEGINSHADEBOX]
> **Merchant / SI (systems integrators)** – Please sign below that you understand that this checklist contains best practices and you 
> understand the importance of completing these for the most successful launch.
> 
> **CTA/CSE** – Sign below that you have reviewed this checklist with your Merchant / SI during your onboarding call. Ensuring launch readiness and managing the site launch is the sole responsibility of the client. By signing this document, the CTA is not assuming responsibility for the success of the launch.
>[!ENDSHADEBOX]
