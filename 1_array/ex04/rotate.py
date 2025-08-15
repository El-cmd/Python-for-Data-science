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
        print(f"The shape of image is: {gray.shape} or ({gray.shape[0]},{gray.shape[1]})") # noqa
        print(gray)
        gray_2d = gray.squeeze()
        h, w = gray_2d.shape[0], gray_2d.shape[1]
        transposed = np.zeros((w, h) + gray_2d.shape[2:], dtype=gray_2d.dtype)
        for i in range(h):
            for j in range(w):
                transposed[j][i] = gray_2d[i][j]
        print(f"New shape after Transpose: ({transposed.shape[0]},{transposed.shape[1]})") # noqa
        print(transposed)
        plt.imshow(transposed, cmap="gray")
        plt.show()
    except (TypeError, ValueError, FileNotFoundError) as e:
        print(f"Erreur : {e}")


if __name__ == "__main__":
    main()
