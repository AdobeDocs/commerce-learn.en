---
title: How do you leverage Global Reference Architecture
description: Learn how to leverage a global reference architecture to establish a scalable and resilient commerce experience
landing-page-description: Learn about Global Reference Architecture and how it is used with Adobe Commerce
kt: 14040
doc-type: video
audience: all
last-substantial-update: 2023-6-25
feature: Best Practices, Configuration, Install
topic: Architecture, Commerce, Development
role: Architect, Developer, User, Leader
level: Beginner, Intermediate

---

# Global Reference Architecture Implementation Techniques

There are several ways to optimize code reuse with Adobe Commerce. These four implementation techniques each have their own advantages.

## When to use Global Reference Architecture

Global reference architecture can be valuable, depending on the number of instances you own. An instance is a standalone installation of Adobe Commerce using its own database. Count the number of production databases to know how many instances you own. If you maintain more than one instance, or you foresee this scenario in the future, you can benefit from global reference architecture. The more functionality the instances share, the more valuable a global reference architecture is.

In any of these scenarios, it is advisable to explore using multiple instances of Adobe Commerce.

1. **Different Store Owners**: If you're serving multiple store owners, each with their own distinct store, separate instances may be needed to maintain their individual requirements effectively.
2. **Compliance with National Regulations**: Certain regulations mandate that customer data must be stored within specific regions. In such cases, separate instances are essential to ensure compliance with these regulations.
3. **Operational Variances Across Geographical Regions**: When operating in multiple regions, differing maintenance schedules and requirements may arise. Using separate instances allows for flexibility in managing these variations efficiently.
4. **High-Intensity Flash Sales**: Stores conducting large-scale flash sales often require optimized server performance. Dedicated infrastructure provided by separate instances ensures optimal performance during such high-demand periods.
5. **Significant Differences Between Brands or Countries**: In cases where the difference between brands or countries is large, using a single instance may result in disabled code. Separate instances can enhance performance and stability by eliminating unnecessary code.

## Global Reference Architecture Patterns

![5 icons of GRA patterns: no GRA, split, bulk, separate and monorepo.](/help/assets/global-reference-architecture/gra%20patterns%20horizontal.png){align="center"}

### No GRA pattern

![An icon that depicts "no GRA"](/help/assets/global-reference-architecture/no-gra.png){align="center"}

When no GRA pattern is applied, each Adobe Commerce instance is a unique application. There is no code reuse, except by manually moving code from one instance to another.

![A diagram depicting 3 stores, where each is a copy from the former, with unique development happening in all 3 copies.](/help/assets/global-reference-architecture/no-gra-pattern-diagram.png){align="center"}

### The split Git GRA pattern

![An icon depicting the "split" GRA pattern](/help/assets/global-reference-architecture/split-git.png){align="center"}

At a high level, this pattern consists of a single Git repository for your project, with 3 remotes: core, third-party and customization. Each file in the project repository is maintained in one of the 3 remotes. They come together as a braid forming the whole GRA.

![A diagram showing where code is stored in a split GRA pattern](/help/assets/global-reference-architecture/split-git-gra-pattern-diagram.png){align="center"}

### The bulk packages GRA pattern

![An icon representing the "bulk" GRA pattern](/help/assets/global-reference-architecture/bulk-packages.png){align="center"}

The Adobe Commerce core and third-party modules are directly installed through Composer repositories. Git repositories can be used as Composer repositories. In this pattern, the entire GRA shared codebase is hosted in a single or a few Git repositories and installed through Composer.

![A diagram showing where code is stored in a bulk packages GRA pattern](/help/assets/global-reference-architecture/bulk-gra-pattern-diagram.png){align="center"}

Bulk packages must contain items that are always installed together. While Composer is used, dependency management within bulk packages is only enforced through module.xml files inside the modules of the bulk package. This method of dependency management is not as flexible and reliable as Composer's dependency management.

### The separate packages GRA pattern

T.B.D.

### The monorepo GRA pattern

T.B.D.

## Choosing a GRA pattern

### The cost of a wrong choice

