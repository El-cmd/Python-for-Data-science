import pandas as pd


def load(path: str):
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions: {df.shape}")
        return df
    except FileNotFoundError:
        print(f"Error: File not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: Empty dataset.")
    except pd.errors.ParserError:
        print(f"Error: File is not a valid CSV file.")
    except Exception as e:
        print(f"Error: {e}")
    return None