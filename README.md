<link rel="stylesheet" href="css/styles.css"></link>

<h1>Cours sur les environnements de développement logiciel</h1>


<!-- TOC -->

- [1. Objet du dépôt](#1-objet-du-d%C3%A9p%C3%B4t)
- [2. Markdown](#2-markdown)
    - [2.1. Boîtes de texte](#21-bo%C3%AEtes-de-texte)
    - [2.2. Référence de TP](#22-r%C3%A9f%C3%A9rence-de-tp)
    - [2.3. Autres icônes utiles](#23-autres-ic%C3%B4nes-utiles)
- [3. Tables des matières et numérotation des titres](#3-tables-des-mati%C3%A8res-et-num%C3%A9rotation-des-titres)
- [4. Générer les documents PDF](#4-g%C3%A9n%C3%A9rer-les-documents-pdf)
- [5. Ressources](#5-ressources)

<!-- /TOC -->


# 1. Objet du dépôt

Ce dépôt contient un cours sur le thème des environnements de développement logiciel.

Accès au cours :
- [Version Markdown](Environnements%20de%20d%C3%A9veloppement%20logiciel.md)
- Version PDF (TODO)


# 2. Markdown

Dans la mesure du possible,
on limite l'utilisation du HTML et des feuilles de style,
pour assurer un meilleur affichage possible dans les différents cas de figure :
- visualisation dans VS Code,
- rendu en ligne par github,
- export PDF.

Cela permet également de rester en syntaxe Markdown autant que possible,
plutôt que de basculer en HTML.


## 2.1. Boîtes de texte

Affichage d'une note informative :
```md
> 🛈 **Info**
>
> Blah blah blah.
```
> 🛈 **Info**
>
> Blah blah blah.

Affichage d'une astuce :
```md
> 💡 **Tip**
>
> Blah blah blah.
```
> 💡 **Tip**
>
> Blah blah blah.

Affichage d'un avertissement :
```md
> ⚠️ **Caution**
>
> Blah blah blah.
```
> ⚠️ **Caution**
>
> Blah blah blah.

Affichage d'une notion importante :
```md
> 📌 **Important**
>
> Blah blah blah.
```
> 📌 **Important**
>
> Blah blah blah.


## 2.2. Référence de TP

```md
> 👷 TP : [Sujet du TP](README.md#22-r%C3%A9f%C3%A9rence-de-tp)
```
> 👷 TP : [Sujet du TP](README.md#22-r%C3%A9f%C3%A9rence-de-tp)


## 2.3. Autres icônes utiles

| Icône | Signification |
|-------|---------------|
| ✅    | OK            |
| ❌    | NOK           |


# 3. Tables des matières et numérotation des titres

A partir de VS Code :
- Installer l'extension [Auto Markdown TOC](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf) par Hunter Tran.
- Dès lors, les mises à jour du document se font automatiquement lors des enregistrements.

Note : Le fichier `.vscode/settings.json` enregistre les configurations utiles pour cette extension.


# 4. Générer les documents PDF

A partir de VS Code :
- Installer l'extension [Markdown PDF](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf) par yzane.
- Ouvrir le fichier `Environnements de développement et déploiement.md`.
- Clic droit dans le fichier > "Mardown PDF: Export (pdf)"
- Le fichier `Environnements de développement et déploiement.pdf` est généré.

Note : Le fichier `.vscode/settings.json` enregistre les configurations utiles pour cette extension.

> **Mémo : Configurations header et footer**
>
> Header :
> - Configuration d'origine : `<div style="font-size: 9px; margin-left: 1cm;"> <span class='title'></span></div> <div style="font-size: 9px; margin-left: auto; margin-right: 1cm; ">%%ISO-DATE%%</div>`
>
> Footer :
> - Configuration d'origine : `<div style="font-size: 9px; margin: 0 auto;"> <span class='pageNumber'></span> / <span class='totalPages'></span></div>`
> - Problème d'affichage des numéros de page :
>     - https://github.com/yzane/vscode-markdown-pdf/issues/262#issuecomment-1646801829
>       => Configuration `markdown-pdf.margin.bottom` supérieure à "1.03cm"
>
> Limitations constatées :
> - Les feuilles de styles CSS ne s'appliquent pas aux header et footer.
> - La propriété `background-color` ne s'applique pas.
> - La propriété `color` s'applique, mais la couleur rendue semble distordue.


# 5. Ressources

Ressources intéressantes pour la syntaxe Markdown :
- https://www.markdownlang.com/fr/basic/blockquotes.html
- https://www.utf8icons.com/

Ressources intéressantes pour la génération de documents PDF à partir de Markdown :
- https://itsfoss.gitlab.io/post/how-to-convert-markdown-md-files-to-pdf-on-linux/
- https://linuxconfig.org/how-to-convert-markdown-to-pdf-on-linux
- https://www.tecmint.com/convert-md-to-pdf-on-linux/

Images :
- https://www.pexels.com/fr-fr/
- https://fr.freepik.com/
- https://pixabay.com/fr/
