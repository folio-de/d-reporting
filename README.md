# d-reporting

[![de](https://img.shields.io/badge/lang-de-blue.svg)](README.de.md)

Copyright (C) 2024 The Open Library Foundation

This software is distributed under the terms of the Apache License, Version 2.0. See the file "[LICENSE](LICENSE)" for more information.

# Overview

This is a shared repository of the German FOLIO community for FOLIO reporting. It contains SQL files for database queries and other files for alternative reporting techniques designed for FOLIO. Most of the content here consists of files developed by the FOLIO reporting community and based on the requirements of the German FOLIO community. The focus of the repository is on German library statistics (DBS).

# Contributing

Everyone is welcome to submit contributions. Please read our guidelines in "[Contributing.md](Contributing.md)".

# How to use this repository?

The repository is to be understood as a shared storage of files that can be used when necessary. In some cases, certain directories can possibly be integrated in programs and thus enable automated reuse. In these cases, we assume no guarantee or liability for proper operation (see also "[LICENSE](LICENSE)"). 

Detailed documentation for using the files can be found on the repository's wiki.

# Versioning

## Branches

There are two main types of branches:

* `main` This is a development branch where new features are first merged. This branch is relatively unstable. The branch is the default view on GitHub.
* Release branches (`release-*`). These are releases from `main`. They are stable branches; That means they may get bug fixes, but generally not new features. Production systems should use one of these branches.

## Releases

Releases are published as separate branches. These release branches (`release-*`) are numbered in ascending order. There are no specific periods or dates when a release will appear. The FOLIO reporting community decides the releases dates together.
