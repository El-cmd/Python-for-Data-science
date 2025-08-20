# Exercice 02 - Chargement d'images

## Description
Cet exercice implémente une fonction pour charger une image JPEG et la convertir en tableau NumPy.

## Fonction

### `ft_load(path)`
Charge une image depuis un chemin et retourne un tableau NumPy.

**Paramètres :**
- `path` : chemin vers le fichier image (str)

**Retour :**
- `np.ndarray` : tableau NumPy représentant l'image

**Affichage :**
- Dimensions de l'image : `The shape of image is: (hauteur, largeur, canaux)`

## Dépendances
- `PIL` (Python Imaging Library) pour l'ouverture d'images
- `numpy` pour la conversion en tableau
- `os` pour la vérification d'existence du fichier

## Validations
- Vérification que le chemin est une chaîne de caractères
- Contrôle de l'extension (.jpg ou .jpeg uniquement)
- Vérification de l'existence du fichier

## Exemple d'utilisation
```python
from load_image import ft_load

# Charger une image
image_array = ft_load("animal.jpeg")
# Affichage : The shape of image is: (480, 640, 3)

print(type(image_array))  # <class 'numpy.ndarray'>
print(image_array.shape)  # (480, 640, 3)
```

## Gestion d'erreurs
- `TypeError` : chemin non-string
- `ValueError` : extension de fichier incorrecte
- `FileNotFoundError` : fichier inexistant

## Images supportées
- Formats : JPEG (.jpg, .jpeg)
- Images couleur (RGB) et niveaux de gris
