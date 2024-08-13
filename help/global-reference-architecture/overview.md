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

Global reference architecture can be valuable, depending on the number of instances you own. An instance is a standalone installation of Adobe Commerce using its own database. Count the number of production databases to know how many instances you own. If you maintain more than one instance, or if you foresee this scenario in the future, you can benefit from global reference architecture. The more functionality the instances share, the more valua a global reference architecture adds.

In any of these scenarios, it is advisable to explore using multiple instances of Adobe Commerce.

1. **Different Store Owners**: If you maintain code for multiple store owners, each with their own distinct store, separate instances may be needed to maintain their individual requirements effectively.
2. **Compliance with National Regulations**: Certain regulations mandate that customer data must be stored within specific regions. In such cases, separate instances are essential to ensure compliance with these regulations.
3. **Operational Variances Across Geographical Regions**: Operating in multiple regions may mean differing maintenance schedules and requirements. Using separate instances allows for flexibility in managing these variations efficiently.
4. **High-Intensity Flash Sales**: Stores conducting large-scale flash sales often require optimized server performance. Dedicated infrastructure provided by separate instances ensures optimal performance during such high-demand periods.
5. **Significant Differences Between Brands or Countries**: When the difference between brands or countries is large, using a single instance  results in code that is only used for some brands or countries. Separate instances can enhance performance and stability by eliminating unnecessary code for brands and countries that don't need it.

## Global Reference Architecture Patterns

Next to "no GRA pattern" there are four styles of GRA patterns.

![5 icons of GRA patterns: no GRA, split, bulk, separate and monorepo.](/help/assets/global-reference-architecture/gra%20patterns%20horizontal.png){align="center"}

### No GRA pattern

![An icon that depicts "no GRA"](/help/assets/global-reference-architecture/no-gra.png){align="center"}

When a GRA pattern is not used, each Adobe Commerce instance is a unique application. There is no code reuse, except by manually moving code from one instance to another. These copies can diverge. In this scenario, three instances need three times the maintenance effort of one instance.

![A diagram depicting 3 stores, where each is a copy from the former, with unique development happening in all 3 copies.](/help/assets/global-reference-architecture/no-gra-pattern-diagram.png){align="center"}

### The split Git GRA pattern

![An icon depicting the "split" GRA pattern](/help/assets/global-reference-architecture/split-git.png){align="center"}

This pattern consists of a single Git repository, with 3 remotes, named "core", "third-party" and "customization". Each file in the project repository is maintained in one of the 3 remotes. They come together as a braid forming the whole GRA. Each line of code only exist in a single development repository and is installed to the instances using the braiding technique, leading to code reuse.

![A diagram showing where code is stored in a split GRA pattern](/help/assets/global-reference-architecture/split-git-gra-pattern-diagram.png){align="center"}

### The bulk packages GRA pattern

![An icon representing the "bulk" GRA pattern](/help/assets/global-reference-architecture/bulk-packages.png){align="center"}

The Adobe Commerce core and third-party modules are directly installed through Composer repositories. Git repositories can be used as Composer repositories. In this pattern, the entire GRA shared codebase is hosted in a single or a few Git repositories and installed through Composer. The key characteristic is that multiple modules, language packs or themes are hosted in a single composer package, simplifying development.

![A diagram showing where code is stored in a bulk packages GRA pattern](/help/assets/global-reference-architecture/bulk-gra-pattern-diagram.png){align="center"}

### The separate packages GRA pattern

![An icon representing the "separate packages" GRA pattern](/help/assets/global-reference-architecture/separate-packages.png){align="center"}

Each Adobe Commerce module, language pack or theme is installed as a separate composer package. Each cusomization has its own Git repository. This means ultimate flexibility in the composition of the instances and it adds the reliability of Composer dependency management. For performance optimization, all packages are mirrored in a single private composer repository.

![A diagram showing where code is stored in a separate packages GRA pattern](/help/assets/global-reference-architecture/separate-packages-gra-pattern-diagram.png){align="center"}

### The monorepo GRA pattern

![An icon representing the "monorepo" GRA pattern](/help/assets/global-reference-architecture/monorepo.png){align="center"}

All development takes place in a single code repository. Automation generates packages for new versions and publishes them to a composer repository. This combines the low development overhead of the bulk packages approach with the flexibility of the separate packages approach. The monorepo pattern is also ideal for running automated functional tests.

![A diagram showing where code is stored in a monorepo GRA pattern](/help/assets/global-reference-architecture/monorepo-gra-pattern-diagram.png){align="center"}

## Choosing a GRA pattern

The choice for a GRA pattern is made by assessing the project complexity, the need for flexibility, and the development team's ability to adapt. 

Teams with little Adobe Commerce experience best start simple. However, if the project demands a more complex GRA pattern due to its characteristics, do not compromise.

Common project characteristics related to each pattern:

1. **No GRA pattern**: Single instance of Adobe Commerce with no plans to extend. Multiple instances of Adobe Commerce with minimal commonality between them.

2. **Split Git GRA pattern**: Teams that wish to avoid Composer for their customizations. In most cases Bulk packages is a preferred pattern to Split Git.

3. **Bulk package GRA pattern**: Customization codebase with high interdepencence. Instances all have very similar combinations of custom packages. No frequent promotion or demotion of individual packages. Teams with little experience in code management and in need of simplicity.

4. **Separate packages GRA pattern**: Flexible release scope management needed. 50 or less custom packages anticipated in the next 5 years. Potentially global and regional layers of common code. No plans to migrate to a Monorepo pattern. Team is technically adept and has strict process adherence.

5. **Monorepo GRA pattern**: All characteristics of the Separate packages GRA pattern. More than 50 packages anticipated in the next 5 years. Need for extensive automated testing. Support for ephemeral environments. Enterprise scale complex codebase, that needs to scale without scaling maintenance cost at an equal rate.

### The cost of a wrong choice

Migration from one pattern to another is possible. The diagram below shows the level of impact of moving from one pattern to another. Green lines show low impact, yellow and amber lines show moderately complex to complex migrations.

![A diagram showing colored arrows between all 4 GRA patterns, indicating the level of difficulty of moving from one to the other.](/help/assets/global-reference-architecture/wrong-choice.png){align="center"}