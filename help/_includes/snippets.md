---
title: Edition Banners
description: Reused visual elements to note feature or pages applying to a specific edition
---
# Edition Banners

## EE only feature {#ee-feature}

<table style="border:1px solid red">
<tr><td><img alt="Adobe Commerce feature" src="../assets/adobe-logo.svg" width="20" height="20" /> Exclusive feature only in Adobe Commerce (<a href="https://experienceleague.adobe.com/docs/commerce-admin/user-guides/home.html#product-editions">Learn more</a>)</td></tr>
</table>

## B2B only feature {#b2b-feature}

<table style="border:1px solid green">
<tr><td><img alt="Adobe Commerce feature" src="../assets/b2b.svg" width="20" height="20" /> Exclusive feature available only with <a href="https://experienceleague.adobe.com/docs/commerce-admin/b2b/guide-overview.html">B2B for Adobe Commerce</a></td></tr>
</table>

## 400 issues {#avoid-400-error}

>[!CAUTION]
>
>When performing API calls, ensure that some sort of searchCriteria is used. You might also consider using pagination. If the result from Adobe Commerce is too large, the Adobe Developer App Builder capacity may be met and cause an unexpected end to the file. The result is a malformed response result as a 400 error.  
> For example, suppose There is a need to request all the current products from Adobe Commerce. The resulting URL would resemble `{{base_url}}rest/V1/products?searchCriteria=all`. Depending on the size of the catalog the returned, the json may be too large for App Builder to consume. Instead use pagination and make a few requests to avoid `Response is not valid 'message/http'.`

## PaaS and Commere Cloud only {#only-for-on-prem-commerce-cloud}

| On-Prem | Adobe Commerce Cloud | Adobe Commerce as a Cloud Service | Aobe Commerce Optimizer |
| --- | --- | --- | --- |
| Yes | Yes | >[!BEGINSHADEBOX]No>[!ENDSHADEBOX] | >[!BEGINSHADEBOX]No>[!ENDSHADEBOX] |
