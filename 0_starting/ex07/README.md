# Exercice 07 - SOS

## Description
Convertisseur de texte en code Morse utilisant un dictionnaire de correspondance.

## Objectif
Apprendre l'utilisation des dictionnaires pour la traduction de caractères et la manipulation de chaînes.

## Fichiers
- `sos.py` : Script de conversion en code Morse

## Concepts abordés
- **Dictionnaires de correspondance** : Mapping caractères → code Morse
- **Validation d'entrée** : `isalnum()` pour vérifier caractères alphanumériques
- **Conversion de casse** : `upper()` pour uniformiser les caractères
- **Boucles sur chaînes** : Parcours caractère par caractère
- **Affichage formaté** : `end=""` pour contrôler les retours à la ligne

## Code Morse supporté
- **Lettres** : A-Z (.- à --..)
- **Chiffres** : 0-9 (.---- à ----.)
- **Espace** : Représenté par "/"

## Utilisation
```bash
python sos.py "HELLO WORLD"
python sos.py "SOS"
python sos.py "42"
```

## Exemples de sortie
```bash
python sos.py "SOS"
# ... --- ... 

python sos.py "HELLO"
# .... . .-.. .-.. --- 
```

## Validation
- **Un seul argument** requis
- **Caractères alphanumériques uniquement** (lettres, chiffres, espaces)
- **Gestion d'erreurs** : "AssertionError: the arguments are bad"

## Dictionnaire NESTED_MORSE
Contient 36 entrées : 26 lettres + 10 chiffres + espace, chaque code Morse se termine par un espace.
