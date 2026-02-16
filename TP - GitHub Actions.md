<link rel="stylesheet" href="css/styles.css"></link>

<h1>GitHub Actions</h1>


L'objectif de ce TP est de démontrer les capacités de CI/CD avec GitHub Actions.

La documentation et les tutoriaux GitHub étant bien fournis,
on se contentera ici de pointer vers ces ressources.


<!-- TOC -->

- [1. Prérequis](#1-pr%C3%A9requis)
- [2. GitHub Actions, qu'est-ce que c'est ?](#2-github-actions-quest-ce-que-cest-)
- [3. Continuous Integration](#3-continuous-integration)
- [4. Continuous Deployment](#4-continuous-deployment)
- [5. Fonctionnalités avancées](#5-fonctionnalit%C3%A9s-avanc%C3%A9es)
- [6. Annexes](#6-annexes)
    - [6.1. Documentation utile](#61-documentation-utile)

<!-- /TOC -->


# 1. Prérequis

- Disposer d'un compte GitHub (cf. TP [GitHub](TP%20-%20GitHub.md) pour la configuration du compte).


# 2. GitHub Actions, qu'est-ce que c'est ?

Documentation :
- https://github.com/features/actions
- https://docs.github.com/en/actions/get-started/quickstart, jusqu'à "Creating your first workflow"
- https://docs.github.com/en/actions/get-started/understand-github-actions
- Parcourir en diagonal le sommaire de la documentation de référence : https://docs.github.com/en/actions/reference
- Prendre connaissance de quelques notions / fonctionnalités :
    - Runners : https://docs.github.com/en/actions/reference/runners
    - Artéfacts : https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts
    - Notifications : https://docs.github.com/en/actions/concepts/workflows-and-actions/notifications-for-workflow-runs

Tutoriels :
- https://docs.github.com/en/actions/tutorials/create-an-example-workflow


# 3. Continuous Integration

Documentation :
- https://docs.github.com/en/actions/get-started/continuous-integration

Tutoriels :
- https://docs.github.com/en/actions/tutorials/build-and-test-code,
  choisir un ou plusieurs des tutoriels suivants :
    - Java avec Maven : https://docs.github.com/en/actions/tutorials/build-and-test-code/java-with-maven
    - Node.js : https://docs.github.com/en/actions/tutorials/build-and-test-code/nodejs
    - Python : https://docs.github.com/en/actions/tutorials/build-and-test-code/python
    - Rust : https://docs.github.com/en/actions/tutorials/build-and-test-code/rust
    - Go : https://docs.github.com/en/actions/tutorials/build-and-test-code/go


# 4. Continuous Deployment

Documentation:
- https://docs.github.com/en/actions/get-started/continuous-deployment

Tutoriels :
- Publier un package Java avec Maven : https://docs.github.com/en/actions/tutorials/publish-packages/publish-java-packages-with-maven
- Publier un package Node.js : https://docs.github.com/en/actions/tutorials/publish-packages/publish-nodejs-packages
- Publier une image Docker : https://docs.github.com/en/actions/tutorials/publish-packages/publish-docker-images


# 5. Fonctionnalités avancées

- Artéfacts : https://docs.github.com/en/actions/tutorials/store-and-share-data
- Créer des actions plus complexes :
    - Action Javascript : https://docs.github.com/en/actions/tutorials/create-actions/create-a-javascript-action
    - Action composite : https://docs.github.com/en/actions/tutorials/create-actions/create-a-composite-action
    - Action Docker : https://docs.github.com/en/actions/tutorials/use-containerized-services/create-a-docker-container-action
- Créer des services Dockers : https://docs.github.com/en/actions/tutorials/use-containerized-services/use-docker-service-containers
    - PostgreSQL : https://docs.github.com/en/actions/tutorials/use-containerized-services/create-postgresql-service-containers
    - Redis : https://docs.github.com/en/actions/tutorials/use-containerized-services/create-redis-service-containers


# 6. Annexes

## 6.1. Documentation utile

- Espace GitHub Actions : https://docs.github.com/en/actions
- Documentation de référence : https://docs.github.com/en/actions/reference
- Tutoriels : https://docs.github.com/en/actions/tutorials
