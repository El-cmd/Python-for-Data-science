import matplotlib.pyplot as plt
import numpy as np
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
from load_image import ft_load

def main():
    try:
        image = ft_load("landscape.jpg")  # charge l'image
        inverted_img = ft_red(image)

        # Affichage
        plt.imshow(inverted_img)
        plt.axis("off")
        plt.show()

    except (FileNotFoundError, TypeError, ValueError) as e:
        print(f"Erreur : {e}")


if __name__ == "__main__":
    main()
