from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    try:
        image = ft_load("animal.jpeg")
        h, w = image.shape[:2]
        start_y, start_x = (h-400)//2, (w-400)//2
        cropped = image[start_y:start_y+400, start_x:start_x+400]
        gray = np.mean(cropped, axis=2, keepdims=True).astype(np.uint8)
        print(f"The shape of image is: {gray.shape} or ({gray.shape[0]},{gray.shape[1]})")
        print(gray)
        rotated = np.rot90(gray)
        print(f"New shape after Transpose: ({rotated.shape[0]},{rotated.shape[1]})")
        print(rotated)
        plt.imshow(rotated.squeeze(), cmap="gray")
        plt.show()
    except (TypeError, ValueError, FileNotFoundError) as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    main()
