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
<tr><td><img alt="Adobe Commerce feature" src="../assets/b2b.svg" width="20" height="20" /> Exclusive feature available only with <a href="https://experienceleague.adobe.com/docs/commerce-admin/user-guides/home.html#product-editions">B2B for Adobe Commerce</a></td></tr>
</table>

## 400 issues {#avoid-400-error}

>[!CAUTION]
>
>When performing API calls, ensure that pagination is used. If the result from Adobe Commerce is too large, the Adobe Developer App Builder capacity may be met and cause an unexpected end to the file. This will result in a malformed response which will be interpreted as a 400 error.  
> Real life example. There is a need to request all the current products from Adobe Commerce.  The resulting URL would resemble `{{base_url}}rest/V1/products?searchCriteria=all`. Depending on the size of the catalog the returned json will be too large for App Builder to consume. Instead use pagination and make a few request to avoid `Response is not valid 'message/http'.`