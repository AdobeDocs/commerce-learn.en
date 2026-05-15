---
title: Learn About Catalog Views in Composable Catalog Data Model
description: Learn how catalog views in Adobe Composable Catalog Data Model (CCDM) map one base catalog to each storefront with distinct products, prices, and rules.
feature: Saas, Storefront
topic: Commerce
role:
  - Architect
  - Developer
level: Beginner
doc-type: Tutorial
duration: 297
last-substantial-update: 2026-05-15
jira: KT-21132
---
# Catalog views in the Adobe Composable Catalog Data Model

Catalog views are how you serve each audience differently from a single composable catalog. This tutorial explains what a catalog view is, how Adobe Commerce Optimizer applies it for a shopper, and why a unique view ID is the anchor for products, prices, and rules—using the **Carvelo Automobiles** demonstration scenario.

## Who is this video for?

* Commerce solution architects and developers who model multi-brand or multi-dealer catalogs on Adobe Commerce Optimizer

## Video content

* The Carvelo Automobiles scenario (brands, dealerships, and agreements)
* What a catalog view is, and the “lens” metaphor over a unified base catalog
* How a storefront uses a catalog view to filter products and pricing (for example, Celport)
* Catalog view unique IDs and the business value of a single source of truth

>[!VIDEO](https://video.tv.adobe.com/v/3491261?learn=on)

## Scenario: Carvelo Automobiles

**Carvelo Automobiles** is a fictitious auto parts company often used in Adobe Commerce demonstrations, documentation, and tutorials. Carvelo sells parts across three brands—**Aurora**, **Bolt**, and **Cruz**—through three dealerships:

* **Arkbridge** belongs to West Coast Inc.
* **Kingsbluff** and **Celport** belong to East Coast Inc.

Each dealership has its own agreement about which products it is allowed to sell. That creates a genuinely complex setup—and it can still run from **a single base catalog** of about six million SKUs. The capability that makes that possible is a **catalog view**.

## What is a catalog view?

A **catalog view** is a configured view of your catalog for a specific business context. Think of it as a **lens**. Your unified base catalog sits in the middle, holding every SKU for every brand. Each dealership gets its own lens—its own catalog view.

In the example:

* The **Arkbridge** lens can show all three brands—Aurora, Bolt, and Cruz parts.
* The **Celport** lens shows only a subset of Bolt and Cruz parts.

Each catalog view can also control **pricing**. The **underlying catalog data does not change**—only the viewable aspects (assortment, price, and rules) change for that context.

## How Commerce Optimizer applies a catalog view

When a shopper visits the **Celport** storefront, Adobe Commerce Optimizer uses the **Celport catalog view** to determine exactly which products, prices, and rules apply. The shopper only sees what that lens allows.

Other products may still exist in the catalog—for example Aurora tires, Bolt motors, or Cruz batteries—but **Celport’s storefront never exposes them** if the catalog view does not allow it.

## Catalog view ID and business value

Every catalog view has a **unique ID**. That ID is what connects your storefront to its catalog configuration. You set it once in storefront configuration, and downstream behavior follows—the right products, the right prices, and the right rules.

Instead of maintaining separate catalogs for every dealer or brand—and keeping them synchronized—you maintain **one** composable catalog. Catalog views are how you shape **many different storefront experiences** from that **single source of truth**.

## Related Content

* [[!DNL Adobe Commerce Optimizer] Guide](https://experienceleague.adobe.com/en/docs/commerce/optimizer/overview){target="_blank"}
* [Getting started with Merchandising API](https://developer.adobe.com/commerce/services/optimizer/merchandising-services/using-the-api/#make-your-first-request){target="_blank"}
