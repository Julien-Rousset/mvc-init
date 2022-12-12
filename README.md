# MVC-INIT Folder
Pour utiliser le script **sh** il suffit d'utiliser la commande suivante:
- **sh mvc-init/mvc-init.sh**

Le script a été codé pour permettre une initialisation d'un environnement de travail MVC PHP. Le script gère aussi la création d'un htaccess avec le code déjà appliquer. Il gère aussi la création et l'initialisation du composer dans votre projet. (Cela comprend la création du **composer.json** et du **dump-autoload**). Attention la ligne de commande doit être appliquée dans le dossier de votre projet et pas en dehors. Un exemple vous sera donné ci-dessous :

## Exemple d'utilisation
- mkdir ProjectFolderName && cd ProjectFolderName
- git clone repo
- sh mvc-init/mvc-init.sh
- rm -R mvc-init

Pour initiliaser l'autoload de Composer, il vous sera demandé de donner un nom à votre namespace, vous devrez donc entrer quelque chose comme *App*(sans les backslash, le script s'en occupe !!!)