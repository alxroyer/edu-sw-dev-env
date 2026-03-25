<link rel="stylesheet" href="css/styles.css"></link>

<h1>Développer en Remote SSH avec VS Code sur une machine distante avec Maven JDK</h1>


TODO: Mettre en forme


Créer une image Docker avec Maven + JDK + git + sshd :
- [Dockerfile](./TP%20-%20Remote%20SSH%20Docker%20Maven%20JDK/Dockerfile)
```bash
docker build -t tp-remote-ssh .
```

Créer un conteneur :
```bash
docker create --name tp-remote-ssh-001 -p 2222:22 tp-remote-ssh
docker container list --all
```

Démarre le conteneur :
```bash
docker start tp-remote-ssh-001
docker ps -a --filter "name=tp-remote-ssh-001"
netstat -an | grep 2222
```

Se connecter en SSH et cloner le dépôt d'exemple :
```bash
ssh root@localhost -p 2222
git clone https://github.com/jenkins-docs/simple-java-maven-app.git
cd simple-java-maven-app
pwd
```

VS Code :
- "Extensions" > Install "Remote - SSH" de Microsoft.
- Cliquer sur l'icône "><" en bas à gauche > "Connect to Host..."
    - Saisir l'adresse et l'utilisateur : "root@localhost:2222"
    - Saisir le mot de passe : "pwdpwdpwd"
- "File" > "Open Folder" > sélectionner le répertoire `simple-java-maven-app`
- "Do you want to install the recommended 'Extension Pack for Java' extension from Microsoft for this repository?" > "Install"
- "Terminal" > "New Terminal"
    - `mvn clean package`
    - `$JAVA_HOME/bin/java -jar cd target/my-app-1.0-SNAPSHOT.jar`


Mémo liens Docker :
- https://linuxize.com/post/how-to-build-docker-images-with-dockerfile/
- https://docs.docker.com/reference/cli/docker/container/create
- https://docs.docker.com/reference/cli/docker/container/run
- https://docs.docker.com/reference/cli/docker/container/start
