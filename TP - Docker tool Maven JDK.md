<link rel="stylesheet" href="css/styles.css"></link>

<h1>Utiliser Docker pour compiler un programme Java</h1>


Ce TP montre comment on peut utiliser Docker pour disposer d'outils de développement dans différentes versions,
Maven et le JDK en l'occurrence,
sans impacter la configuration système de la machine de développement.


<!-- TOC -->

- [1. Prérequis](#1-pr%C3%A9requis)
- [2. Téléchargement du programme Java d'exemple](#2-t%C3%A9l%C3%A9chargement-du-programme-java-dexemple)
- [3. Compilations avec Docker](#3-compilations-avec-docker)
    - [3.1. Vérifier l'existence d'un JDK ou non sur la machine de développement](#31-v%C3%A9rifier-lexistence-dun-jdk-ou-non-sur-la-machine-de-d%C3%A9veloppement)
    - [3.2. Compiler avec Java 17](#32-compiler-avec-java-17)
    - [3.3. Compiler avec Java 21](#33-compiler-avec-java-21)
    - [3.4. Conclusion](#34-conclusion)
- [4. Annexes](#4-annexes)
    - [4.1. Documentation utile](#41-documentation-utile)

<!-- /TOC -->


# 1. Prérequis

Sur la machine de développement :
- Disposer de git.
- Disposer de docker.
- Disposer d'une JRE (mais pas forcément d'un JDK).

> 💡 **`docker` & Linux : `sudo` or not `sudo`**
>
> Pour éviter d'avoir à passer les commandes `docker` avec `sudo` sous Linux,
> ajouter l'utilisateur au groupe `docker` :
> ```bash
> sudo usermod --append --groups docker $(whoami)
> ```
>
> Il semble ensuite qu'un redémarrage soit nécessaire
> pour que la configuration de groupe soit prise en compte par le système.
>
> Ressources :
> - https://stackoverflow.com/questions/51218233/docker-why-do-i-need-to-sudo-in-linux#51218264
> - https://stackoverflow.com/questions/48957195/how-to-fix-docker-permission-denied#48957722


# 2. Téléchargement du programme Java d'exemple

Cloner le programme d'exemple `simple-java-maven-app.git` fourni par le projet Jenkins :
```bash
git clone https://github.com/jenkins-docs/simple-java-maven-app.git
cd simple-java-maven-app
```


# 3. Compilations avec Docker

## 3.1. Vérifier l'existence d'un JDK ou non sur la machine de développement

Vérifier si un JDK est installé sur le système :
```bash
which javac
```

Si `javac` est bien présent, identifier la version installée :
```bash
javac -version
```


## 3.2. Compiler avec Java 17

Qu'un JDK soit installé ou non,
et quelle que soit sa version,
on va tenter de compiler le projet avec un SDK 17.

Pour ce faire,
on va utiliser les images Docker publiées par le projet Apache Maven :
https://hub.docker.com/_/maven

Dans la section "Supported tags and respective Dockerfile links",
on peut repérer des images "temurin-17".
La dernière en date (à l'heure où on écrit ces lignes)
avec une version officielle de Maven est la `3.9.12-eclipse-temurin-17`

TODO :
- Expliquer le fonctionnement des raccourcis de noms de tags, d'où les hash qui se retrouvent.
- Expliquer l'intérêt d'être le plus spécifiant possible sur les noms de versions,
  pour figer / maîtriser la version utilisée,
  même si de nouvelles images seraient publiées ultérieurement.

On lance la commande suivante :
```bash
docker run --rm -v "$PWD":/usr/src/mymaven -w /usr/src/mymaven maven:3.9.12-eclipse-temurin-17 mvn clean package
```

Explications de la commande :
- `docker run`

  D'après `docker run --help` :
  "Create and run a new container from an image",

- `--rm` :

  Toujours d'après `docker run --help` :
  "Automatically remove the container and its associated anonymous volumes when it exits",

- `-v "$PWD":/usr/src/mymaven`

  Permet de monter de monter le répertoire courant (`$PWD`)
  contenant les sources du projet Java téléchargé au [§2](#2-t%C3%A9l%C3%A9chargement-du-programme-java-dexemple),
  en tant que `/usr/src/mymaven` dans le conteneur Docker.

- `-w /usr/src/mymaven`

  L'option `-w` ou `--workdir` permet de spécifier le répertoire courant à l'intérieur du contenenur Docker.

  En l'occurrence, on donne comme chemin le répertoire `/usr/src/mymaven`
  sur lequel on a configuré le montage de volume juste avant.

- `maven:3.9.12-eclipse-temurin-17`

  Nom de l'image Docker repérée prédécemment.

- `mvn clean package`

  Commande exécutée dans le conteneur Docker.

  En l'occurrence la commande `mvn` qui exécute successivement les règles
  `clean` puis `package`.

Dans la mesure où c'est la première fois qu'on utilise l'image,
on voit les traces Docker suivantes s'afficher :
```
Unable to find image 'maven:3.9.12-eclipse-temurin-17' locally
3.9.12-eclipse-temurin-17: Pulling from library/maven
d10f3ac7b458: Pull complete
02a2ab1a3a0b: Pull complete
0315dd7c027c: Pull complete
6c73c7e6cdbd: Pull complete
9ae2e4a8370e: Pull complete
78395afbc5eb: Pull complete
bea46ab8f938: Pull complete
1bbcf5688c19: Pull complete
fd88562ce968: Pull complete
c8831fc103ff: Download complete
c74a8312dafa: Download complete
Digest: sha256:a0603aab698040d9c94259f379ec0487da1678560748d6c7508483034033c53d
Status: Downloaded newer image for maven:3.9.12-eclipse-temurin-17
```

Docker télécharge automatiquement l'image spécifiée depuis Docker Hub,
et l'installe dans le cache local de la machine de développement.

Les traces suivantes correspondent à la compilation Maven :
```
[INFO] Scanning for projects...
[INFO]
[INFO] ----------------------< com.mycompany.app:my-app >----------------------
[INFO] Building my-app 1.0-SNAPSHOT
[INFO]   from pom.xml
[INFO] --------------------------------[ jar ]---------------------------------
Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-enforcer-plugin/3.6.2/maven-enforcer-plugin-3.6.2.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-enforcer-plugin/3.6.2/maven-enforcer-plugin-3.6.2.pom (8.2 kB at 17 kB/s)

(...)
```

> 📌 **Cache des images Docker**
>
> A ce stade, la compilation se termine en erreur,
> mais relançons dans un premier temps la même commande de compilation :
> - le téléchargement de l'image ne se répète pas,
> - on obtient directement les traces de la compilation.
>
> En effet :
> ```bash
> docker images
> ```
> On peut voir que l'image `maven:3.9.12-eclipse-temurin-17` fait maintenant partie de la liste des images locales.

Observons l'erreur :
> Detected JDK /opt/java/openjdk is version 17.0.18 which is not in the allowed range [21,).

Effectivement, si on regarde le fichier `pom.xml`,
on voit que la valeur `requireJavaVersion` est configurée à `[21,)`,
ce qui indique que le projet requiert une version de JDK supérieure ou égale à 21.


## 3.3. Compiler avec Java 21

Repérer à nouveau dans Docker Hub une image Maven "temurin-21".
A date, on retient l'image `3.9.12-eclipse-temurin-21`.

Relancer la commande de compilation avec cette nouvelle image :
```bash
docker run --rm -v "$PWD":/usr/src/mymaven -w /usr/src/mymaven maven:3.9.12-eclipse-temurin-21 mvn clean package
```

La compilation passe avec succès cette fois-ci :
```
[INFO] -------------------------------------------------------
[INFO]  T E S T S
[INFO] -------------------------------------------------------
[INFO] Running com.mycompany.app.AppTest
[INFO] Tests run: 2, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.032 s -- in com.mycompany.app.AppTest
[INFO]
[INFO] Results:
[INFO]
[INFO] Tests run: 2, Failures: 0, Errors: 0, Skipped: 0

(...)

[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  18.195 s
[INFO] Finished at: 2026-03-05T23:44:13Z
[INFO] ------------------------------------------------------------------------
```

Si on regarde dans notre dépôt, on a bien un répertoire `target/` qui a été créé.

On exécute le programme obtenu :
```bash
java -jar target/my-app-1.0-SNAPSHOT.jar
```
On obtient bien :
```
Hello World!
```


## 3.4. Conclusion

Quel que soit l'état de notre machine de développement constaté
au [§3.1](#31-v%C3%A9rifier-lexistence-dun-jdk-ou-non-sur-la-machine-de-d%C3%A9veloppement),
on a bien réussi à lancer des compilations de notre projet Java avec différentes versions de JDK :
JDK 17 puis JDK 21.

TODO:
Pour aller plus loin,
on pourra se poser la question de persister le cache Maven,
pour éviter que celui-ci ne retélécharge tout à chaque exécution
(cf. https://hub.docker.com/_/maven#reusing-the-maven-local-repository).


# 4. Annexes

## 4.1. Documentation utile

- Images Docker, par Apache Maven, sur Docker Hub : https://hub.docker.com/_/maven
