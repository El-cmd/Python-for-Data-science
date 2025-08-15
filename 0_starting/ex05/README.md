# Exercice 05 - Building

## Description
Analyseur de texte qui compte différents types de caractères dans une chaîne.

## Objectif
Apprendre l'analyse de chaînes de caractères et l'utilisation des méthodes de classification des caractères.

## Fichiers
- `building.py` : Script d'analyse de texte

## Concepts abordés
- **Input utilisateur** : `input()` pour saisie interactive
- **Classification de caractères** : `isupper()`, `islower()`, `isdigit()`, `isspace()`
- **Module string** : `string.punctuation` pour identifier la ponctuation
- **Gestion d'arguments** : Arguments optionnels en ligne de commande
- **Compteurs** : Variables pour compter différents types de caractères

## Utilisation
```bash
# Avec argument
python building.py "Hello World!"

# Sans argument (saisie interactive)
python building.py
What is the text to count?
Hello World!
```

## Exemple de sortie
```
The text contains 12 characters:
1 upper letters
9 lower letters
1 punctuation marks
1 spaces
0 digits
```

## Types de caractères analysés
- **Lettres majuscules** : A-Z
- **Lettres minuscules** : a-z
- **Signes de ponctuation** : !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
- **Espaces** : espaces, tabulations, retours à la ligne
- **Chiffres** : 0-9

## Gestion d'erreurs
- **Trop d'arguments** : "AssertionError: Too many arguments"
