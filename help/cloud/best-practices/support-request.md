---
title: Create an effective support request
description: Learn about ways to create a support ticket to maximize the efficiency of the request.
feature: Best Practices, Customer Service, Support
topic: Commerce
role: Admin, Developer, User
level: Beginner, Intermediate
doc-type: Tutorial
duration: 0
last-substantial-update: 2024-08-23
jira: KT-15165
exl-id: cea62272-c7b9-44f7-9c39-5ad3d9122382
---
# Effective Support Requests

When creating a support ticket, it is important to submit it through the appropriate channels, provide accurate and detailed information about the issue, select the correct organization and contact reason, choose the appropriate product and version, review suggested articles for potential solutions, double-check all the information before submitting, track the ticket's progress and engage in a conversation with the support team, mark the ticket as solved when the issue is resolved, and open a follow-up ticket if further assistance is needed. ​ Remember to submit the ticket through the appropriate channels, provide accurate and detailed information, select the correct organization and contact reason, choose the appropriate product and version, review suggested articles, double-check all information before submitting, track the ticket's progress, engage in conversation with the support team, mark the ticket as solved when the issue is resolved, and open a follow-up ticket if needed. ​

## Include logs or screenshots

There are several logs that are helpful depending on the issue at hand. If possible, find a section of the log and include it as part of the support request. This snippet of the log helps the engineers understand the errors being shown and will expedite the triage process. Remember, every app server has individual logs, and those logs are fed into New Relic as an aggregate.  This means that you can search in one location for all errors instead of reading each application server's individual log files. As a final option, if there is an entry found in New Relic, a screenshot can also be used as additional information and help expedite the process, but having an NRQL statement is preferred.

## Ensure that the time zone is referenced

Ensuring that when people contribute to a support issue, remind them to clarify their time zone when referring to an incident. Referencing a timezone ensures that when the support engineering team is researching the logs and events, they are able to focus on the time frames that are actually relevant. Remember that someone can be many hours ahead or behind the server log times.

## Describe initial triage taken and findings

By discussing and documenting all triage steps taken so far helps the support engineers validate early assumptions. If the supporting triage steps and findings are provided it can expedite the overall process. This will also help reduce duplication of efforts and eventually provide a way to document the findings with a level of validation.

## Links to New Relic reports or provide NRQL statement

Many of the issues for Adobe Commerce are traceable through New Relic. By looking at the New Relic dashboards or custom NRQL statements give you insights to where some issues are originating. Those same dashboards and custom New Relic queries are shareable. By providing those links in the support ticket, the engineers are able to see exactly what the reporter is.

>[!MORELIKETHIS]
> 
> - [Adobe Commerce Help User Guide](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/help-center-guide/magento-help-center-user-guide){target="_blank"}
