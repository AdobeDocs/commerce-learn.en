---
title: Separate Packages Global Reference Architecture
description: Optimize Adobe Commerce with Separate Packages GRA. Learn setup, benefits, and best practices for flexible, versioned package management.
kt: 16727
doc-type: tutorial
audience: all
last-substantial-update: 2025-1-6
feature: Best Practices, Configuration, Install
topic: Architecture, Commerce, Development
role: Architect, Developer, User, Leader
level: Beginner, Intermediate
exl-id: cbddc4a3-602f-4208-85cd-b906d2b81f8b
---
# The Separate Packages global reference architecture pattern

This guide explains how to set up Adobe Commerce with the Separate Packages Global Reference Architecture (GRA) Pattern.

The Separate Packages GRA pattern involves one Git repository for each common package and a Git repository for each Adobe Commerce instance. Common packages are exposed through Composer with a private composer repository.

This global reference architecture pattern is completely Composer based and it is designed to get the maximum benefit from all Composer features.

![A diagram showing where code is stored in a Separate Packages GRA pattern](/help/assets/global-reference-architecture/separate-packages-gra-pattern-diagram.png){align="center"}

## Advantages and disadvantages of this pattern

Advantages:

- Code reuse through a shared code repositories
- Complete flexibility in package installation, each GRA package can be upgraded, downgraded or backported individually
- Full support for semantic versioning
- No special tooling, complex infrastructure or special branching strategy required
- Support for all package types that Composer supports

Disadvantages:

- Development within this GRA pattern is slightly more difficult at the start, there is a small learning curve
- Possible to deploy combinations of packages that were not developed in the same configuration, need for strict test procedures

## Set up Adobe Commerce with the Separate Packages GRA pattern

### The directory structure

The final directory structure of a full Adobe Commerce installation with the Separate Packages GRA pattern looks like this:

```text
.
├── app/
│   └── etc/
│       └── config.php
├── composer.json
└── composer.lock
```

The `app/code`, `app/i18n` and `app/design` directories are omitted on purpose. The Separate Packages GRA installs every single package from Composer. Even if the package is only installed in a single Adobe Commerce instance.

### Prepare the store repository

Create a repository for the first Adobe Commerce instance, which represents a web store for Brand X.

```bash
mkdir gra-separate-brand-x
cd gra-separate-brand-x
composer create-project --repository-url=https://repo.magento.com/ magento/project-enterprise-edition .
git init
git remote add origin git@github.com:AntonEvers/gra-separate-brand-x.git 
git add composer.json composer.lock
git commit -m 'initialize Brand X repository'
git push -u origin main
```

Install Adobe Commerce with `bin/magento setup:install`. Commit the resulting `app/etc/config.php`.

### Create package repositories

Each package in this global reference architecture pattern has its own Git repository. Below are example packages containing Adobe Commerce modules representing a GRA module, a third-party module and a local module.

- <https://github.com/AntonEvers/module-example-gra>
- <https://github.com/AntonEvers/module-example-3rdparty>
- <https://github.com/AntonEvers/module-example-local>

Use the examples to create your own packages.

### Create metapackage repositories

Metapackages control the scope of the GRA common codebase in this GRA pattern. They define what is in the foundation: which combination of package versions are always installed together. An example:

```json
{
    "name": "antonevers/gra-meta-foundation",
    "type": "metapackage",
    "require": {
        "antonevers/gra-component-foundation": "~1.0",
        "antonevers/module-gra": "~1.0",
        "antonevers/module-3rdparty": "~1.0",
        "magento/composer-dependency-version-audit-plugin": "~0.1",
        "magento/composer-root-update-plugin": "~2.0",
        "magento/product-enterprise-edition": "2.4.6-p3"
    }
}
```

The snippet above is the composer.json of a metapackage. Because metapackages only contain a composer.json file and no other code. The code above is also the full metapackage. Host it in a Git repository and you have an installable metapackage composer repository. It requires one example GRA module and a third-party module, as well as the Adobe Commerce core. It also requires the gra-component-foundation, which will be explained in the next chapter.

Metapackages are a way to bundle packages without creating dependencies between the packages. So, even when there is no technical dependency between packages, with a metapackage you can cause them to be installed together. If you require this metapackage in your project, then any package or metapackage that the metapackage requires gets installed. So, if you create a blank composer project and you only require this package, then Composer installs Adobe Commerce and the GRA and third-party module.

This way you can ensure that each store contains the same set of foundational packages.

You can similarly define a metapackage that defines store x. It requires the foundation metapackage, requiring the full GRA foundation, plus a local module:

```json
{
    "name": "antonevers/gra-meta-brand-x",
    "type": "metapackage",
    "require": {
        "antonevers/gra-meta-foundation": "~1.0",
        "antonevers/module-local": "~1.0"
    }
}
```

The Brand-X metapackage is optional. You may also skip the brand metapackage and require these dependencies directly in your store Composer project. The advantage of making a metapackage for local modules is that you do not have any feature branches and feature pull requests on the store Git repository, only in the package repositories. It is a safety measure. Additionally, you can choose to apply semantic versioning on the package repositories and use different Git tags on your main project, for instance to track named releases. It is up to you.

### GRA foundation files outside the vendor directory

Sometimes you need to store files outside of the vendor directory. Such as `.gitignore`, files that go in the `dev/` directory or domain verification files. The magento2-component package type is designed for this purpose. Look at <https://github.com/AntonEvers/gra-component-foundation>.

```json
{
    "name": "antonevers/gra-component-foundation",
    "type": "magento2-component",
    "require": {
        "magento/magento-composer-installer": "*"
    },
    "extra": {
        "map": [
            [
                "src/gitignore",
                ".gitignore"
            ]
        ]
    }
}
```

This package has the type magento2-component and it contains a src directory that hosts files that are copied to the Adobe Commerce root directory. The mapping in this file copies `/src/gitignore` to `/.gitignore` in the main Composer project.

This way you can make files outside of the vendor directory part of your GRA foundation too.

### Develop a GRA foundation module

Development happens inside the vendor directory. Ask Composer to install your foundation packages from source. Doing so, checks out packages from Git instead of installing them from a downloaded archive.

```bash
rm -r vendor/antonevers/*
composer install --prefer-source
```

With this command, packages in the antonevers namespace have been checked out using Git. When you enter the vendor/antonevers/module-gra directory, you are also entering the module-gra Git repository. You can now create, checkout and merge branches in place and develop in this way, straight from the vendor directory.

### Include third-party modules to the GRA foundation

Add third-party packages to the GRA metapackage. If third-party code is not available to be installed from a Composer repository, then create a package for it. Create a Git repo, add the packages contents (everything that would be in app/code/Vendor/Package) and make sure that there is a valid composer.json file at the root of the repository. You can now install this package through Composer.

## Set up a private Composer repository

A private repository is not mandatory in global reference architecture. It makes deployments and installation faster, reduces repository configuration in composer.json, and it increases security. Credentials to other Composer repositories and the Adobe Commerce marketplace are stored in your private repository. No more sensitive credentials bundled with the code or on developers' machines.

Additionally, some private repositories offer extra functionalities such as email notifications when one of your stores contains a security vulnerability in one of its dependencies.

The slowness issue is what occurs when you have multiple VCS repositories in composer.json. Each Composer repository needs to be read when doing upgrades and having 50 repositories for 50 packages has at least 50 times the overhead of just a single Composer repository.

![A diagram showing where slowness occurs when a composer repository is missing](/help/assets/global-reference-architecture/separate-packages-without-mirror-diagram.png){align="center"}

Include a Composer mirror in the form of a private Composer repository. The mirror contains a copy of all packages from other Composer repositories as well as all Git hosted packages. With a private Composer repository, you additionally get fine grained access control.

With Git synchronization, a private Composer repository automatically detects new packages in your Git repositories as well as new versions of existing packages.

You can host your own private repository with Satis: <https://composer.github.io/satis/>. See an example public repository at <https://antonevers.github.io/gra-composer-repository/>. This repo is used as the composer repository in the code examples. Additional measures are necessary to make a Satis repository private.

There are solutions that you can configure and forget about: Private Packagist <https://packagist.com/>, which is made by the same people that wrote Composer or JFrog Artifactory <https://jfrog.com/artifactory/>.

## Deliver code

With metapackages, there are 3 steps to deliver code.

1. Merge changes into packages and version the changed packages.
2. (Optional, only if new packages are added) Require the new packages in metapackages and version the metapackages.
3. (Optional, only if new packages are added) Require the new metapackages in Adobe Commerce and deploy.

Deployment scope is controlled with package versions. Creation of a stable version of a package means that this package is ready for production deployment.

To build a new release, run composer update in the main Composer project, which contains the full store installation. All latest versions of packages are installed.

## Versioning

Versioning in a Separate Packages GRA is a synonym to tagging modules in Git. Git tags create numbered versions of your packages that Composer installs.
The right versioning approach lets your packages flow automatically, while also remaining safe.

Two examples:

```json
{
    "name": "antonevers/gra-meta-foundation",
    "type": "metapackage",
    "require": {
        "antonevers/gra-component-foundation": "1.1.4",
        "antonevers/module-gra": "1.0.0",
        "antonevers/module-3rdparty": "1.3.89"
    }
}
```

This example shows a strict definition of dependencies. 3 packages are required in exact versions. Composer update with this metapackage in your installation does nothing. It always installs these 3 packages in these exact versions, even if a newer version is available.

```json
{
    "name": "antonevers/gra-meta-foundation",
    "type": "metapackage",
    "require": {
        "antonevers/gra-component-foundation": "~1.0",
        "antonevers/module-gra": "~1.0",
        "antonevers/module-3rdparty": "~1.0"
    }
}
```

This example shows a loose definition of dependencies. With `~1.0` any version of these packages can be installed if they are greater than or equal to `1.0.0` and lower than `2.0.0`, with a preference for the highest available version. You can learn more about how to define version dependencies at <https://getcomposer.org/doc/articles/versions.md>:

> The ~ operator is best explained by example: `~1.2` is equivalent to `>=1.2 <2.0.0`, while `~1.2.3` is equivalent to `>=1.2.3 <1.3.0`.

As soon as you release a new version of any of the packages mentioned, it is automatically installed with Composer update.

Apply semantic versioning. You can learn everything about semantic versioning at <https://semver.org/>. Especially, the FAQ is a must read. With semantic versioning, the numbers in "1.0.0" are called MAJOR.MINOR.PATCH. Minor and patch releases of a package should be safe to introduce without breaking the application.
You can automatically include patches and manually choose minor upgrades. Be aware that doing so costs you extra overhead by picking each minor change manually:

```json
{
    "name": "antonevers/gra-meta-foundation",
    "type": "metapackage",
    "require": {
        "antonevers/gra-component-foundation": "~1.1.0",
        "antonevers/module-gra": "~1.0.0",
        "antonevers/module-3rdparty": "~1.3.0"
    }
}
```

Of course, all this only works if you apply semantic versioning consistently, always. And not only in metapackages, but the requirements of your regular packages should define dependencies loosely too. If you have one strict dependency in your system, that package is limited to the strict definition.

Find these strict dependencies by typing composer depends \<package name\>. See <https://getcomposer.org/doc/03-cli.md#depends-why> for more information.

## Branching strategy

You can use various branching strategies to support this global reference strategy pattern, provided that the main branch is the only branch where you version your packages. If you version across several branches, it introduces the risk of randomly losing functionality between versions. Only create stable versions on the main branch.

Only create feature branches in your package repositories. Not on your store installation repositories. Remain able to introduce any change to your store just by using Composer. Avoid the necessity of Git merges on the deployment repository.

Branch types that are common in branching strategies and repositories they should exist in:

**Feature branches**: exist in your package repositories, nowhere else.

**Release branches**: are created in any repository: packages, metapackages, store installation repositories. When you plan a release, group changes in release branches of packages before versioning them. Suppose you are preparing a release with the code name "Unicorn". You can create a release-unicorn branch in packages with changes. Merge anything in there and then require "dev-release-unicorn as 1.4.0" in your metapackage. Learn more about aliases to see what is happening there: <https://getcomposer.org/doc/articles/aliases.md>.

**QA/Dev branches**: similar to release branches.

**Main branch**: must exist in every repository and should always be the branch that represents production or a production-ready state. The main branch is where you tag code to release versions.
Make sure you choose a branching strategy with little maintenance overhead. For example, merging the main branch back into QA, UAT, release, or dev branches after a hotfix release is an overhead maintenance task. The more packages, the more repositories and the more repetitive overhead tasks.

Use a tool like mixu/gr to perform routine operations on multiple Git repositories in a batch: <https://github.com/mixu/gr>

## Naming conventions

With the Separate Packages GRA pattern, packages are part of the GRA foundation if the foundation metapackage requires them. Add or remove packages from the metapackage to move them in and out of the foundation.

Metapackages give flexibility to the installation scope of packages. It is extra important that the names of packages do not contain any words that relate to the intended use of the package. The name antonevers/module-gra-store-locator may become confusing when you decide to take that package out of the GRA foundation. Avoid scope (GRA, foundation, local). Avoid region (EMEA, Spain, Global). Most definitely avoid the name of the store that a package is built for. Choose names that only relate to the functionality that is added in the package. That way you can reuse them everywhere you please, also in unforeseen future scenarios. The name antonevers/module-store-locator would be excellent.

Make sure that related packages show up together in overviews. Build names from generic to specific. So, antonevers/module-b2b-tax-exempt instead of antonevers/tax-exempt-module-b2b.

## Code examples

The code examples of this blog post have been combined in a set of Git repositories, which you can use to play around with the proof of concept.

- An example production store: <https://github.com/AntonEvers/gra-separate-brand-x>
- An example foundation module: <https://github.com/AntonEvers/module-example-gra>
- An example third-party module: <https://github.com/AntonEvers/module-example-3rdparty>
- An example local module: <https://github.com/AntonEvers/module-example-local>
- An example foundation metapackage: <https://github.com/AntonEvers/gra-meta-foundation>
- An example local metapackage (optional): <https://github.com/AntonEvers/gra-meta-brand-x>
- An example Composer repository: <https://github.com/AntonEvers/gra-composer-repository>
