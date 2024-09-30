---
title: The Separate Packages global reference architecture pattern
description: Learn how to leverage a global reference architecture to establish a scalable and resilient commerce experience
landing-page-description: Learn about Global Reference Architecture and how it is used with Adobe Commerce
kt: 14040
doc-type: tutorial
audience: all
last-substantial-update: 2024-6-25
feature: Best Practices, Configuration, Install
topic: Architecture, Commerce, Development
role: Architect, Developer, User, Leader
level: Beginner, Intermediate

---

# The Separate Packages global reference architecture pattern

This guide explains how to set up Adobe Commerce with the Separate Packages Global Reference Architecture (GRA) Pattern.

The Separate Packages GRA pattern involves one Git repository for each common package and a Git repository for each Adobe Commerce instance. Common packages are exposed through Composer with a private composer repository.

This global reference architecture pattern is completely Composer based and it is designed to get the maximum benefit from all Composer features.

![A diagram showing where code is stored in a separate packages GRA pattern](/help/assets/global-reference-architecture/separate-packages-gra-pattern-diagram.png){align="center"}

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

Metapackages are a way to bundle packages without creating dependencies between the packages. So, even when there is no technical dependency between packages, with a metapackage you can cause them to be installed together. If you require this metapackage in your project, then any package or metapackage that the metapackage requires is installed. So, if you create a blank composer project and you only require this package, then Composer installs Adobe Commerce and the GRA and third-party module.

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

