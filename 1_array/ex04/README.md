# Exercice 04 - Rotation d'image

## Description
Cet exercice implémente un programme pour découper une image, la convertir en niveaux de gris et effectuer une transposition (rotation de 90°).

## Fonctionnalités
Le programme `rotate.py` effectue les opérations suivantes :
1. **Chargement** d'une image JPEG
2. **Découpage** d'une zone centrale de 400x400 pixels
3. **Conversion** en niveaux de gris
4. **Transposition** manuelle (rotation 90°)
5. **Affichage** du résultat avec matplotlib

## Processus détaillé

### Étape 1 : Chargement et découpage
- Utilise `ft_load()` pour charger "animal.jpeg"
- Calcule la zone centrale de 400x400 pixels
- `cropped = image[start_y:start_y+400, start_x:start_x+400]`

### Étape 2 : Conversion en niveaux de gris
- `np.mean(cropped, axis=2, keepdims=True)` : moyenne des canaux RGB
- Conversion en `uint8` pour les valeurs 0-255
- Résultat : tableau (400, 400, 1)

### Étape 3 : Préparation pour la transposition
- `gray.squeeze()` : supprime la dimension unitaire → (400, 400)
- Récupère les dimensions : `h, w = gray_2d.shape[0], gray_2d.shape[1]`

### Étape 4 : Transposition manuelle
- Crée un nouveau tableau : `np.zeros((w, h))`
- Boucle double pour échanger lignes et colonnes :
  ```python
  for i in range(h):
      for j in range(w):
          transposed[j][i] = gray_2d[i][j]
  ```
- Transformation : (400, 400) → (400, 400) avec rotation 90°

### Étape 5 : Affichage des résultats
- Affiche la forme originale et transposée
- Affiche le contenu du tableau transposé
- Visualise avec `plt.imshow()` et `cmap="gray"`

## Dépendances
- `load_image` : module local pour charger les images
- `matplotlib.pyplot` : affichage graphique
- `numpy` : manipulation des tableaux

## Exemple de sortie
```
The shape of image is: (768, 1024, 3)
The shape of image is: (400, 400, 1) or (400,400)
[[[145] [146] ...]]
New shape after Transpose: (400,400)
[[145 146 147 ...]
 [148 149 150 ...]
 ...]
```

## Algorithme de transposition
La transposition échange les coordonnées (i,j) → (j,i) :
- Pixel à la position [ligne][colonne] → [colonne][ligne]
- Effet visuel : rotation de 90° dans le sens horaire

## Gestion d'erreurs
- `TypeError`, `ValueError`, `FileNotFoundError` : gestion globale
- Affichage d'un message d'erreur explicite

## Utilisation
```bash
python rotate.py
```

L'image transposée s'affiche dans une fenêtre matplotlib.
