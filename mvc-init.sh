#!bin/bash

echo "===== Initialisation de la construction MVC ====="
python3 mvc-init/main.py 
echo ""
echo "===== Initialisation de Composer ====="
composer install
composer dump-autoload
echo ""
echo "===== Initialisation réussie ====="