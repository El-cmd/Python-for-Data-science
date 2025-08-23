import pandas as pd
from load_csv import load
import matplotlib.pyplot as plt

def main():
    try:
        df = load("life_expectancy_years.csv")
        france_row = df[df['country'] == 'France'].iloc[0]
        years = [int(col) for col in df.columns if col != 'country']
        life_expectancy = [france_row[str(year)] for year in years]
        plt.plot(years, life_expectancy)
        plt.title("France Life expectancy Projection")
        plt.xlabel("Years")
        plt.ylabel("Life expectancy")
        plt.show()
        plt.close()
    except Exception:
        return

if __name__ == "__main__":
    main()