---
title: How do you leverage Global Reference Architecture
description: Learn how to leverage a global reference architecture to establish a scalable and resilient commerce experience
landing-page-description: Learn about Global Reference Architecture and how it is used with Adobe Commerce
kt: 14040
doc-type: tutorial
audience: all
last-substantial-update: 2025-1-6
feature: Best Practices, Configuration, Install
topic: Architecture, Commerce, Development
role: Architect, Developer, User, Leader
level: Intermediate, Advanced

---

# The Monorepo global reference architecture pattern

This guide explains how to set up Adobe Commerce with the Monorepo Global Reference Architecture (GRA) Pattern.

The Monorepo GRA pattern involves a single Git repository to host all common customizations. This single Git repository is exposed through Composer as a separate composer packages.

![A diagram showing where code is stored in a monorepo GRA pattern](/help/assets/global-reference-architecture/monorepo-gra-pattern-diagram.png){align="center"}

## Advantages and disadvantages of this pattern

Advantages:

- Ideal for functional testing
- Code reuse through a shared code repositories
- Complete flexibility in package installation, each GRA package can be upgraded, downgraded or backported individually
- Full support for semantic versioning
- No special tooling, complex infrastructure or special branching strategy required
- Support for all package types that Composer supports
- Ideal for ephemeral environments, which are optional, but high volume delivery teams will find them very useful

Disadvantages:

- Possible to deploy combinations of packages that were not developed in the same configuration, need for strict test procedures
- The monorepo GRA pattern can be complex at the start. Assign a lead that understands the what, the how, and the why. This will prevent the team from trying to work around the monorepo and help them work with the system

## Set up Adobe Commerce with the Separate Packages GRA pattern

### The directory structure

The final directory structure of a full Adobe Commerce installation with the Separate Packages GRA pattern looks like this:

```text
.
├── app/
│   └── etc/
│       └── config.php
├── packages/
│   └── ...
├── composer.json
└── composer.lock
```

A production Git repository is equal to this:

```text
.
├── app/
│   └── etc/
│       └── config.php
├── composer.json
└── composer.lock
```

The difference is that the production stores install from Composer, where the monorepo holds its own copy of every package inside the packages directory.

### Prepare a production repository

Create a repository for the first Adobe Commerce instance, which represents a web store for Brand X.

```bash
mkdir gra-monorepo-brand-x
cd gra-monorepo-brand-x
composer create-project --repository-url=https://repo.magento.com/ magento/project-enterprise-edition .
git init
git remote add origin git@github.com:AntonEvers/gra-monorepo-brand-x.git 
git add composer.json composer.lock
git commit -m 'initialize Brand X repository'
git push -u origin main
```

Install Adobe Commerce with `bin/magento setup:install`. Commit the resulting `app/etc/config.php` and the composer files. Anything else is managed by Composer so should not be in Git.

### Prepare the monorepo repository

The monorepo repository starts with the same steps.

```bash
mkdir gra-monorepo 
cd gra-monorepo
composer create-project --repository-url=https://repo.magento.com/ magento/project-enterprise-edition .
```

Install Adobe Commerce with `bin/magento setup:install`, commit and push.

```bash
git init
git remote add origin git@github.com:AntonEvers/gra-monorepo.git 
git add composer.json composer.lock app/etc/config.php
git commit -m 'initialize monorepo GRA development repository'
git push -u origin main
```

### Prepare for monorepo development

For monorepo development, make the following changes to your composer.json file:

1. Change the name and description of the package so that it is clear that this is your monorepo package.
1. Delete the version attribute from composer.json, because the version will be managed using Git tags for this repository.
1. Replace the require section with a meta package which will be created later.
1. Change minimum stability to dev.
1. Add a path type repository that points to `packages/*/*` to host monorepo packages, including branch aliases for each package it contains
1. Add a branch alias for the project itself

The following Git diff shows the difference between a clean Adobe Commerce install and the changes mentioned above:

```diff
@@ -1,6 +1,6 @@
 {
-    "name": "magento/project-enterprise-edition",
-    "description": "eCommerce Platform for Growth (Enterprise Edition)",
+    "name": "antonevers/gra-monorepo",
+    "description": "Monorepo repository for Global Reference Architecture development",
     "type": "project",
     "license": [
         "proprietary"
@@ -15,11 +15,8 @@
         "preferred-install": "dist",
         "sort-packages": true
     },
-    "version": "2.4.7-p3",
     "require": {
-        "magento/product-enterprise-edition": "2.4.7-p3",
-        "magento/composer-dependency-version-audit-plugin": "~0.1",
-        "magento/composer-root-update-plugin": "^2.0.4"
+        "antonevers/gra-meta-brand-x": "self.version"
     },
     "autoload": {
         "exclude-from-classmap": [
@@ -69,16 +66,33 @@
             "Magento\\Tools\\Sanity\\": "dev/build/publication/sanity/Magento/Tools/Sanity/"
         }
     },
-    "minimum-stability": "stable",
+    "minimum-stability": "dev",
     "prefer-stable": true,
     "repositories": [
         {
+            "type": "path",
+            "url": "packages/*/*",
+            "options": {
+                "versions": {
+                    "antonevers/gra-meta-brand-x": "1.4.x-dev",
+                    "antonevers/gra-meta-foundation": "1.4.x-dev",
+                    "antonevers/gra-component-foundation": "1.4.x-dev",
+                    "antonevers/module-gra": "1.4.x-dev",
+                    "antonevers/module-3rdparty": "1.4.x-dev",
+                    "antonevers/module-local": "1.4.x-dev"
+                }
+            }
+        },
+        {
             "type": "composer",
             "url": "https://repo.magento.com/"
         }
     ],
     "extra": {
-        "magento-force": "override"
+        "magento-force": "override",
+        "branch-alias": {
+            "dev-main": "1.4.x-dev"
+        }
     }
 }
```

### Use metapackages

Download the example code from [AntonEvers/gra-meta-foundation](https://github.com/AntonEvers/gra-meta-foundation) on GitHub to get the metapackages and the sample modules that are used in this example.

Composer metapackages bundle multiple composer packages together under a single package. When a metapackage is required, all packages it bundles will be automatically installed. This is achieved through the Composer require secion of the metapackage.

For this example, there are two metapackages:

1. **antonevers/gra-meta-brand-x**: A metapackage that contains everything that makes up "Brand X".
1. **antonevers/gra-meta-foundation**: A metapackage that contains everything that is always installed in any brand.

The brand metapackage requires the foundation metapackage. When brand metapackage is required, the foundation metapackage is automatically required as well. Please see the two composer.json files of the metapackages to see how they relate:

antonevers/gra-meta-brand-x:

```json
{
    "name": "antonevers/gra-meta-brand-x",
    "type": "metapackage",
    "license": [
        "OSL-3.0",
        "AFL-3.0"
    ],
    "require": {
        "antonevers/gra-meta-foundation": "^1.4",
        "antonevers/module-local": "^1.4"
    }
}
```

antonevers/gra-meta-foundation:

```json
{
    "name": "antonevers/gra-meta-foundation",
    "type": "metapackage",
    "license": [
        "OSL-3.0",
        "AFL-3.0"
    ],
    "require": {
        "antonevers/gra-component-foundation": "^1.4",
        "antonevers/module-gra": "^1.4",
        "antonevers/module-3rdparty": "^1.4",
        "magento/composer-dependency-version-audit-plugin": "~0.1",
        "magento/composer-root-update-plugin": "^2.0.4",
        "magento/product-enterprise-edition": "2.4.7-p3"
    }
}
```

Metapackages are a good way to organize code that belongs together. Use metapackages to define groups of packages that are regional, global, brand-specific or any grouping that makes sense for you. If you maintain multiple installations of Adobe Commerce, this is a safe and versatile way of defining the context in which a package is expected.

Metapackages exist in the monorepo inside the `packages` directory. There, the directory structure of the `vendor` is mirrored:

```text
.
├── packages/
│   └── antonevers
│       ├── gra-meta-brand-x
│       │   └── composer.json
│       └── gra-meta-foundation
│           └── composer.json
├── composer.json
└── composer.lock
```

### Add and develop modules

Modules in the monorepo exist in the `packages` directory. This way Composer can find them through the path type repository.

Download the example code from [AntonEvers/gra-meta-foundation](https://github.com/AntonEvers/gra-meta-foundation) on GitHub to get the metapackages and the sample modules that are used in this example.

```text
.
├── packages/
│   └── antonevers
│       ├── gra-meta-brand-x
│       ├── gra-meta-foundation
│       ├── module-3rdparty
│       ├── module-gra
│       └── module-local
├── composer.json
└── composer.lock
```

You can have multiple namespaces inside the `packages` directory if needed.

Development takes place in the packages directory. Symlinks to the packages inside the `packages` directory are created in the `vendor` directory once you run `composer update`. This way, the code becomes part of the Adobe Commerce installation.

Run `bin/magento module:enable --all` or for only specific modules to enable the modules that were added.

By now you should have a working Adobe Commerce installation with the three sample modules installed and working. You can validate this by running the commands:

```bash
bin/magento test:gra
bin/magento test:3rdparty
bin/magento test:local
```

### Achieve automated package creation

There are multiple options to achieve automated package creation, some of these are:

1. [Private Packagist](https://packagist.com/)
1. [Simplyfy Monorepo Builder](https://github.com/symplify/monorepo-builder)
1. Build your own solution

[Private Packagist](https://packagist.com/) takes care of the complete automation of recognizing packages in your Git monorepo and exposing them through Composer. It is compatible with Adobe Commerce, fast, low-maintenance and error-prone, which is why this guide will focus on the Private Packagist option.

It is beyond the scope of this guide to explain how to set up Private Packagist. For that, please see the [docs](https://packagist.com/docs). 

There is the possibility to turn a package into a monorepo once you have set up organization syncing and your Git repositories are automatically syncing to Private Packagist.

First, go to the packages tab and find the monorepo:

![Private Packagist screen shot with the monorepo package visible in the packages screen](/help/assets/global-reference-architecture/packagist-packages-before-multi-package.png){align="center"}

Click on the monorepo package and click "Edit" in the details screen. This should take you to the following page:

![Private Packagist screen shot with the monorepo package edit page](/help/assets/global-reference-architecture/packagist-packages-edit.png)

Underneath the first input field, there is a link saying: Create a multi-package repository. Click this link.

![Private Packagist screen shot with the multi-package configuration](/help/assets/global-reference-architecture/packagist-packages-multi-package.png)

Define the location where composer packages can be found inside your monorepo. In the example this is `packages/**/composer.json`. Change this to limit or broaden where Private Packagist searches for packages to extract.

The packages tab will show all found packages after saving, and the monorepo itself will no longer be visible as a Composer package:

![Private Packagist screen shot with all monorepo packages visible in the packages screen](/help/assets/global-reference-architecture/packagist-packages-after-multi-package.png)

A version will be created in Composer for each package inside the monorepo, for every tag or branch that is created on the monorepo in Git.

## Install the packages to the production environment

Follow the instructions from Private Packagist to add Private Packagist as a composer repository. Private Packagist can and should be used as a mirror for all your Composer repositories and Git repositories, including packagist.org. That way credentials do not have to be shared with developers and you have complete control over each package. This example does not follow this best practice as it would expose the Adobe Commerce codebase publicly.

Download [GRA Monorepo Brand X](https://github.com/AntonEvers/gra-monorepo-brand-x) from GitHub to see an example of a production store. 

In the production store, there is no `packages` directory, and all packages are installed through Composer. The only package that is required is:

```json
    "require": {
        "antonevers/gra-meta-brand-x": "^1.0"
    },
```

Yet all of Adobe Commerce and the entire GRA is installed through this metapackage's requirements and its decendants.

## Versioning

All packages in the monorepo receive the same version as the monorepo itself. Think of it as publising new versions of the entire application. On production, however, you can install a mix of packages from different monorepo versions.

## Ephemiral environments

If you use phemiral environments or you plan to use them, the monorepo is an excellent choice. Every version and branch of the monorepo contains all Adobe Commerce, third party and custom module files. Because of this it is possible to run every type of test including functional tests. With other GRA setups such as the separate packages or bulk packages GRA, you would first need to build a working Adobe Commerce environment before being able to run functional tests. From a DevOps perspective monorepo makes it much simpler.

## Code examples

The code examples of this article have been combined in a set of Git repositories, which you can use to play around with the proof of concept.

- An example monorepo repository: <https://github.com/AntonEvers/gra-monorepo>
- An example production store: <https://github.com/AntonEvers/gra-monorepo-brand-x>
