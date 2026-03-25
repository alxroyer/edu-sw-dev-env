<link rel="stylesheet" href="css/styles.css"></link>

<h1>Configuration d'un IDE VS Code pour C/C++ en mode remote</h1>


Il existe des cas où on souhaite / doit, travailler sur du code accessible à distance via SSH :
- Postes en Windows lié à la DSI d'entreprise, mais des développements sous Linux, donc sur des machines dédiées.
- Simplification de la gestion de l'environnement de développement via des conteneurs Dockers.
- ...

Dans ce genre de situation,
on peut se connecter en SSH,
puis faire un *export display* d'un VS Code lancé sur la machine distante.
Mais cela utilise beaucoup de mémoire,
et la fluidité n'est souvent pas au rendez-vous.

VS Code propose également la possibilité de travailler à distance,
en lançant VS Code sur la machine Windows,
VS Code travaillant via SSH sur la machine distante.


<!-- TOC -->

- [1. Configuration VS Code en mode remote](#1-configuration-vs-code-en-mode-remote)
- [2. Annexes](#2-annexes)
    - [2.1. Documentation utile](#21-documentation-utile)

<!-- /TOC -->


# 1. Configuration VS Code en mode remote

Créer une image Docker embarquant une installation mingw ou gcc/g++.

A partir de cette image, créer un conteneur disposant du code du [TP - IDE VS Code C-Cpp.md](TP%20-%20IDE%20VS%20Code%20C-Cpp.md).

A l'aide de la documentation officielle,
configurer VS Code en local de sorte à ce que ce dernier puisse :

- accéder au code,
- compiler,
- exécuter,
- débugguer

à distance dans le conteneur.

TODO : Détailler les étapes.


# 2. Annexes

## 2.1. Documentation utile

Documentation officielle VS Code :
- https://code.visualstudio.com/docs/languages/cpp#_remote-development
