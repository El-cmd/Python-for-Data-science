import pandas as pd


def load(path: str):
    """
    Charge un fichier CSV et retourne un DataFrame.
    Args:
        path (str): Chemin du fichier CSV.
    Returns:
        pd.DataFrame: DataFrame contenant les données du fichier CSV.
    """
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions: {df.shape}")
        return df
    except FileNotFoundError:
        print("Error: File not found.")
    except pd.errors.EmptyDataError:
        print("Error: Empty dataset.")
    except pd.errors.ParserError:
        print("Error: File is not a valid CSV file.")
    except Exception as e:
        print(f"Error: {e}")
    return None
