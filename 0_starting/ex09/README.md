# Exercice 09 - Package

## Description
Création et distribution d'un package Python avec setuptools, incluant la structure complète d'un projet distributable.

## Objectif
Apprendre à créer, configurer et distribuer un package Python avec les outils standards.

## Structure du projet
```
ex09/
├── ft_package/          # Package principal
├── setup.py            # Configuration de distribution
├── pyproject.toml      # Configuration moderne Python
├── LICENSE             # Licence MIT
├── README.md           # Documentation
├── test.py             # Script de test
├── dist/               # Fichiers de distribution générés
└── ft_package.egg-info/ # Métadonnées du package
```

## Fichiers principaux
- **setup.py** : Configuration setuptools classique
- **pyproject.toml** : Configuration moderne (PEP 518)
- **LICENSE** : Licence MIT pour la distribution
- **ft_package/** : Code source du package

## Concepts abordés
- **Setuptools** : Outil de packaging Python standard
- **Distribution** : Création de packages installables
- **Métadonnées** : Informations sur l'auteur, version, licence
- **Structure de projet** : Organisation standard d'un package Python

## Configuration setup.py
```python
setup(
    name="ft_package",
    version="0.0.1",
    packages=find_packages(),
    license="MIT",
    url="https://github.com/El-cmd/Python-for-Data-science",
    author="vloth",
    author_email="vloth@student.42.fr",
    description="A simple package for testing"
)
```

## Utilisation
```bash
# Installation en mode développement
pip install -e .

# Création des fichiers de distribution
python setup.py sdist bdist_wheel

# Test du package
python test.py
```

## Commandes de build
- **sdist** : Crée une archive source (.tar.gz)
- **bdist_wheel** : Crée un wheel (.whl) pour installation rapide
- **egg_info** : Génère les métadonnées du package

Un exemple de package Python simple pour la piscine Data Science.
