# Exercice 06 - Filter String

## Description
Implémentation d'une fonction de filtrage personnalisée et son utilisation pour filtrer des mots selon leur longueur.

## Objectif
Comprendre les fonctions de filtrage, les expressions lambda et les générateurs.

## Fichiers
- `ft_filter.py` : Implémentation personnalisée de la fonction filter
- `filterstring.py` : Script principal utilisant ft_filter
- `__pycache__/` : Cache Python généré automatiquement

## Concepts abordés
- **Générateurs** : `yield` pour créer un générateur économe en mémoire
- **Expressions lambda** : Fonctions anonymes pour le filtrage
- **Validation d'arguments** : Vérification de type et de format
- **Module string** : `string.punctuation` pour détecter la ponctuation
- **Méthodes de chaînes** : `split()`, `isdigit()`

## Fonction ft_filter
```python
def ft_filter(function, iterable):
    for x in iterable:
        if function(x):
            yield x
```

## Utilisation
```bash
python filterstring.py "Hello world this is a test" 4
```

## Exemple de sortie
```
['Hello', 'world']
```

## Validation des arguments
- **Nombre d'arguments** : Exactement 2 arguments requis
- **Deuxième argument** : Doit être un nombre entier
- **Premier argument** : Ne doit pas contenir de ponctuation

## Logique de filtrage
Le programme filtre les mots dont la longueur est **strictement supérieure** au nombre donné.

## Gestion d'erreurs
Toutes les erreurs de validation affichent : "AssertionError: the arguments are bad"
