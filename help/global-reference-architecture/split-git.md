---
title: How do you leverage Global Reference Architecture
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

# The Split Git global reference architecture pattern

This guide explains how to set up Adobe Commerce with the Split Git Global Reference Architecture (GRA) Pattern.

The split Git GRA pattern involves two Git repositories for development and one Git repository per Adobe Commerce instance. In the examples, it is assumed that each instance represents a unique brand.

![A diagram showing where code is stored in a split GRA pattern](/help/assets/global-reference-architecture/split-git-gra-pattern-diagram.png){align="center"}

## Advantages and disadvantages of this pattern

Advantages:

- Code reuse through a shared code repository
- Simple GRA pattern, suitable even for teams with limited Composer knowledge
- In addition to Adobe Commerce modules, themes and language packs, it is possible to install any type of Composer package through this model, including composer-plugin, composer-metapackage, magento2-component and patches
- Possible to release in phases, planning releases to regions in their own maintenance windows
- Support for Git tags for administration purposes, not for deployment control
- Guarantee that the combination of packages in a production deployment is developed and tested in this exact configuration

Disadvantages:

- No added flexibility compared to other GRA patterns
- Not possible to upgrade or downgrade individual modules per instance, always upgrade or downgrade the GRA as a whole
- In most cases, the bulk packages pattern is a better fit as it is equally simple, but more conventional

## Setting up Adobe Commerce with the Split Git GRA pattern

### The directory structure

The Split Git GRA pattern has two types of repositories; development repositories and installation repositories. The development repositories only contain part of a full Adobe Commerce installation. The installation repositories contain the full Adobe Commerce installation and are used for deployment, but not for development.

The final directory structure of a full Adobe Commerce installation with the Split Git GRA pattern looks like this:

```text
.
├── .gitignore
├── app/
│   └── etc/
│       └── config.php
├── composer.json
├── composer.lock
└── packages/
    ├── 3rdparty/
    ├── gra/
    └── local/
```

The `app/code`, `app/i18n` and `app/design` directories are omitted on purpose, because Composer does not evaluate code in these directories. As a result, dependencies that are declared in the packages are not automatically installed. The Split Git GRA pattern resolves this issue by installing all custom code in `packages/` and treating that directory as a composer repository. Composer symlinks packages inside `packages/` to `vendor/`.

## Preparing the Git repositories

Create 3 Git repositories for:

1. An Adobe Commerce instance
2. Third-party code that is not installed through Composer
3. Your customizations in the form of modules, themes, language packs and such; your GRA

In this guide the following names are used for these repositories:

1. gra-split-brand-x
2. gra-split-3rdparty
3. gra-split-gra

All repositories in the Split Git GRA pattern are merged into one. For Git to allow merging multiple repositories, all three repositories need a shared history. Create a Git project with a single commit and push it to all remotes.

```bash
mkdir gra-split-brand-x
cd gra-split-brand-x
git init
git remote add origin git@github.com:AntonEvers/gra-split-brand-x.git
git remote add 3rdparty git@github.com:AntonEvers/gra-split-3rdparty.git
git remote add gra git@github.com:AntonEvers/gra-split-gra.git
touch .gitkeep
git add .gitkeep
git commit -m 'initialize repository'
git push -u origin main
git push 3rdparty main
git push gra main
```

Pushing the temporary file `.gitkeep` to all remotes creates the same initial commit with the same commit hash, making a shared history. Each change that is created in one remote can be merged to the others.

From here, the repositories diverge. The gra-split-brand-x repository contains brand specific code. The gra-split-3rdparty repository contains only third-party code. The gra-split-gra repository contains only your global reference architecture foundation, which consists of all your custom code.

Install Adobe Commerce in the gra-split-brand-x repository.

```bash
composer create-project --no-install --repository-url=https://repo.magento.com/ magento/project-enterprise-edition temp
mv temp/composer.json ./
rmdir temp
git add composer.json
git commit -m 'install Adobe Commerce'
git push origin main
```

Create initial commits in the gra-split-3rdparty and the gra-split-gra repositories. The easiest way is by checking out these repositories in separate directories.

```bash
cd ..
git clone git@github.com:AntonEvers/gra-split-3rdparty.git
git clone git@github.com:AntonEvers/gra-split-gra.git
cd gra-split-3rdparty
mkdir -p packages/3rdparty
touch packages/3rdparty/.gitkeep
git add packages/3rdparty/.gitkeep
git commit -m 'initialize 3rd party package storage'
git push origin main
cd ../gra-split-gra
mkdir -p packages/gra
touch packages/gra/.gitkeep
git add packages/gra/.gitkeep
git commit -m 'initialize GRA package storage'
git push origin main
```

These two repositories store third-party packages and GRA packages. There may be code that is exclusive to each instance of Adobe Commerce. Create a place to store these local packages in the gra-split-brand-x repository.

```bash
cd ../gra-split-brand-x
mkdir -p packages/local
touch packages/local/.gitkeep
git add packages/local/.gitkeep
git commit -m 'initialize local package storage'
git push origin main
```

## Where to store different types of code

Adobe Commerce is a Composer application. The preferred way to install is always through Composer repositories. Only if a module vendor does not offer installation through a Composer repository, you can store third-party modules in the third-party repository. The preferred place for custom code is in the GRA repository. When a module is only used by one specific instance, it becomes local code.

Summarizing:

- **Adobe Commerce**: stored in a Composer repository.
- **Third-party modules**: stored in a Composer repository.
- **Third-party modules fallback option**: stored in the gra-split-3rdparty Git repository.
- **GRA foundation code**: stored in the gra-split-gra Git repository.
- **Local code**: stored in the gra-split-brand-x Git repository.

## Connect package storage to Composer

Composer can treat the packages directory as a composer repository. Inform Composer about the location of packages inside the packages directory.

```json
"repositories": [
  {"type": "path", "url": "packages/local/*/*"},
  {"type": "path", "url": "packages/gra/*/*"},
  {"type": "path", "url": "packages/3rdparty/*/*"},
  {"type": "composer", "url": "https://repo.magento.com"}
]
```

Composer looks for composer.json files two levels deep in the three storage directories. Create subdirectories inside the three code storage directories exactly like they would appear in the `vendor/` directory.

For instance: If a package is normally installed in `vendor/example-corp/module-example/`, then you store it in `packages/3rdparty/example-corp/module-example/`. Composer symlinks the package to `vendor/example-corp/module-example/` when you require it.

Use the composer package namespace and name as the directory structure. For instance: a module that traditionally exists in `app/code/MyCorp/MyCustomization/` has the name `my-corp/module-my-customization` in composer.json. Store this package in `packages/gra/my-corp/module-my-customization`.

## Include new packages in the instance repositories

Merge packages from the third-party and GRA remotes into the gra-split-brand-x repository.

```bash
cd gra-split-brand-x
git fetch - all
git merge gra/main 3rdparty/main
git push origin main
```

The result is the following directory structure:

```text
.
├── composer.json
└── packages/
    ├── 3rdparty/
    ├── gra/
    └── local/
```

Changes in the third-party and GRA foundation repository are merged into the brand repositories. This way third-party and GRA code are only maintained in one place. Move the changes to the brands with a Git merge.

Adobe Commerce does not automatically recognize new modules. Run composer require to add a new package after a merge. Run composer update every time you update one of your packages after a merge.

## Install example modules

As a proof of concept, install example modules to see how the GRA pattern works.

Run `composer install` and `bin/magento install` before moving on.

There are 3 test modules for on GitHub:

1. [module-example-local](https://github.com/AntonEvers/module-example-local)
2. [module-example-gra](https://github.com/AntonEvers/module-example-gra)
3. [module-example-3rdparty](https://github.com/AntonEvers/module-example-3rdparty)

### Install a local module

Adding a module to the local code pool is simple. Download and extract the module. Require it with Composer. Enable it with `bin/magento` and commit the files in the brand repository.

```bash
cd gra-split-brand-x
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

If you see the output above, then you can safely commit it to the brand repository.

```bash
git add packages/local/antonevers/module-local app/etc/config.php composer.json composer.lock 
git commit -m 'add local module'
git push origin main
```

## Install and develop a GRA foundation module

Adding a module to the GRA repository is different from installing local modules. By default, commits are added to origin/main, which is the gra-split-brand-x repository. Changes to GRA modules should be pushed to the gra-split-gra repository and merged into the gra-split-brand-x repository afterwards.

### Create a development environment

Create a development environment with a combination of all code pools in one place. You can push code to the local, GRA and third-party repository individually through symlinks. Start by creating a new development directory next to your brand, GRA and third-party repo directories.

```text
.
├── gra-development    # <---
├── gra-split-3rdparty
├── gra-split-brand-x
└── gra-split-gra
```

```bash
cd ..
mkdir gra-development
cd gra-development
cp ../gra-split-brand-x/composer.json ../gra-split-brand-x/composer.lock .
mkdir packages
ln -s ../../gra-split-brand-x/packages/local/ packages/
ln -s ../../gra-split-3rdparty/packages/3rdparty/ packages/
ln -s ../../gra-split-gra/packages/gra/ packages/
```

The result is the following directory structure:

```text
.
├── packages/
│ ├── 3rdparty -> ../../gra-split-3rdparty/packages/3rdparty/
│ ├── gra -> ../../gra-split-gra/packages/gra/
│ └── local -> ../../gra-split-brand-x/packages/local/
├── composer.lock
└── composer.json
```

Run `composer install` and `bin/magento install` in the gra-development directory.

It is now possible to commit changes directly from the `packages/3rdparty`, `packages/gra` and `package/local` directories. Git commits the changes to the Git repository that the directories symlink to. It is important that the git commit command is issued inside the `packages/3rdparty`, `packages/gra` or `package/local` directory. Do not run git commit at the project root.

### Install example modules

Install the third-party and GRA example modules in the packages directories.

```bash
cd packages/gra
mkdir antonevers
cd antonevers
curl -OL https://github.com/AntonEvers/module-example-gra/archive/refs/heads/main.zip
unzip main.zip
rm main.zip
mv module-example-gra-main module-gra
git add module-gra
 
cd ../../3rdparty
mkdir antonevers
cd antonevers
curl -OL https://github.com/AntonEvers/module-example-3rdparty/archive/refs/heads/main.zip
unzip main.zip
rm main.zip
mv module-example-3rdparty-main module-3rdparty
git add module-3rdparty
 
cd ../../..
composer require antonevers/module-gra:@dev antonevers/module-3rdparty:@dev
bin/magento module:enable AntonEvers_Gra AntonEvers_ThirdParty
bin/magento test:gra
bin/magento test:3rdparty
```

That last command should result in the following output to prove that the module is installed and working:

```bash
GRA module is installed successfully and working!
3rd party module is installed successfully and working!
```

If you see the output above, then you can safely commit it to the brand repository. Run `git remote -v` to verify that you are committing to the right remote.

```bash
cd packages/gra
git remote -v 
origin git@github.com:AntonEvers/gra-split-gra.git (fetch)
origin git@github.com:AntonEvers/gra-split-gra.git (push)
git add antonevers/module-gra
git commit -m 'add GRA module'
git push origin main
 
cd ../3rdparty
git remote -v 
origin git@github.com:AntonEvers/gra-split-3rdparty.git (fetch)
origin git@github.com:AntonEvers/gra-split-3rdparty.git (push)
git add antonevers/module-3rdparty
git commit -m 'add third-party module'
git push origin main
```

## Deliver code to the instances

Merge the GRA and third-party repositories to the gra-split-brand-x repository to deliver the code to an Adobe Commerce instance. Run `composer require`, `bin/magento module:enable` and commit the result.

```bash
cd gra-split-brand-x
git fetch - all
git merge gra/main 3rdparty/main
composer require antonevers/module-gra:@dev antonevers/module-3rdparty:@dev
bin/magento module:enable AntonEvers_Gra AntonEvers_ThirdParty
git add app/etc/config.php composer.lock composer.json
git commit -m 'install GRA and third-party modules'
git push origin main
```

## Branching strategy

This GRA pattern works with all branching strategies, if you mirror the branching strategy of the store repositories in your third-party and GRA repositories. For releases, create a release branch with the same name in all three repositories. Merge the release branches together on the store repository during release preparation.

Sometimes you have a ticket branch that requires both local code and third-party code or GRA code to be altered. In this case, the ticket branches need to be created in all related repositories.

Never merge third-party and GRA commits into the brand repository inside ticket branches. Instead, check out the right branches in your development environment for each code pool. Merging into the brand repository is only done when composing the release, or when composing a QA branch.

## Code examples

The code examples of this article are available as a set of Git repositories, which you can use to test the proof of concept.

- An example production store: https://github.com/AntonEvers/gra-split-brand-x
- The third-party code repository: https://github.com/AntonEvers/gra-split-3rdparty
- The GRA code repository: https://github.com/AntonEvers/gra-split-gra
- An example local module: https://github.com/AntonEvers/module-example-local
- An example GRA module: https://github.com/AntonEvers/module-example-gra
- An example third-party module: https://github.com/AntonEvers/module-example-3rdparty
