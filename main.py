from pathlib import Path
import sys
import subprocess
import json

class MvcInit:
    folders_keys = ["app/", "public/"]
    currentDir = Path().cwd()

    def __init__(self, *args):
        self.paths = list(args)
        
        for keys in __class__.folders_keys:
            folderPath = __class__.currentDir / keys
            folderPath.mkdir()

    def constructAppFolder(self):
        app_folder = __class__.currentDir / __class__.folders_keys[0]

        for path in self.paths:
            children_folder = app_folder / path
            children_folder.mkdir()
        
    def constructPublicFolder(self):
        public_folder = __class__.currentDir / __class__.folders_keys[1]
        
        index_file = public_folder / "index.php"
        index_file.touch()

        with open(index_file, "w") as f:
            f.write("<?php\n\n")
            f.write("require_once __DIR__ . '/../vendor/autoload.php';\n\n")
            f.write("$router = new AltoRouter();\n\n")
        
        htaccess_file = public_folder / ".htaccess"
        htaccess_file.touch()

        with open(htaccess_file, "w") as f:
            f.write("RewriteEngine On\n")
            f.write("RewriteCond %{REQUEST_URI}::$1 ^(/.+)/(.*)::\\2$\n")
            f.write("RewriteRule ^(.*) - [E=BASE_URI:%1]\n")
            f.write("RewriteCond %{REQUEST_FILENAME} !-d\n")
            f.write("RewriteCond %{REQUEST_FILENAME} !-f\n")
            f.write("RewriteRule ^(.*)$ index.php?_url=/$1 [QSA,L]")
    
    def initComposer(self):
        composer_file = __class__.currentDir / "composer.json"
        composer_file.touch()

        namespace_key = input("Do you want rename Namespace's Default ? ")

        if namespace_key == False:
            namespace_key = "App"

        with open(composer_file, "w") as f:
            json.dump({"autoload": {"psr-4": {f"{namespace_key}\\": "app/"}}}, f, indent=4)

        bash_script = __class__.currentDir / "mvc-init.sh"
        bash_script.touch()

        with open(bash_script, "w") as f:
            f.write("composer install\n")
            f.write("composer dump-autoload\n")
            f.write("composer require altorouter/altorouter")
        
        subprocess.run(["sh", "mvc-init.sh"])
        subprocess.run(["rm", "mvc-init.sh"])

class App:
    PATHS = [
        "Views",
        "Utils",
        "Models",
        "Controllers"
    ]
    def __init__(self):
        self.init = MvcInit(*__class__.PATHS)
    
    def run(self):
        self.init.constructAppFolder()
        self.init.initComposer()
        self.init.constructPublicFolder()
    
app = App();

app.run();