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
