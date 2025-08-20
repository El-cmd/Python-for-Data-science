# Module 1_array - Manipulation de tableaux et traitement d'images

## Vue d'ensemble
Ce module explore la manipulation de tableaux NumPy et le traitement d'images avec Python. Il couvre les concepts fondamentaux des tableaux multidimensionnels et leur application au traitement d'images.

## Structure du module

### **ex00 - Calcul d'IMC**
- **Objectif :** Manipulation de listes et calculs mathématiques
- **Fonctions :** `give_bmi()`, `apply_limit()`
- **Concepts :** Validation des données, gestion d'erreurs, calculs sur listes

### **ex01 - Manipulation de tableaux 2D**
- **Objectif :** Découpage de tableaux bidimensionnels
- **Fonction :** `slice_me()`
- **Concepts :** Slicing, dimensions de tableaux, validation de structure

### **ex02 - Chargement d'images**
- **Objectif :** Introduction au traitement d'images
- **Fonction :** `ft_load()`
- **Concepts :** PIL/Pillow, conversion NumPy, formats d'images

### **ex03 - Zoom sur image**
- **Objectif :** Découpage et conversion d'images
- **Programme :** `zoom.py`
- **Concepts :** Crop d'images, conversion en niveaux de gris, affichage matplotlib

### **ex04 - Rotation d'image**
- **Objectif :** Transformation géométrique d'images
- **Programme :** `rotate.py`
- **Concepts :** Transposition manuelle, rotation 90°, manipulation de pixels

### **ex05 - Filtres d'images**
- **Objectif :** Application de filtres colorés
- **Fonctions :** `ft_invert()`, `ft_red()`, `ft_green()`, `ft_blue()`, `ft_grey()`
- **Concepts :** Manipulation des canaux RGB, filtres colorés, effets visuels

## Dépendances principales
```txt
numpy>=1.21.0
matplotlib>=3.5.0
Pillow>=8.3.0
```

## Progression pédagogique

### **Niveau 1 : Bases (ex00-ex01)**
- Manipulation de listes Python
- Validation des données et gestion d'erreurs
- Introduction aux tableaux 2D

### **Niveau 2 : Images (ex02-ex03)**
- Chargement d'images avec PIL
- Conversion vers NumPy
- Découpage et transformation basique

### **Niveau 3 : Transformations (ex04-ex05)**
- Transformations géométriques
- Manipulation des canaux de couleur
- Filtres et effets visuels

## Concepts clés abordés

### **Tableaux NumPy**
- Création et manipulation de tableaux multidimensionnels
- Indexation et slicing avancé
- Opérations vectorisées

### **Traitement d'images**
- Formats d'images (JPEG)
- Représentation RGB des pixels
- Conversion couleur ↔ niveaux de gris

### **Transformations**
- Découpage (cropping)
- Rotation et transposition
- Filtres colorés

### **Visualisation**
- Affichage avec matplotlib
- Gestion des palettes de couleurs
- Interface graphique pour images

## Utilisation générale

### Installation des dépendances
```bash
pip install -r requirements.txt
```

### Exécution des exercices
```bash
# Exercices avec tests
cd ex00 && python tester.py
cd ex01 && python tester.py

# Programmes interactifs
cd ex03 && python zoom.py
cd ex04 && python rotate.py
cd ex05 && python tester.py
```

## Structure des fichiers
```
1_array/
├── ex00/           # Calcul IMC
│   ├── give_bmi.py
│   ├── tester.py
│   └── README.md
├── ex01/           # Tableaux 2D
│   ├── array2D.py
│   ├── tester.py
│   └── README.md
├── ex02/           # Chargement images
│   ├── load_image.py
│   ├── animal.jpeg
│   ├── landscape.jpg
│   └── README.md
├── ex03/           # Zoom image
│   ├── zoom.py
│   ├── load_image.py
│   ├── animal.jpeg
│   └── README.md
├── ex04/           # Rotation image
│   ├── rotate.py
│   ├── load_image.py
│   ├── animal.jpeg
│   └── README.md
├── ex05/           # Filtres image
│   ├── pimp_image.py
│   ├── load_image.py
│   ├── tester.py
│   ├── animal.jpeg
│   └── README.md
├── requirements.txt
└── README.md
```

## Objectifs d'apprentissage
À la fin de ce module, vous maîtriserez :
- La manipulation de tableaux NumPy
- Le chargement et traitement d'images
- Les transformations géométriques de base
- L'application de filtres colorés
- La visualisation d'images avec matplotlib
