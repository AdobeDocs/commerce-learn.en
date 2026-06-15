---
title: Why the Composable Catalog Data Model (CCDM) Exists
description: Learn how CCDM keeps one unified catalog while storefronts receive filtered products, prices, and rules using catalog views and Merchandising Services.
feature: Saas, Storefront
topic: Commerce
role: Developer
level: Beginner
doc-type: Tutorial
duration: 259
last-substantial-update: 2026-05-15
jira: KT-18624
---
# Why the composable catalog data model exists

Modern commerce teams often sell across **brands**, **regions**, **dealerships**, and **digital channels**. When each channel keeps its own catalog copy, teams spend more time reconciling SKUs, prices, and availability than improving the shopper experience. The **Adobe Composable Catalog Data Model (CCDM)** behind **Adobe Commerce Optimizer** is designed to reverse that pattern: **one unified catalog** in a SaaS layer, with **catalog views** and **policies** shaping what each storefront or integration is allowed to see.

## Who is this video for?

* Commerce solution architects and developers who are new to Adobe Commerce Optimizer and need the business context before configuring catalog sources, views, and policies

## Video content

* Why duplicated, channel-specific catalogs create operational risk and slower innovation
* How CCDM keeps product data unified while still supporting multi-brand and multi-region scenarios
* How catalog views act as the "lens" between a shared base catalog and a specific storefront or audience
* How Merchandising Services APIs consume those views so headless experiences stay aligned with the configured catalog

>[!VIDEO](https://video.tv.adobe.com/v/3491285?learn=on)

## The challenge with siloed catalogs

When every dealer site, regional storefront, or brand property maintains **its own catalog database**, several problems compound:

* **Duplication** — the same SKU, description, and media are entered many times.
* **Drift** — price updates, new attributes, or discontinued items land in one channel but not others.
* **Slower launches** — each new touchpoint repeats heavy data work instead of reusing a single product record.

CCDM exists so product information can live in **one composable catalog** that other systems enrich, while storefronts still receive **channel-appropriate** assortments and pricing.

## What the composable catalog data model changes

In Adobe Commerce Optimizer, product data is **ingested into a unified base catalog** from one or more **catalog sources** (for example a locale such as `en-US`, or upstream systems such as a PIM or ERP). That source supplies the raw attributes and values.

**Catalog views** then define how that unified data is **organized and exposed** for a business context: which products pass your **policies**, which **price books** apply, and which **catalog source** backs the view. The same underlying records can therefore support **many projections**—for example separate views per dealer, region, or brand—without cloning the entire catalog for each site.

This separation—**where data comes from** (catalog source) versus **how it is presented** (catalog view)—is the core reason teams adopt CCDM instead of maintaining parallel catalogs per channel.

## Catalog views as the storefront lens

As described in [Catalog Views for Merchandising Services](https://experienceleague.adobe.com/en/docs/commerce/optimizer/setup/catalog-view){target="_blank"}, a catalog view behaves like a **lens**: shoppers only see the products, prices, and rules that view allows, while the **base catalog** remains the shared system of record. That model pairs directly with **Merchandising Services** so API clients pass the correct view (and related headers) and receive a consistent, policy-driven response for each experience.

For a deeper walkthrough of how those pieces fit an end-to-end flow, see the developer walkthrough [Create a composable catalog for your storefront](https://developer.adobe.com/commerce/services/optimizer/ccdm-use-case){target="_blank"}.

## Related Content

* [Learn about Catalog Views](./learn-about-the-ccdm-feature-catalog-views.md)
* [Catalog Views for Merchandising Services](https://experienceleague.adobe.com/en/docs/commerce/optimizer/setup/catalog-view){target="_blank"}
* [Create a composable catalog for your storefront](https://developer.adobe.com/commerce/services/optimizer/ccdm-use-case){target="_blank"}
* [[!DNL Adobe Commerce Optimizer] Guide](https://experienceleague.adobe.com/en/docs/commerce/optimizer/overview){target="_blank"}
* [Getting started with Merchandising API](https://developer.adobe.com/commerce/services/optimizer/merchandising-services/using-the-api#make-your-first-request){target="_blank"}
