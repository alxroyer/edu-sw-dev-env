<link rel="stylesheet" href="css/styles.css"></link>

<h1>Environnements de développement logiciel</h1>

![Banner](images/binary-code-7190628_1280.jpg)

Alexis ROYER - https://www.linkedin.com/in/alexis-royer/

2025-2026


---

Ce document constitue un cours d'ingénierie logicielle,
plus particulièrement sur la mise en oeuvre des environnements de développement.

L'environnement de développement contribue à l'efficience des activités,
et par conséquent à la qualité d'un logiciel produit,
d'où l'importance de maîtriser l'environnement de travail pour l'ensemble d'une équipe.

---

Source : https://github.com/alxroyer/edu-sw-dev-env/

Ce document est rédigé en format Markdown suivi sous git à dessein,
pour démontrer le format Markdown
et comment on peut l'utiliser pour la constitution de documentations techniques,
ainsi que les capacités de suivi de version et de travail collaboratif apportées par git sur un format texte.

---


Sommaire :

<!--
Mémo:
- Utilisation d'un titre HTML h1 en tête de document,
  pour éviter la confusion avec les titres de niveau 1 par l'extension "Auto Markdown TOC"
-->

<!-- TOC -->

- [1. Avant-propos](#1-avant-propos)
    - [1.1. Types de logiciel](#11-types-de-logiciel)
    - [1.2. Technos et langages](#12-technos-et-langages)
    - [1.3. Environnements de développement et qualité logicielle](#13-environnements-de-d%C3%A9veloppement-et-qualit%C3%A9-logicielle)
- [2. Développement](#2-d%C3%A9veloppement)
    - [2.1. IDE Integrated Development Environment](#21-ide-integrated-development-environment)
    - [2.2. Debugging](#22-debugging)
    - [2.3. Bibliothèques](#23-biblioth%C3%A8ques)
    - [2.4. Build](#24-build)
    - [2.5. Industrialisation](#25-industrialisation)
- [3. Exécution](#3-ex%C3%A9cution)
- [4. Assurance qualité](#4-assurance-qualit%C3%A9)
- [5. Delivery](#5-delivery)
    - [5.1. Enregistrements](#51-enregistrements)
    - [5.2. CI/CD](#52-cicd)
- [6. Déploiement](#6-d%C3%A9ploiement)

<!-- /TOC -->


# 1. Avant-propos

## 1.1. Types de logiciel

Avant toute chose, il convient de considérer que la mise en oeuvre d'un environnement de développement
est fortement dépendante du type de logiciel développé.

On distingue différents types de logiciels :
- <span class="sw-type pc"></span> les applications PC (Windows, Mac, Linux),
- <span class="sw-type web"></span> les applications web (front et back),
- <span class="sw-type mobile"></span> les applications mobile (Android, iPhone),
- <span class="sw-type embedded"></span> les logiciels embarqués.


## 1.2. Technos et langages

Pour chacun des types de logiciels, des technologies différentes peuvent être mises en jeu (liste non exhaustive) :
- <span class="sw-type pc"></span>
  Applications PC :
    - Langages :
        - C / C++
        - Java
        - Node.js (1) / Typescript (2)
        - Python
        - Go : exemple [esbuild](https://esbuild.github.io/faq/#why-is-esbuild-fast) (6)
        - Rust (3)
    - Systèmes d'exploitation :
        - Windows
        - Mac
        - Linux
    - Frameworks :
        - Qt (4)
        - React Native (4)
- <span class="sw-type web"></span>
  Applications web :
    - Langages :
        - HTML
        - Côté *frontend* :
            - Javascript / Typescript (2)
        - Côté *backend* :
            - Node.js (1) / Typescript (2)
            - Java
            - PHP
            - Ruby
            - Python
            - C / C++
            - Go (6)
    - Frameworks :
        - Angular (Javascript)
        - Vue.js (Javascript)
        - React Native (Javascript) (4)
        - Symfony (PHP)
        - Ruby on Rails
- <span class="sw-type mobile"></span>
  Applications mobiles :
    - Architectures / systèmes d'exploitation :
        - Android
        - iOS
    - Langages :
        - Java, Kotlin (Android)
        - Swift (iOS)
        - Objective-C (iOS)
        - C (Code natif Android & iOS)
    - Frameworks :
        - React Native (4)
    - Kits de développement :
        - SDK Android : Software Development Kit
        - NDK Android : Native Development Kit
- <span class="sw-type embedded"></span>
  Logiciels embarqués :
    - Langages :
        - C / C++
        - Go ? à confirmer (6)
        - Rust (3)
    - Systèmes d'exploitation :
        - Linux : couramment utilisé pour réaliser des systèmes embarqués. (5)
        - vxWorks : système d'exploitation dit *temps-réel*, propriétaire, développé par Wind River.
        - µC-OS : OS minimaliste, sans système de fichier, pile IP, ... par défaut.
        - Sans OS : simple boucle de réaction sur événement.
    - Frameworks / kits de développement :
        - buildroot

> Notes :
> - (1) Node.js : extension de Javascript, initialement restreint aux navigateurs, avec exécution par un moteur dédié.
> - (2) Typescript : extension de la syntaxe Javascript pour permettre le typage.
> - (3) Rust est un langage de programmation compilé, relativement nouveau,
>   dont un des objectifs principaux est la sécurisation de la gestion de la mémoire.
>   De fait, certains le présentent comme le successeur de C / C++.
> - (4) Certains frameworks ont l'avantage d'être *cross-platform*,
>   c'est à dire qu'ils permettent de réaliser un seul développement utilisable sur différents environnements
>   (plateformes et/ou systèmes d'exploitation).
> - (5) L'OS Linux, même dans une version embarquée, n'est pas considéré comme un OS *temps-réel*,
>   c'est-à-dire qu'il ne garantit pas un temps d'exécution pour un traitement donné.
>   L'occupation mémoire est plus importante que pour un OS minimaliste.
>   En revanche, il a l'avantage de fournir un écosystème riche de services et d'outils qui peut faciliter les développements.
> - (6) Go plebiscité pour ses capacités de gestion multi-thread,
    qui peut avoir son intrêt pour le développement d'applications avec des contraintes de perfs.
    Langage un peu spécifique, qui nécessite une phase d'apprentissage spécifique.

Le choix du langage et des technologies peut dépendre de plusieurs facteurs :
- en premier lieu, de la nature du logiciel développé,
- mais aussi des caractéristiques attendues :
  performances, empreinte mémoire, look & feel, ...
- de la culture d'entreprise : compétences disponibles en interne,
- de la stratégie d'entreprise :
  volonté d'investir sur telle ou telle technologie,
  ou de rationaliser les technologies utilisées, ...
- de la disponibilité des compétences sur le marché de l'emploi :
  capacité à staffer des équipes, assurer la maintenance dans le temps, ...
- ...

Quoi qu'il en soit, le langage et les technologies retenus
conditionnent fortement l'environnement de développement à mettre en place.

> ℹ️ **Vidéos pour le fun**
>
> Most popular coding language 2012 - 2024 :
> https://www.youtube.com/watch?v=viPKPhOUcyU
>
> Most Popular Programming Languages 1955 - 2025 :
> https://www.youtube.com/watch?v=5yAbVkIMl_M


## 1.3. Environnements de développement et qualité logicielle

La norme ISO 9126, ainsi que l'ISO 25010 qui la remplace aujourd'hui,
identifient différentes dimensions pour la caractérisation de la qualité d'un logiciel.
Entre autres (1) :
- Capacité fonctionnelle
- Facilité d'utilisation
- Fiabilité
- Performance
- Maintenabilité
- Portabilité

Une partie de ces dimensions reste essentiellement portée par le logciel développé.

Toutefois, l'environnement de développement peut contribue à certaines de ces dimensions, notamment :
- Fiabilité :
    - Mettre en oeuvre des outils d'analyse de code statique, permettant d'éviter des bugs avant même d'exécuter le code.
    - Exécuter régulièrement des tests de non-régression, pour détecter les problèmes au plus tôt.
- Maintenabilité :
    - Assurer un maximum de confort pour les développeurs, de sorte à faciliter le codage, le debugging...
      de par le choix des outils, pour leurs fonctionnalités, et sans oublier leurs performances !
      Faire en sorte de limiter les freins aux différentes actions nécessaires à la réalisation d'un logiciel de qualité.
    - Faciliter notamment les refactorings, nécessaires à la maintenabilité.
    - Utiliser un outil de versioning (git).
    - Automatiser les vérifications de qualité (linters, indentation) pour s'assurer d'un certain niveau de lisibilité du code,
      donc un code plus facile à maintenir, à suivre en historique.
- Portabilité :
    - Exécution des tests de non-régression sur les différentes cibles.

> ℹ️ **(1) Accès aux normes ISO**
>
> La difficulté des normes ISO est que celles-ci ne sont pas libres d'accès.
>
> En effet, le site de référence de l'ISO ne fournit qu'une prévisualisation
> de la version en cours de la norme ISO 25010 :
> https://www.iso.org/obp/ui/#iso:std:iso-iec:25010
>> *To view the full content, you will need to purchase the standard by clicking on the "Buy" button.*
>
> Toujours sur le site de référence,
> difficile de trouver une telle prévisualisation pour l'ISO 9126.
>
> La liste simplifiée ci-dessus est tirée de la page Wikipédia https://fr.wikipedia.org/wiki/Qualit%C3%A9_logicielle


# 2. Développement

Avant de délivrer et exécuter le logiciel, commençons par mettre en oeuvre les éléments permettant de le construire.


## 2.1. IDE (*Integrated Development Environment*)

Un des premiers outils qu'on est amené à aborder pour faire du développement logiciel est l'IDE.

L'usage d'un IDE présente de nombreux intérêts :

- Edition de code :
  Basique, un simple notepad (voire `vi` pour les puristes !)
  pourrait faire le job.

- Coloration syntaxique :
  Ca change déjà un peu la vie,
  dans la mesure où ça fluidifie la lecture du code.

- Navigation :
  Capacité à aller directement sur le code d'une variable ou d'une fonction,
  ou dans le code Markdown d'un chapitre donné.
  Possibilité de gagner du temps,
  en évitant de scroller et de faire des CTRL+F dans tous les sens
  quand le code commence à prendre du volume.

- Complétion :
  La complétion apporte un vrai plus,
  en évitant des fautes de frappe
  donc des erreurs chronophages au passage.

  > ⚠️ **Attention : Complétion et fautes d'orthographe**
  >
  > Il existe un risque avec la complétion de répliquer
  > des fautes d'orthographe ou des dyslexies
  > sur les noms de variables ou de fonctions
  > dans la totalité de code.
  >
  > Le cas échéant, avoir le réflexe d'utiliser les fonction de refactoring
  > pour corriger le tir.

- Refactoring :
  On gagne encore plus du temps.
  On n'hésite plus à renommer une variable, une fonction, une classe,
  pour lui redonner un nom plus adapté, allant dans le sens de la maintenabilité.

- Edition multi-lignes :
  Capacité mise à disposition par un certain nombre d'éditeurs de texte,
  à laquelle on s'habitue très vite dès lors qu'on commence à l'utiliser.

- Debugging :
  Dès lors que c'est possible,
  permet d'obtenir plein d'informations utiles
  dans le cadre de résolution d'un bug.
  Possibilité également d'utiliser les fonctions de debugging
  pour tester des injections de fautes.

- IA :
  Les IDE intègrent aujourd'hui des fonctions d'IA
  qui peuvent augmenter la productivité.

  > ⚠️ **Attention : IA et confidentialité**
  >
  > A ce jour, l'IA fonctionne principalement par communication d'informations sur des moteurs s'exécutant sur Internet.
  >
  > L'utilisation de l'IA dans les IDE peut donc être problématique si l'entreprise ne souhaite pas divulguer le code.
  >
  > Bien se renseigner sur les usages possibles ou non.
  >
  > Possible que l'entreprise dispose d'un contrat de confidentialité avec une IA donnée,
  > voire héberge une solution d'IA *on premise*,
  > auquel cas on pourra configurer les IDE pour utiliser cette IA validée par l'entreprise.

On liste ci-après des IDE connus (liste non exhaustive) :
- <span class="sw-type pc"></span> Applications PC :
    - Visual C++
    - Eclipse : Java, mais aussi C / C++ (version CDT)
    - VS Code : Node.js, Typescript, mais aussi C / C++ (extension)
    - JetBrains IntelliJ IDEA : Java
    - JetBrains PyCharm : Python
- <span class="sw-type web"></span> Applications web :
    - VS Code : HTML, Javascript, Typescript, PHP
    - PHPStorm
    - JetBrains IntelliJ IDEA : Java
- <span class="sw-type mobile"></span> Applications mobile :
    - Android Studio
    - JetBrains IntelliJ IDEA : Java, Kotlin
    - XCode : iOS
- <span class="sw-type embedded"></span> Logiciel embarqué :
    - VS Code : C / C++ (extension), Rust (extension)
    - Eclipse : C / C++ (version CDT)

> <span class="sw-type pc"></span> 👷 TP : [Configuration d'un IDE VS Code pour C/C++](TP%20-%20IDE%20VS%20Code%20C-Cpp.md)

> 👷 TP : Refactoring (TODO)


## 2.2. Debugging

> ℹ️ **Note**
>
> On parle de debugging dès à présent,
> car c'est une des fonctions majeures apportées par un IDE
> facilitant l'investigation et la résolution de bugs logiciels.
>
> Cela entend qu'on sait exécuter notre logiciel au préalable
> (cf. [§ Exécution](#3-ex%C3%A9cution)).
> La notion reste toutefois abordable
> en considérant le cas simple des applications PC dans un premier temps.

Les débuggers (tels `gdb`) peuvent généralement s'utiliser en ligne de commande.
Toutefois, cela reste extrêmement compliqué,
et l'utilisation d'une interface graphique est quasiment indispensable pour débugguer efficacement.

Les IDE intègrent très bien les débuggeurs,
et permettent ainsi de basculer très rapidement entre les modes édition de code et debugging / intégration.

Parmi les fonctions utiles d'un debugger, on note :
- la possibilité de positionner des points d'arrêt (*breakpoints*)
- l'exécution pas à pas, i.e. ligne à ligne,
- l'observation des valeurs de variables,
- rentrer dans l'exécution des fonctions (et en ressortir)
- l'affichage de la pile d'appels (*callstack*)
- la possibilité de définir un point d'arrêt sur modification de valeur :
  très utile pour investiguer des problèmes de débordement mémoire
- la capacité à modifier des valeurs de données :
  utile pour tester des injections de fautes
- la capacité pour certains langages interprétés (Python, JS) à pouvoir exécuter des routines à chaud
- ...

> <span class="sw-type pc"></span> 👷 TP : [Debugging C/C++ avec VS Code](TP%20-%20Debugging%20VS%20Code%20C-Cpp.md)

Dans le cas du debugging d'un logiciel embarqué, la difficulté est de savoir synchroniser
un IDE/debugger qui tourne sur une machine de développement,
et le programme à débugguer qui tourne sur une cible autre.
Pour ce faire, on peut utiliser des moyens spécifiques :
- `gdbserver` :
    - Possible pour des cibles tournant sous Linux uniquement.
    - Le programme à débugguer est lancé sur la cible avec `gdbserver`,
      et le debugger sur la machine de développement se connecte au `gdbserver` en tant que client.
    - J'ai déjà constaté personnellement que la connexion pouvait être instable.
      Pas de garantie notamment que les points d'arrêts soient bien pris en compte,
      notamment dans des cas d'applicatifs multi-threadés.
- Utilisation d'une sonde :
    - Matériel de sonde spécifique au micro-processeur de la cible.
    - Branchement sur un bus série dédié, directement sur le micro-processeur sur la cible.
      Nécessite que les signaux aient été routés sur la carte.

> <span class="sw-type embedded"></span> 👷 TP : Debugging C/C++ à distance avec gdbserver (TODO)

On note finalement que les investigations par debugging ont leurs limitent :
- Pas de debugging possible *post-mortem*,
  i.e. après constat d'un problème après que l'exécution du logiciel soit terminée
  (cas typique d'une exception ou d'un crash constaté en prod)
  et tant qu'on n'a pas caractérisé les conditions de reproduction du problème.
- Il arrive fréquemment que le fait de poser des points d'arrêts provoque des effets de bords
  sur des timeouts qui arrivent à échéance, et donc des effets indésirables empêchant un debugging confortable.
- Dans le cas des logiciels embarqués, comme le logiciel s'exécute sur une cible autre,
  le debugging est par nature moins facile à mettre en oeuvre.
- Cas en Python où le débuggueur exécute automatiquement des routines `__repr__()`
  pour obtenir une représentation des représentation des objets
  à afficher dans l'IHM de debug,
  ces exécutions surnuméraires pouvant provoquer des effets de bords indésirables selon les cas.

En raison de ces limitations, la bonne vieille technique du debugging "à la trace" ne doit pas être négligée.

Plus encore, il convient de mettre en place un système de logs efficace dès le début du projet,
avec quelques fonctions utiles :
- Niveaux de criticité : debug, info, warning, erreur classiquement.
- Colorisation : savoir faire apparaître les erreurs en rouge a minima.
- Indentation : utile pour analyser les logs de traitements récursifs.
- Filtrages : par fonction, par module.

L'utilisation d'outils tels que Kibana peut également s'avérer utile
pour exploiter ces logs.


## 2.3. Bibliothèques

## 2.4. Build

## 2.5. Industrialisation

La constitution d'images Docker
embarquant des versions d'outils bien identifiées
contribue à la maîtrise de l'environnement de développement.

Grâce à ces images,
on peut répéter facilement une configuration de développement,
pour chaque membre de l'équipe,
ainsi que pour la chaîne de CI/CD,
et avec l'assurance d'utiliser les mêmes versions des outils.


# 3. Exécution

Dès les premières versions de notre logiciel disponibles,
il s'avère intéressant de savoir exécuter notre production aux différentes étapes de sa construction :
- en cours de développement, pour des tests unitaires, ou tests d'intégration libres,
- sur des versions intermédiaires, pour des tests de non-régression quotidiens par exemple,
- sur des versions identifiées, pour des campagnes de test avant livraison.


# 4. Assurance qualité


# 5. Delivery

## 5.1. Enregistrements

## 5.2. CI/CD


# 6. Déploiement
