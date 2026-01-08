Ce dépôt contient un cours sur le thème des environnement de développement logiciel.

Accès au cours : voir le fichier [Environnements de développement logiciel.md](Environnements%20de%20d%C3%A9veloppement%20logiciel.md)


# Table des matières et numérotation des titres

A partir de VS Code :
- Installer l'extension [Auto Markdown TOC](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf) par Hunter Tran.
- Dès lors, les mises à jour du document se font automatiquement lors des enregistrements.

Note : Le fichier `.vscode/settings.json` enregistre les configurations utiles pour cette extension.


# Générer le document PDF

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


# Ressources

Ressources intéressantes pour la génération de documents PDF à partir de Markdown :
- https://itsfoss.gitlab.io/post/how-to-convert-markdown-md-files-to-pdf-on-linux/
- https://linuxconfig.org/how-to-convert-markdown-to-pdf-on-linux
- https://www.tecmint.com/convert-md-to-pdf-on-linux/

Images :
- https://www.pexels.com/fr-fr/
- https://fr.freepik.com/
- https://pixabay.com/fr/
