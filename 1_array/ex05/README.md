# Exercice 05 - Filtres d'images

## Description
Cet exercice implémente plusieurs fonctions pour appliquer des filtres colorés à une image.

## Fonctions de filtrage

### `ft_invert(array)`
**Inverse les couleurs** de l'image (effet négatif).
- **Algorithme :** `nouvelle_valeur = 255 - ancienne_valeur`
- **Canaux modifiés :** Rouge, Vert, Bleu
- **Effet :** Transforme les couleurs claires en sombres et vice-versa

### `ft_red(array)`
**Filtre rouge** - ne conserve que le canal rouge.
- **Algorithme :** Met les canaux vert et bleu à 0
- **Canaux modifiés :** `array[:, :, 1] = 0` et `array[:, :, 2] = 0`
- **Effet :** Image avec dominante rouge

### `ft_green(array)`
**Filtre vert** - ne conserve que le canal vert.
- **Algorithme :** Met les canaux rouge et bleu à 0
- **Canaux modifiés :** `array[:, :, 0] = 0` et `array[:, :, 2] = 0`
- **Effet :** Image avec dominante verte

### `ft_blue(array)`
**Filtre bleu** - ne conserve que le canal bleu.
- **Algorithme :** Met les canaux rouge et vert à 0
- **Canaux modifiés :** `array[:, :, 0] = 0` et `array[:, :, 1] = 0`
- **Effet :** Image avec dominante bleue

### `ft_grey(array)`
**Conversion en niveaux de gris**.
- **Algorithme :** Calcule la moyenne des 3 canaux RGB
- **Formule :** `gris = (R + G + B) / 3`
- **Application :** Copie la valeur grise sur les 3 canaux
- **Effet :** Image en noir et blanc

## Caractéristiques communes

### Paramètres
- `array` : tableau NumPy représentant l'image (hauteur, largeur, 3)

### Retour
- Tableau NumPy modifié avec le filtre appliqué

### Affichage
- Chaque fonction affiche automatiquement l'image filtrée
- Utilise `plt.imshow()` avec `plt.axis("off")`
- `plt.show()` pour ouvrir la fenêtre d'affichage

### Préservation des données
- Toutes les fonctions utilisent `array.copy()` pour préserver l'original
- Modifications effectuées sur la copie uniquement

## Dépendances
- `numpy` : manipulation des tableaux
- `matplotlib.pyplot` : affichage des images

## Exemple d'utilisation
```python
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey

# Charger une image
image = ft_load("animal.jpeg")

# Appliquer différents filtres
inverted = ft_invert(image)    # Image inversée
red_filter = ft_red(image)     # Filtre rouge
green_filter = ft_green(image) # Filtre vert
blue_filter = ft_blue(image)   # Filtre bleu
grey_image = ft_grey(image)    # Niveaux de gris
```

## Structure des canaux
- **Canal 0** : Rouge (Red)
- **Canal 1** : Vert (Green)  
- **Canal 2** : Bleu (Blue)
- **Valeurs** : 0-255 (uint8)

## Algorithmes de filtrage

### Inversion
```python
inverted[:, :, 0] = 255 - array[:, :, 0]  # Rouge
inverted[:, :, 1] = 255 - array[:, :, 1]  # Vert
inverted[:, :, 2] = 255 - array[:, :, 2]  # Bleu
```

### Filtres monochromatiques
```python
# Rouge uniquement
red[:, :, 1] = 0  # Supprime vert
red[:, :, 2] = 0  # Supprime bleu
```

### Conversion en gris
```python
grey_value = np.mean(array[:, :, :3], axis=2)
grey[:, :, 0] = grey_value  # Rouge = gris
grey[:, :, 1] = grey_value  # Vert = gris
grey[:, :, 2] = grey_value  # Bleu = gris
```

## Utilisation
Chaque fonction peut être appelée individuellement et affiche automatiquement le résultat dans une fenêtre matplotlib.
