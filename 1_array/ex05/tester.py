import matplotlib.pyplot as plt
from pimp_image import ft_invert
from load_image import ft_load


def main():
    try:
        image = ft_load("landscape.jpg")  # charge l'image
        inverted_img = ft_invert(image)

        # Affichage
        plt.imshow(inverted_img)
        plt.axis("off")
        plt.show()

    except (FileNotFoundError, TypeError, ValueError) as e:
        print(f"Erreur : {e}")


if __name__ == "__main__":
    main()
