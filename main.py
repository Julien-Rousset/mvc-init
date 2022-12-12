from pathlib import Path
import json

listePath = []
currentPath = Path().cwd()

for element in ["Views", "Controllers", "Models", "Utils"]:
    listePath.append(currentPath / f"app/{element}")

for path in listePath:
    path.mkdir(exist_ok=True, parents=True)

publicFodler = currentPath / "public"
publicFodler.mkdir(exist_ok=True, parents=True)

indexFile = publicFodler / "index.php"
indexFile.touch()

htaccessFile = publicFodler / ".htaccess"
htaccessFile.touch()

composerFile = currentPath / "composer.json"
composerFile.touch()

with open(indexFile, "w") as f:
    f.write("<?php \nrequire_once __DIR__ . '/../vendor/autoload.php';")

with open(htaccessFile, "w") as f:
    f.write("RewriteEngine On\n")
    f.write("RewriteCond %{REQUEST_URI}::$1 ^(/.+)/(.*)::\\2$\n")
    f.write("RewriteRule ^(.*) - [E=BASE_URI:%1]\n")
    f.write("RewriteCond %{REQUEST_FILENAME} !-d\n")
    f.write("RewriteCond %{REQUEST_FILENAME} !-f\n")
    f.write("RewriteRule ^(.*)$ index.php?_url=/$1 [QSA,L]")

with open(composerFile, "w") as f:
    namespaceName = input("Name of name space (like App): ")
    json.dump({"autoload": {"psr-4": {f"{namespaceName}\\": "app/"}}}, f, indent=4)