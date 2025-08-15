# Exercice 08 - Loading

## Description
Implémentation d'une barre de progression personnalisée similaire à la bibliothèque `tqdm`.

## Objectif
Créer un générateur avec affichage de progression en temps réel pour visualiser l'avancement d'une itération.

## Fichiers
- `Loading.py` : Fonction ft_tqdm avec barre de progression
- `tester.py` : Script de test de la fonction
- `__pycache__/` : Cache Python généré automatiquement

## Concepts abordés
- **Générateurs** : `yield` pour créer un itérateur avec état
- **Affichage dynamique** : `sys.stdout.write()` et `sys.stdout.flush()`
- **Contrôle du curseur** : `\r` pour réécrire sur la même ligne
- **Calculs de pourcentage** : Progression en temps réel
- **Formatage de chaînes** : Création d'une barre visuelle

## Fonction ft_tqdm
```python
def ft_tqdm(lst: range) -> None:
```

## Utilisation
```python
from Loading import ft_tqdm
import time

for item in ft_tqdm(range(100)):
    time.sleep(0.01)  # Simulation de travail
```

## Affichage de la barre
```
 75%|██████████████████████████████████████████████████-----------| 75/100
```

## Composants de l'affichage
- **Pourcentage** : Progression en % (format 3 caractères)
- **Barre visuelle** : 66 caractères avec █ (fait) et - (restant)
- **Compteur** : Position actuelle / total

## Fonctionnement technique
- **Calcul progression** : `(i + 1) / total * 100`
- **Longueur barre** : 66 caractères fixes
- **Caractères remplis** : `int(bar_length * (i + 1) / total)`
- **Mise à jour** : `\r` pour revenir au début de ligne
