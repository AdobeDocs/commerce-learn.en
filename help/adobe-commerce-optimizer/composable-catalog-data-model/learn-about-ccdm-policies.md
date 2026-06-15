---
title: Learn About CCDM Policies in Composable Catalog Data Model
description: Learn how STATIC and TRIGGER policies in the Adobe Composable Catalog Data Model control product visibility across catalog views without rebuilding the catalog.
feature: Saas, Storefront
topic: Commerce
role: Developer
level: Beginner
doc-type: Tutorial
duration: 349
last-substantial-update: 2026-05-21
jira: KT-21258
---
# Policies in the Adobe Composable Catalog Data Model

If a **catalog view** is the lens that shapes what shoppers see from a unified base catalog, **policies** are what that lens is made of. This tutorial explains what a policy is, how **STATIC** and **TRIGGER** policies work together in the **Carvelo Automobiles** demonstration scenario, and why updating a policy takes effect immediately—without rebuilding the catalog.

## Who is this video for?

* Commerce solution architects and developers who configure catalog views and merchandising rules on Adobe Commerce Optimizer

## Video content

* Policies as data access filters on product attributes
* How multiple policies combine in the Celport catalog view (brands and part categories)
* STATIC policies for permanent business rules
* TRIGGER policies activated by API request headers (for example `AC-Policy-Brand`)
* Updating policies in day-to-day operations with no catalog rebuild

>[!VIDEO](https://video.tv.adobe.com/v/3491413?learn=on)

A **policy** is a **data access filter**. It inspects product attributes and applies rules that determine which products a catalog view may expose. Policies sit on top of the shared composable catalog—they do not duplicate catalog data.

## STATIC policies

A **STATIC** policy is **always on**. It enforces permanent business rules regardless of shopper behavior or session state.

In the Celport scenario, STATIC rules include:

* Celport will only sell **Bolt** and **Cruz** brands.
* Celport will only show **brakes** and **suspension** parts.

These rules never switch off. STATIC policies are where **licensing agreements**, **territorial restrictions**, and **brand permissions** live. Set them once, and Adobe Commerce Optimizer enforces them automatically on every request.

## TRIGGER policies

Policies with a value source of **TRIGGER** are sometimes called **exclusive policies**. The catalog view runs that policy **only when the trigger is specified** in the header of the API call.

For example, an Experience Delivery Services (EDS) storefront might offer a dropdown with **All Brands**, **Aurora**, **Bolt**, and **Cruz**:

* On the initial page view, nothing is selected, so no extra brand header is sent.
* When the shopper selects **Bolt**, the underlying API sets the `AC-Policy-Brand` header to `Bolt`.
* When the shopper selects **Cruz**, the same header is set to `Cruz`.

The catalog view applies the TRIGGER policy only when that header is present, which supports interactive filtering without changing your permanent STATIC rules.

## STATIC and TRIGGER together

**STATIC** policies handle permanent rules. **TRIGGER** policies handle interactive ones. Used together on a single catalog view, they provide both **compliance** and **flexibility**—fixed assortment boundaries plus shopper-driven refinement.

## Update policies without rebuilding the catalog

For day-to-day operations, policy changes are immediate. Suppose Celport's licensing agreement now allows **tires** as well as brakes and suspension:

1. Open the relevant policy.
1. Add **tires** to the values list.
1. Save.

That change is **live immediately**. There is no catalog rebuild, re-deployment, or wait time. The next request to the Celport storefront reflects the update.

Policies are lightweight filters on a **shared catalog**, not rules baked into separate catalog copies. **Change the rule, not the data.**

## Related Content

* [Why the composable catalog data model exists](./why-ccdm-exists.md)
* [Learn about Catalog Views](./learn-about-the-ccdm-feature-catalog-views.md)
* [Catalog Views for Merchandising Services](https://experienceleague.adobe.com/en/docs/commerce/optimizer/setup/catalog-view){target="_blank"}
* [[!DNL Adobe Commerce Optimizer] Guide](https://experienceleague.adobe.com/en/docs/commerce/optimizer/overview){target="_blank"}
* [Getting started with Merchandising API](https://developer.adobe.com/commerce/services/optimizer/merchandising-services/using-the-api#make-your-first-request){target="_blank"}
