
# dirName

Dossiers mal rangés, mal orthorgaphiés ou juste la flemme de créer des dossiers ? Faites comme les profs et copiez leur dossiers !

dirName est un petit programme python qui permet de copier les répertoires d'une page moodle sur sa machine. (Le programme n'installe pas le contenu des répertoires sur moodle. Il recopie simplement leur nom).


## Auteur

- [@n0upi](https://www.linkedin.com/in/louis-bruche-37278b221/)


## Installation

Installer **Python3**.
https://www.python.org/ftp/python/3.12.2/Python-3.12.2.tar.xz

Installer **beautifulsoup4** (bibliothèque python permettant de faire des requêtes web).
```bash
  pip install beautifulsoup4
```

Copier le projet sur votre machine
```bash
  git clone https://github.com/noupiiii/dirName.git
```

## Utilisation

```bash
  python3 main.py
```
Saisir le lien moodle contenant les dossiers voulu (ex : https://moodle.iut-littoral.fr/moodle/course/index.php?categoryid=7)

Puis saisir le répertoire de destination (ex : '/iut/a1-s1')
