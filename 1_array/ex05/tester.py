from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
from load_image import ft_load


def main():
    try:
        image = ft_load("landscape.jpg")  # charge l'image
        ft_invert(image)
        ft_red(image)
        ft_green(image)
        ft_blue(image)
        ft_grey(image)
        print(ft_invert.__doc__)

    except (FileNotFoundError, TypeError, ValueError) as e:
        print(f"Erreur : {e}")


if __name__ == "__main__":
    main()
