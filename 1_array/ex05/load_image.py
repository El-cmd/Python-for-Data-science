from PIL import Image
import numpy as np
import os


def ft_load(path: str) -> np.ndarray:
    """
    Charge une image depuis `path` et retourne un tableau NumPy.

    Args:
        path (str): Chemin du fichier image.

    Returns:
        np.ndarray: Tableau représentant l'image.

    Raises:
        FileNotFoundError: Si l'image n'existe pas.
        ValueError: Si l'image ne peut pas être ouverte.
    """
    if not isinstance(path, str):
        raise TypeError("Path must be a string")
    if not path.endswith(".jpg") and not path.endswith(".jpeg"):
        raise ValueError("Path must be a .jpg or .jpeg file")
    if not os.path.exists(path):
        raise FileNotFoundError("File not found")
    img = Image.open(path)  # ouvre l'image
    array = np.array(img)
    print(f"The shape of image is: {array.shape}")
    return array
