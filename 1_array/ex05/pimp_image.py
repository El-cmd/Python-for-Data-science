import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
Inverse les couleurs de l'image.
    """
    inverted = array.copy()
    inverted[:, :, 0] = 255 - inverted[:, :, 0]  # 0 = canal rouge
    inverted[:, :, 1] = 255 - inverted[:, :, 1]  # 1 = canal vert
    inverted[:, :, 2] = 255 - inverted[:, :, 2]  # 2 = canal bleu
    plt.imshow(inverted)
    plt.axis("off")
    plt.show()
    return inverted


def ft_red(array: np.ndarray) -> np.ndarray:
    """
Retire les couleurs vertes et bleues de l'image.
    """
    red = array.copy()
    red[:, :, 1] = 0  # 1 = canal vert
    red[:, :, 2] = 0  # 2 = canal bleu
    plt.imshow(red)
    plt.axis("off")
    plt.show()
    return red


def ft_green(array: np.ndarray) -> np.ndarray:
    """
Retire les couleurs rouges et bleues de l'image.
    """
    green = array.copy()
    green[:, :, 0] = 0  # 0 = canal rouge
    green[:, :, 2] = 0  # 2 = canal bleu
    plt.imshow(green)
    plt.axis("off")
    plt.show()
    return green


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
Retire les couleurs rouges et vertes de l'image.
    """
    blue = array.copy()
    blue[:, :, 0] = 0  # 0 = canal rouge
    blue[:, :, 1] = 0  # 1 = canal vert
    plt.imshow(blue)
    plt.axis("off")
    plt.show()
    return blue


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
Convertit l'image en niveaux de gris.
    """
    grey = array.copy()
    grey[:, :, 0] = np.mean(grey[:, :, :3], axis=2)
    grey[:, :, 1] = grey[:, :, 0]  # 1 = canal vert
    grey[:, :, 2] = grey[:, :, 0]  # 2 = canal bleu
    plt.imshow(grey)
    plt.axis("off")
    plt.show()
    return grey
