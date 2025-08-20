# Exercice 03 - Zoom sur image

## Description
Cet exercice implémente un programme pour découper une zone centrale d'une image et la convertir en niveaux de gris.

## Fonctionnalités
Le programme `zoom.py` effectue les opérations suivantes :
1. **Chargement** d'une image JPEG
2. **Découpage** d'une zone centrale de 400x400 pixels
3. **Conversion** en niveaux de gris
4. **Affichage** du résultat avec matplotlib

## Processus détaillé

### Étape 1 : Chargement de l'image
- Utilise `ft_load()` pour charger "animal.jpeg"
- Affiche automatiquement les dimensions originales
- Retourne un tableau NumPy (hauteur, largeur, canaux RGB)

### Étape 2 : Calcul de la zone de crop
- Calcule les coordonnées pour centrer un crop de 400x400
- `start_y = (hauteur - 400) // 2`
- `start_x = (largeur - 400) // 2`

### Étape 3 : Découpage
- Extrait la zone centrale : `image[start_y:start_y+400, start_x:start_x+400]`
- Résultat : tableau (400, 400, 3)

### Étape 4 : Conversion en niveaux de gris
- `np.mean(cropped, axis=2, keepdims=True)` : moyenne des canaux RGB
- `axis=2` : moyenner sur la dimension des canaux
- `keepdims=True` : conserve la dimension (400, 400, 1)
- `.astype(np.uint8)` : conversion en entiers 8-bits

### Étape 5 : Affichage
- Utilise `plt.imshow()` avec `cmap='gray'`
- `gray.squeeze()` : supprime la dimension unitaire pour matplotlib

## Dépendances
- `load_image` : module local pour charger les images
- `matplotlib.pyplot` : affichage graphique
- `numpy` : manipulation des tableaux

## Exemple de sortie
```
The shape of image is: (768, 1024, 3)
[[[123 145 167] [124 146 168] ...]]
New shape after slicing: (400, 400, 1)
[[[145] [146] [147] ...]]
```

## Gestion d'erreurs
- `TypeError`, `ValueError`, `FileNotFoundError` : gestion globale des erreurs
- Affichage d'un message d'erreur explicite

## Utilisation
```bash
python zoom.py
```

L'image découpée et convertie s'affiche dans une fenêtre matplotlib.
