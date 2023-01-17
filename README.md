# MVC-INIT Folder
Pour utiliser le script **python** il suffit d'utiliser la commande suivante:
- **python3 main.py**

Le script a été codé pour permettre une initialisation d'un environnement de travail MVC PHP. Le script gère aussi la création d'un htaccess avec le code déjà appliquer. Il gère aussi la création et l'initialisation du composer dans votre projet. (Cela comprend la création du **composer.json** et du **dump-autoload**, le require de AltoRouter et son instanciation). Attention la ligne de commande doit être appliquée dans le dossier de votre projet et pas en dehors. Un exemple vous sera donné ci-dessous:

## Exemple :
- mkdir Project && cd Project
- python3 main.py
- rm main.py

Pour initiliaser l'autoload de Composer, il vous sera demandé de donner un nom à votre namespace (sauf si vous voulez garder celui par Defaut qui est App), vous devrez donc entrer quelque chose comme *Namespace* (sans les backslash, le script s'en occupe !!!)