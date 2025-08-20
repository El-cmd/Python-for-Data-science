# Exercice 01 - Manipulation de tableaux 2D

## Description
Cet exercice implémente une fonction pour découper un tableau 2D entre deux indices et afficher les dimensions avant et après le découpage.

## Fonction

### `slice_me(family, start, end)`
Découpe un tableau 2D entre deux indices et affiche les formes avant/après.

**Paramètres :**
- `family` : tableau 2D (liste de listes) contenant des int ou float
- `start` : indice de début (inclusif)
- `end` : indice de fin (exclusif)

**Retour :**
- Tableau 2D découpé

**Affichage :**
- Forme originale : `My shape is : (lignes, colonnes)`
- Nouvelle forme : `My new shape is : (nouvelles_lignes, colonnes)`

## Validations
- Vérification que `family` est une liste de listes
- Contrôle que toutes les lignes ont la même longueur
- Validation que tous les éléments sont des int ou float
- Vérification que `start` et `end` sont des entiers
- Contrôle que le tableau n'est pas vide

## Exemple d'utilisation
```python
from array2D import slice_me

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

result = slice_me(family, 0, 2)
# Affichage :
# My shape is : (4, 2)
# My new shape is : (2, 2)
# Résultat : [[1.80, 78.4], [2.15, 102.7]]
```

## Gestion d'erreurs
- `TypeError` : types incorrects (non-liste, éléments non numériques)
- `ValueError` : tableau vide ou lignes de tailles différentes
