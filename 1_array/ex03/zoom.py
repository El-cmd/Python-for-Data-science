from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    try:
        # ========== ÉTAPE 1: CHARGEMENT DE L'IMAGE ==========
        # Charge l'image "animal.jpeg" et affiche automatiquement sa forme
        # Retourne un tableau NumPy de forme (hauteur, largeur, canaux)
        image = ft_load("animal.jpeg")
        # Affiche le contenu complet de l'image (tous les pixels RGB)
        # Format: [[[R, G, B], [R, G, B], ...], [[R, G, B], ...], ...]
        print(image)
        # ========== ÉTAPE 2: CALCUL DE LA ZONE DE CROP ==========
        # Récupère les dimensions de l'image (hauteur, largeur)
        # image.shape = (768, 1024, 3) donc h=768, w=1024
        h, w = image.shape[:2]
        # Calcule les coordonnées pour centrer un crop de 400x400 pixels
        # start_y = (768-400)//2 = 184 (début en Y)
        # start_x = (1024-400)//2 = 312 (début en X)
        start_y, start_x = (h-400)//2, (w-400)//2
        # ========== ÉTAPE 3: DÉCOUPAGE (CROP) DE L'IMAGE ==========
        # Découpe une zone centrale de 400x400 pixels
        # cropped aura la forme (400, 400, 3) - toujours en RGB
        cropped = image[start_y:start_y+400, start_x:start_x+400]
        # ========== ÉTAPE 4: CONVERSION EN NIVEAUX DE GRIS ==========
        # np.mean(cropped, axis=2) : calcule la moyenne des 3 canaux RGB
        # pour chaque pixel
        # axis=2 signifie "moyenner sur la dimension des canaux (R, G, B)"
        # keepdims=True : garde la dimension du canal, résultat
        # (400, 400, 1) au lieu de (400, 400)
        # .astype(np.uint8) : convertit en entiers 8-bits (0-255)
        gray = np.mean(cropped, axis=2, keepdims=True).astype(np.uint8)
        # ========== ÉTAPE 5: AFFICHAGE DES INFORMATIONS ==========
        # Affiche la nouvelle forme après découpage et conversion
        print(f"New shape after slicing: {gray.shape}")
        # Affiche le contenu de l'image en niveaux de gris
        # Format: [[[valeur], [valeur], ...], [[valeur], ...], ...]
        print(gray)
        # ========== ÉTAPE 6: PRÉPARATION POUR L'AFFICHAGE ==========
        # gray.squeeze() : enlève la dimension 1 pour matplotlib
        # (400, 400, 1) devient (400, 400) pour l'affichage
        # cmap='gray' : utilise une palette de couleurs en niveaux de gris
        plt.imshow(gray.squeeze(), cmap='gray')
        # Tente d'afficher l'image dans une fenêtre
        # (peut échouer selon l'environnement)
        plt.show()
    except (TypeError, ValueError, FileNotFoundError) as e:
        # Gestion des erreurs : affiche un message clair en cas de problème
        print(f"Erreur : {e}")


if __name__ == "__main__":
    main()
