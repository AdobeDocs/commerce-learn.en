---
title: Optimizing Adobe Commerce with Bulk Packages Global Reference Architecture
description: Learn how to set up Adobe Commerce using the Bulk Packages Global Reference Architecture for efficient code management and version control.
jira: KT-16726
doc-type: tutorial
audience: all
last-substantial-update: 2025-1-6
feature: Best Practices, Configuration, Install
topic: Architecture, Commerce, Development
badge: label="Contributed by Tony Evers, Sr. Technical Architect, Adobe" type="Informative" url="https://www.linkedin.com/in/evers-tony/" tooltip="Contributed by Tony Evers"
role: Architect, Developer, User, Leader
level: Beginner, Intermediate
exl-id: ac63e31e-3047-410a-a6f9-a578b495bd8c
---
# The Bulk Packages global reference architecture pattern

This guide explains how to set up Adobe Commerce with the Bulk Packages Global Reference Architecture (GRA) Pattern.

The Bulk Packages GRA pattern involves a single Git repository to host all common customizations. This single Git repository is exposed through Composer as a single composer package, which contains multiple Adobe Commerce modules.

![A diagram showing where code is stored in a bulk packages GRA pattern](/help/assets/global-reference-architecture/bulk-gra-pattern-diagram.png){align="center"}

## Advantages and disadvantages of this pattern

Advantages:

- Code reuse through a shared code repository
- Flexibility to install different historical versions of the GRA on different instances, enabling phased releases
- Flexibility to backport and maintain multiple major versions of the GRA
- Support for semantic versioning of the GRA
- Simplicity, developers do not need more skills than in regular single store development patterns
- No special tooling, complex infrastructure or special branching strategy required
- The combination of packages in a release is always developed and tested together

Disadvantages:

- Only possible to upgrade the full GRA, including all packages contained in it.
- No support in the GRA bulk package for composer packages other than Adobe Commerce modules, language packs and themes, so no metapackages, magento2-component packages, Composer plugins and patches

## Set up Adobe Commerce with the Split Git GRA pattern

### The directory structure

The Bulk Packages GRA installs all reusable code through Composer repositories. Code that is specific to a single instance resides inside that instance's Git repository. Instance specific code is not reused in other instances of Adobe Commerce.

The final directory structure of a full Adobe Commerce installation with the Bulk Packages GRA pattern looks like this:

```text
.
├── app/
│   └── etc/
│       └── config.php
├── composer.json
├── composer.lock
└── packages/
    └── local/
```

The `app/code`, `app/i18n` and `app/design` directories are omitted on purpose, because Composer does not evaluate code in these directories. As a result, dependencies that are declared in the packages are not automatically installed. The Bulk Packages GRA pattern resolves this issue by installing some custom code in `packages/` and treating that directory as a composer repository. Composer symlinks packages inside `packages/` to `vendor/`.

### Prepare the Git repositories

Create two Git repositories for the shared GRA code and for the first store. Start with the GRA repository, which has the following file structure:

The result is the following directory structure:

```text
.
├── composer.json
└── src/
    ├── GraOne/
    │   ├── composer.json
    │   └── registration.php
    ├── GraTwo/
    │   ├── composer.json
    │   └── registration.php
    └── registration.php
```

This directory structure only mentions the composer.json file and registration.php file of the GraOne and GraTwo modules. In reality, there are more files inside these modules.

Run these commands to initiate the Git repository:

```bash
mkdir gra-bulk-foundation
cd gra-bulk-foundation
git init
git remote add origin git@github.com:AntonEvers/gra-bulk-foundation.git
vim composer.json # see code snippet below for contents
git add composer.json
git commit -m 'initialize GRA foundation repository'
git push -u origin main
```

The composer.json file contents:

```json
{
    "name": "antonevers/gra-bulk-foundation",
    "description": "Shared code repository",
    "type": "library",
    "license": [
        "OSL-3.0",
        "AFL-3.0"
    ],
    "require": {},
    "autoload": {
        "files": [
            "src/registration.php"
        ],
        "psr-0": {
            "": "src/"
        }
    }
}
```

Change the namespace of the composer.json package to your own namespace.

The src/registration.php file contents:

```php
<?php

declare(strict_types=1);

$pathList[] = dirname(__DIR__) . '/src/*/*/registration.php';
foreach ($pathList as $path) {
    $files = glob($path, GLOB_NOSORT | GLOB_ERR);
    if ($files === false) {
        throw new RuntimeException('glob() returned error while searching in \'' . $path . '\'');
    }
    foreach ($files as $file) {
        require_once $file;
    }
}
```

The registration.php file looks for other registration.php files inside the Adobe Commerce modules and executes them.

Create the two sample modules using the code in <https://github.com/AntonEvers/gra-bulk-foundation>. Composer does not evaluate the composer.json files in the sample modules. They are there as a habit. If you decide to move the modules to another place, the composer.json files become necessary again.

### Set up the store repository

The deployment repository contains the entire Adobe Commerce installation including the GRA code. Create the deployment repository:

```bash
mkdir gra-bulk-brand-x
cd gra-bulk-brand-x
composer create-project --repository-url=https://repo.magento.com/ magento/project-enterprise-edition .
git init
git remote add origin git@github.com:AntonEvers/gra-bulk-brand-x.git 
git add composer.json composer.lock
git commit -m 'initialize Brand X repository'
git push -u origin main
```

Install Adobe Commerce with `bin/magento setup:install`. Install the GRA sample modules in the deployment repository with Composer:

```bash
composer config repositories.gra-foundation vcs git@github.com:AntonEvers/gra-bulk-foundation.git
composer require antonevers/gra-bulk-foundation:@dev
bin/magento module:enable AntonEvers_GraOne AntonEvers_GraTwo
bin/magento test:gra-one
bin/magento test:gra-two
git add app/etc/config.php composer.json composer.lock
git commit -m 'install GRA foundation'
git push origin main
```

That last command should result in the following output to prove that the module is installed and working:

```bash
GRA One module is installed successfully and working!
GRA Two module is installed successfully and working!
```

You can create multiple bulk packages to organize code. For instance, a third-party bulk package for third-party code that is not available through Composer. Everything that you would traditionally install in `app/code` should now be in the `src/` directory of the bulk package. An exception to that rule is code that is only used in a single instance. These packages are called local packages.

### Install local packages

The deployment repository hosts local packages. They do not live in the GRA bulk package. The location of the local packages is not `app/code` but `packages/local`. Instruct Composer to treat this directory as a repository:

```bash
composer config repositories.local path 'packages/local/*/*'
git add composer.json
git commit -m 'initialize local composer package storage'
git push origin main
```

Add the example module that is hosted at <https://github.com/AntonEvers/module-example-local>:

```bash
mkdir -p packages/local
cd packages/local
mkdir antonevers
cd antonevers
curl -OL https://github.com/AntonEvers/module-example-local/archive/refs/heads/main.zip
unzip main.zip
rm main.zip
mv module-example-local-main module-local
git add module-local
cd ../../..
composer require antonevers/module-local:@dev
bin/magento module:enable AntonEvers_Local
bin/magento test:local
```

That last command should result in the following output to prove that the module is installed and working:

```bash
Local module is installed successfully and working!
```

Commit the local module to the brand repository:

```bash
git add packages/local/antonevers/module-local app/etc/config.php composer.json composer.lock 
git commit -m 'add local module'
git push origin main
```

## Overview of code locations

Only if the third-party does not offer installation through a Composer repository, you can store third-party modules in the `src/` directory of your foundation repository or a dedicated third-party bulk package.

- **Adobe Commerce core**: available through repo.magento.com.
- **Third-party modules**: available through the Marketplace or a vendor's own Composer repository.
- **Third-party modules fallback option**: stored in `src/` of a bulk package.
- **GRA foundation code**: stored in `src/` of the foundation bulk package.
- **Local code**: stored in the `packages/local` directory of the deployment repository.

## Develop a GRA module

Install the bulk package from source to enable Git in the bulk package directory:

```bash
rm -r vendor/antonevers/gra-bulk-foundation
composer install --prefer-source
```

The bulk package has been checked out using Git. When you enter the `vendor/antonevers/gra-bulk-foundation` directory, you are also entering the gra-bulk-foundation Git repository. You can create, checkout and merge branches in this directory.

Add Composer dependencies to the composer.json file at the root of the GRA bulk package, which is the only file in the bulk package that Composer evaluates.

## Include third-party modules to the GRA bulk package

Add third-party packages in the require section of the composer.json at the root of the GRA foundation to add them to your GRA. That way, the packages are always installed in all your instances through composer.

## Deliver your code

To deliver code to the main branch, there are 2 paths. First the local modules, which are merged to the main branch. Run Composer update for those modules. Do not allow developers to update composer.lock in their ticket branches to reduce conflicts. Only update the composer.lock file in staging and production branches, which reduces the risk of conflicts.

Secondly, the GRA bulk packages, which are merged into the main branch of the GRA bulk repository. Then you can add a Git tag to the main branch, versioning the Composer package. Require your new version of the GRA bulk package in the composer.json of the deployment repository to install it.

## Branching strategy

This GRA pattern works with all branching strategies so long as you mirror the branching strategy of the deployment repositories in your GRA bulk repository. For releases, create a release branch with the same name in both repositories. For development, create a ticket branch in both repositories.

In ticket branches, you should almost never have to update the composer.lock file. Just check out the right branches in your development environment for both the store and the GRA foundation repository with Git. The exception is when you update requirements in the GRA foundation composer.json file. Upgrading the GRA foundation in the deployment repository is only done when building the release, or when building a QA branch.

## Code examples

The code examples of this article are available as a set of Git repositories, which you can use to test the proof of concept.

- An example production store: <https://github.com/AntonEvers/gra-bulk-brand-x>
- The GRA code repository: <https://github.com/AntonEvers/gra-bulk-foundation>
- An example local module: <https://github.com/AntonEvers/module-example-local>
