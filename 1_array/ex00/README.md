# Exercice 00 - Calcul d'IMC

## Description
Cet exercice implémente deux fonctions pour calculer et analyser l'Indice de Masse Corporelle (IMC).

## Fonctions

### `give_bmi(height, weight)`
Calcule l'IMC pour chaque paire (taille, poids).

**Paramètres :**
- `height` : liste de tailles en mètres (int ou float)
- `weight` : liste de poids en kg (int ou float)

**Retour :**
- Liste des IMC calculés

**Formule :** IMC = poids / (taille²)

### `apply_limit(bmi, limit)`
Compare chaque IMC à une limite donnée.

**Paramètres :**
- `bmi` : liste des IMC
- `limit` : seuil de comparaison (int ou float)

**Retour :**
- Liste de booléens (True si IMC > limite, False sinon)

## Validation des données
- Vérification des types (listes, int/float)
- Validation des valeurs positives
- Contrôle de la cohérence des longueurs de listes

## Exemple d'utilisation
```python
from give_bmi import give_bmi, apply_limit

heights = [1.75, 1.80, 1.65]
weights = [70, 85, 60]

bmi_values = give_bmi(heights, weights)
print(bmi_values)  # [22.86, 26.23, 22.04]

overweight = apply_limit(bmi_values, 25)
print(overweight)  # [False, True, False]
```

## Gestion d'erreurs
- `TypeError` : types incorrects
- `ValueError` : valeurs négatives ou listes de tailles différentes
