# Exercice 03 - NULL not found

## Description
Fonction de détection et classification des valeurs "nulles" ou "vides" en Python.

## Objectif
Identifier et différencier les différents types de valeurs considérées comme "fausses" en Python.

## Fichiers
- `NULL_not_found.py` : Fonction de détection des valeurs nulles
- `tester.py` : Script de test de la fonction

## Concepts abordés
- **Valeurs falsy** : `None`, `0`, `''`, `False`, `nan`
- **Opérateurs de comparaison** : `is`, `==`, `isinstance()`
- **Détection de NaN** : `object != object` pour détecter `float('nan')`
- **Types spécifiques** : Distinction entre `0` (int) et `False` (bool)

## Fonction principale
```python
def NULL_not_found(object=any) -> int:
```

## Utilisation
```bash
python tester.py
```

## Détections
- **None** : "Nothing: None <class 'NoneType'>"
- **0 (entier)** : "Zero: 0 <class 'int'>"
- **Chaîne vide** : "Empty: <class 'str'>"
- **False** : "Fake: False <class 'bool'>"
- **NaN** : "Cheese: nan <class 'float'>"
- **Autres** : "Type not found"

## Valeurs de retour
- `0` : Valeur nulle détectée
- `1` : Type non trouvé

## Points techniques
- Utilise `is` pour `None` et `False` (identité d'objet)
- Utilise `isinstance()` pour vérifier le type exact
- Détecte NaN avec la propriété `nan != nan`
