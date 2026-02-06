<link rel="stylesheet" href="css/styles.css"></link>

<h1>Commandes git de base</h1>



# Configurer git

`git config user.name`

`git config user.email`


# Commandes de base

## Tirer un dépôt existant

`git clone`

## Initialiser un nouveau dépôt

`git init`

## Se positionner dans l'arbre de versions

`git checkout`

On peut choisir une branche, un tag, voire un hash de commit.

## Etat du dépôt / modifications locales

`git status`

## Voir l'historique du dépôt

`gitk --all &`

Lance une fenêtre graphique, pas très jolie, mais qui rend le service.

`git log`

Permet de visualiser une information d'historique dans la console,
mais on ne voit pas les branches qui partent de droite et de gauche.

`git log -n 1`

Permet de visualiser rapidement les détails du commit sur lequel on pointe actuellement.

## Créer un commit

`git commit`
Mais pas facile à utiliser en ligne de commandes.

Plus facile d'utiliser l'interface graphique, pas très jolie, mais fournie de base avec Git Bash.
`git gui &`

## Branches

`git branch` ou `git branch -vv`

Permet de lister les branches locales dans le dépôts (avec plus ou moins de détails).

`git branch -a` ou `git branch -avv`

Permet de lister les branches locales et distantes (avec plus ou moins de détails encore une fois).

Pour tirer une novelle branche, personnellement je préfère utiliser la séquence suivante :

`git checkout ...` => d'abord je sélectionne la d'où je veux repartir.

`git checkout -b ...` => permet de tirer la nouvelle branche et de l'utiliser directement.

## Tags

`git tag`
Permet de visualiser les tags.

`git tag V1.0.3`
Pose le tag "V1.0.3".

## Comparer des versions du repos

`git diff`

`git diff --stat`

## Pousser / récupérer des commits entre repos

`git fetch`
Récupère une mise à jour de l'historique depuis le dépôt distant.

`git push`
Pousse les commits locaux vers le dépôt distant.

Upstream branch
`git push --set-upstream origin <local-branch>`
Tip : Je laisse git me rappeler la commande, que je peux simplement copier / coller.

`git push --tags`
Par défaut, git ne pousse pas les tags

Dangers du `git push --force`


# Commit ligne à ligne avec `git gui`

Intérêt :
- Relecture personnelle
- Rédaction du commit log au fur et à mesure

Autres frontends intéressants
- Git Extension
    - Raccourcis clavier
    - Permet d'éviter l'erreur du click malencontreux sur "Stage Hunk" en lieu et place de "Stage Lines"


# Merges & rebases

## Merge

`git merge`

Principe du merge :
- Merges automatiques
- Merges conflictuels


## Rebase

`git rebase`

Principe du rebase :
- Déplacement des noeuds
- Réécriture d'historique


Rebases conflictuels :
- `git status`
- `git rebase --continue`


## Cherry-pick

`git cherry-pick`


# Utilisation de frontends

- Turtoise Git
- Git Extension
