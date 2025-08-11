from load_image import ft_load

if __name__ == "__main__":
    try:
        print(ft_load("landscape.jpg"))
    except (TypeError, ValueError, FileNotFoundError) as e:
        print(f"Erreur : {e}")
