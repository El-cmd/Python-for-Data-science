# Exercice 02 - Find ft_type

## Description
Fonction d'identification et d'affichage des types d'objets Python.

## Objectif
Comprendre l'introspection de types et l'utilisation de la fonction `type()`.

## Fichiers
- `find_ft_type.py` : Fonction d'identification de types
- `tester.py` : Script de test de la fonction

## Concepts abordés
- **Introspection de types** : `type(object)` pour identifier le type
- **Conditions multiples** : Série de `if` pour différents types
- **Types de base** : `list`, `tuple`, `set`, `dict`, `str`
- **Formatage conditionnel** : Affichage différent selon le type

## Fonction principale
```python
def all_thing_is_obj(object: any) -> int:
```

## Utilisation
```bash
python tester.py
```

## Comportement
- **Liste** : Affiche "List: <class 'list'>"
- **Tuple** : Affiche "Tuple: <class 'tuple'>"
- **Set** : Affiche "Set: <class 'set'>"
- **Dict** : Affiche "Dict: <class 'dict'>"
- **String** : Affiche "[contenu] is in the kitchen: <class 'str'>"
- **Autres types** : Affiche "Type not found"

## Valeur de retour
La fonction retourne toujours `42`.
