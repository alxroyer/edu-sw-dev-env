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


# 1. Hello World à distance

A l'aide de la documentation officielle: https://code.visualstudio.com/docs/languages/cpp#_remote-development,
reprendre l'exemple du Hello World
avec une conteneur Docker
tiré d'une image embarquant une installation mingw
(bien identifiée et déjà prête, d'où le gain en maîtrise sur l'environnement de développement).
