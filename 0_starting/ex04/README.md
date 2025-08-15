# Exercice 04 - What is

## Description
Programme de détermination de la parité d'un nombre entier passé en argument.

## Objectif
Apprendre la gestion des arguments de ligne de commande et la gestion d'erreurs avec `sys.argv`.

## Fichiers
- `whatis.py` : Script principal de détection de parité

## Concepts abordés
- **Arguments système** : `sys.argv` pour récupérer les arguments
- **Gestion d'erreurs** : `try/except` avec `AssertionError` et `ValueError`
- **Conversion de types** : `int()` pour convertir une chaîne en entier
- **Opérateur modulo** : `%` pour déterminer la parité
- **Assertions** : `assert` pour valider les conditions

## Utilisation
```bash
python whatis.py [nombre]
```

## Exemples
```bash
python whatis.py 42    # Sortie: I'm Even
python whatis.py 13    # Sortie: I'm Odd
python whatis.py       # Aucune sortie (pas d'argument)
python whatis.py abc   # AssertionError: argument is not an integer
python whatis.py 1 2   # AssertionError: more than one argument is provided
```

## Gestion d'erreurs
- **Aucun argument** : Le programme se termine silencieusement
- **Trop d'arguments** : "AssertionError: more than one argument is provided"
- **Argument non-entier** : "AssertionError: argument is not an integer"

## Logique
- Nombre pair (`n % 2 == 0`) → "I'm Even"
- Nombre impair (`n % 2 != 0`) → "I'm Odd"
