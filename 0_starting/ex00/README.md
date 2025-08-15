# Exercice 00 - Hello World

## Description
Introduction aux structures de données de base en Python : listes, tuples, sets et dictionnaires.

## Objectif
Comprendre les différences entre les types de données mutables et immutables en Python.

## Fichiers
- `Hello.py` : Script principal démontrant l'utilisation des structures de données

## Concepts abordés
- **Liste** (`list`) : Structure mutable et ordonnée
- **Tuple** (`tuple`) : Structure immutable et ordonnée  
- **Set** (`set`) : Structure mutable et non ordonnée (pas de doublons)
- **Dictionnaire** (`dict`) : Structure mutable de paires clé-valeur

## Utilisation
```bash
python Hello.py
```

## Sortie attendue
```
['Hello', 'World!']
('Hello', 'France!')
{'Hello', 'Paris!'}
{'Hello': '42Paris!'}
```

## Points clés
- Les listes peuvent être modifiées directement (`ft_list[1] = "World!"`)
- Les tuples nécessitent une réassignation complète pour être "modifiés"
- Les sets ne garantissent pas l'ordre d'affichage
- Les dictionnaires associent des clés à des valeurs
