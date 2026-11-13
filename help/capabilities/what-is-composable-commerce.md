---
title: Composable Commerce With Adobe
description: Learn about composable commerce with Adobe platform options, Edge Delivery Services storefronts, API Mesh, App Builder, and Commerce development MCP tools.
feature: API Mesh, App Builder, Saas
topic: Architecture, Commerce, Development, Headless, Integrations, Performance, Personalization
role: Admin, Developer, User
level: Intermediate
doc-type: Tutorial
duration: 307
last-substantial-update: 2026-11-13
jira: KT-15730
exl-id: 4d811a2f-8488-4de7-babd-449aced42e3a
TQID: 'https://experienceleague.adobe.com/NG-US7zLBgzV425mheo3oQ9Z6gnzAr6aRCLNjHVU0aM'
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: ba9e5be9-7de1-4f71-a5d2-baead0e425ee
    internal-label: Security
  - id: c32adafa-ed01-4b31-997e-2413013911b0
    internal-label: Integrations
  - id: e8818fe6-9c8b-4bc0-9ef8-377a10b7bc75
    internal-label: Architecture
  - id: d3b92bef-63fa-5031-a925-d04d9362d616
    internal-label: Saas
  - id: cc250cf1-34eb-4863-80d0-d170d45ea067
    internal-label: Developer tools
subfeature_v2:
  - id: a743e5dc-8f37-4b5d-a848-03c32ca30598
    internal-label: App Builder
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: b5ce8718-c3af-4fdb-a1a9-fca32f83a87c
    internal-label: Implementation
  - id: bce87dde-a4ab-44c9-8a18-ad66e4ddb377
    internal-label: Customer experience
  - id: d095671a-1355-40aa-8b5f-06c33c68080b
    internal-label: Security
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
  - id: f4e6943a-c91a-4134-a2c7-f4f20cfff2f0
    internal-label: Privacy
autotag-review: '2026-11-13T20:04:10.194Z'
---
# Composable commerce

Composable commerce is an architectural approach that combines commerce capabilities through APIs. You can select and integrate components for storefront experiences, catalog management, product discovery, checkout, and other business needs instead of requiring every capability to come from one tightly coupled application.

Headless commerce separates the storefront presentation layer from the commerce backend. Composable commerce builds on that separation by letting teams choose which capabilities to keep together and which to integrate independently. A headless storefront does not inherently make every backend component independently replaceable.

Adobe supports this approach through commerce platform options, storefront technology, and integration and development tools. Adobe Commerce as a Cloud Service (ACCS), Adobe Commerce Optimizer (ACO), Edge Delivery Services, API Mesh, App Builder, and Commerce development MCPs serve different purposes. They are not interchangeable products or a required combined stack.

## Benefits and trade-offs

A composable approach can help you:

* **Adapt the customer experience:** Choose storefront components and integrate services that meet your business requirements.
* **Modernize incrementally:** Replace selected capabilities while retaining other systems and their data.
* **Scale and evolve independently:** Design integrations and extensions so their changes do not require a release of the entire commerce application.
* **Reuse commerce capabilities:** Use supported platform features and APIs rather than rebuilding every business function.

These benefits depend on the implementation. Evaluate technical maturity, delivery costs, licensing, security, and data privacy. Define ownership for API contracts, data synchronization, authentication, performance, and failures across services. A more modular architecture can also increase integration and operational complexity.

## Adobe Commerce architecture options

Start by deciding whether you need a managed commerce platform or want to modernize customer experiences around an existing transactional backend.

For a video comparison, see [Adobe's available commerce options](./adobes-available-commerce-options.md).

### Adobe Commerce as a Cloud Service

Adobe Commerce as a Cloud Service is a managed SaaS commerce platform. Adobe manages the core application, infrastructure, and updates. Its architecture includes Commerce Foundation, headless storefront capabilities, merchandising services, and developer tools.

Use this option when evaluating a managed commerce foundation with supported extension points. For custom business logic, plan for supported out-of-process extensibility rather than assuming existing PHP extensions can be deployed unchanged. ACCS does not support Luma storefronts; include storefront migration in your implementation plan when applicable.

See the [Adobe Commerce as a Cloud Service overview](https://experienceleague.adobe.com/en/docs/commerce/cloud-service/overview).

### Adobe Commerce Optimizer

Adobe Commerce Optimizer supports catalog management, product discovery, search, recommendations, and storefront experiences while allowing you to retain an existing commerce backend. Catalog data can come from external sources, and a third-party system can remain responsible for the cart and checkout lifecycle.

Use this option when customer-facing modernization is the goal and replacing the transactional backend is not required. Plan catalog ingestion and cart and checkout integrations explicitly. ACCS and ACO are separate architecture options, not a required combined stack. Verify current integration support before selecting services for your implementation.

See the [Adobe Commerce Optimizer overview](https://experienceleague.adobe.com/en/docs/commerce/optimizer/overview).

### Existing Adobe Commerce deployments

Adobe Commerce on cloud infrastructure and on-premises deployments can also adopt headless storefronts and supported API-based integrations incrementally. Depending on the deployment, you can retain an existing storefront or adopt a supported headless storefront. Keeping existing commerce capabilities together can reduce integration work while allowing selected services to evolve separately.

Feature availability, extension compatibility, licensing, and setup requirements vary by offering and version. Compare the [Adobe Commerce platforms and services](https://experienceleague.adobe.com/en/docs/commerce/information-center/explore-platforms-and-services/platform-and-services) before choosing an architecture.

## Commerce Storefront powered by Edge Delivery Services

Commerce Storefront powered by Edge Delivery Services provides the storefront experience and content delivery layer. Its headless architecture lets teams develop the frontend independently from the commerce foundation. Document-based authoring and visual editing support content updates, while storefront components use commerce APIs for shopping capabilities.

Distinguish the storefront interface from the systems responsible for catalog data, pricing, cart operations, checkout, and orders. Edge Delivery Services does not replace the transactional commerce backend. Identify the supported services and integration path for your chosen backend before implementing the storefront.

See the [Commerce Storefront documentation](https://experienceleague.adobe.com/en/tools/commerce-storefront/).

## Integration and extensibility

API Mesh and App Builder help connect and extend commerce capabilities without requiring every customization to be embedded in the core commerce application.

### API Mesh

API Mesh for Adobe Developer App Builder combines multiple Adobe, private, and third-party API sources into a queryable GraphQL endpoint. Use it to compose data for frontend experiences and coordinate access to existing services.

API composition does not remove the need to define API contracts, authentication, error handling, or ownership of transactional business logic. Keep those responsibilities explicit in the integration design.

See the [API Mesh overview](https://developer.adobe.com/graphql-mesh-gateway/).

### Adobe App Builder

Adobe App Builder provides a platform for applications that extend Adobe solutions and run on Adobe infrastructure, including Adobe I/O Runtime. You can use it for out-of-process customizations and integrations with systems such as CRMs, ERPs, and PIMs.

Choose supported extension points, events, and webhooks for the Commerce offering you use. Design and test the application separately from the core commerce release lifecycle.

See the [App Builder overview](https://developer.adobe.com/app-builder/docs/intro_and_overview/).

## Commerce development MCPs and skills

Commerce development MCPs and skills support AI-assisted development of App Builder applications and storefront customizations. They can also help migrate existing Adobe Commerce PHP extensions to App Builder applications when moving to ACCS.

Model Context Protocol (MCP) servers connect compatible AI coding clients to development tools. Adobe's tooling includes the Commerce Developer MCP Server, App Builder MCP Server, and Dropins AI Tools, together with Commerce-specific skills.

Commerce development MCPs are development tools, not storefront delivery, cart, checkout, or order-processing services. They do not make an application compatible with every Commerce offering automatically. Review generated changes and test them against the target environment.

See [Commerce development MCPs and skills](https://developer.adobe.com/commerce/extensibility/developer-agent/coding-tools).

## Plan a composable implementation

1. Define business goals, customer experiences, security requirements, and the skills available to your team.
2. Choose the commerce platform and identify which existing systems to retain or replace.
3. Select a supported storefront and define the boundaries between presentation, merchandising, and transactional services.
4. Establish data ownership and API contracts for catalog information, prices, inventory, customers, carts, checkout, and orders.
5. Plan authentication, data synchronization, caching, monitoring, and failure handling across integrations.
6. Implement incrementally and validate functionality, performance, and security before each release.

A composable implementation succeeds when its components meet business requirements and work together reliably. Select the capabilities you need rather than adding services solely to make the architecture more modular.

## Related resources

Explore these tutorials, videos, implementation guides, and the playlist to plan your architecture and build commerce integrations.

### Commerce platforms and storefronts

* [Adobe Commerce as a Cloud Service architecture](../commerce-as-a-cloud-service/architecture.md)
* [Composable storefronts and modular architecture](../commerce-as-a-cloud-service/product-overview/composable-storefront-and-modular-architecture.md)
* [Adobe Commerce Optimizer overview](../adobe-commerce-optimizer/overview.md)
* [Why the composable catalog data model exists](../adobe-commerce-optimizer/composable-catalog-data-model/why-ccdm-exists.md)
* [Shopper experiences with Edge Delivery Services](../edge-delivery-services/shopper-experience.md)

### Integration and development

* [Out-of-process extensibility with App Builder](../app-builder/foundations/introduction-to-app-builder.md)
* [Get started with API Mesh](../api-mesh/getting-started-api-mesh.md)
* [Create an API Mesh with multiple sources](../api-mesh/graphql-multiple-source.md)
* [Build custom shipping rates with AI and MCP tools](../app-builder/custom-shipping-rates-ai-tools/ai-tools-starter-kit.md)

### Architecture and development documentation

* [Migrate to Adobe Commerce as a Cloud Service](https://experienceleague.adobe.com/en/docs/commerce/cloud-service/migration/overview)
* [Adobe Commerce Optimizer integrations](https://experienceleague.adobe.com/en/docs/commerce/optimizer/integrations-overview)
* [Get started with Commerce Storefront development](https://experienceleague.adobe.com/en/tools/commerce-storefront/get-started/)
* [Best practices for Commerce development MCPs and skills](https://developer.adobe.com/commerce/extensibility/developer-agent/best-practices)

### Playlist

* [Get started with API Mesh using Adobe App Builder and Adobe Commerce](https://experienceleague.adobe.com/en/playlists/commerce-get-started-app-builder-and-api-mesh)
