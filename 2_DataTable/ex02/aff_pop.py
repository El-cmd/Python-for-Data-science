import pandas as pd
from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def convert_population(value):
    """Convertit les valeurs comme '29M', '500k', '1.4B' en nombres"""
    if pd.isna(value):
        return 0
    value_str = str(value)
    if value_str.endswith('B'):
        return float(value_str[:-1]) * 1_000_000_000
    elif value_str.endswith('M'):
        return float(value_str[:-1]) * 1_000_000
    elif value_str.endswith('k'):
        return float(value_str[:-1]) * 1_000
    else:
        try:
            return float(value_str)
        except ValueError:
            return 0


def main():
    """
    Charge un fichier CSV et affiche la projection
    de la population de la France et du Brésil dans un graph.
    """
    try:
        df = load("population_total.csv")
        france_row = df[df['country'] == 'France'].iloc[0]
        belgium_row = df[df['country'] == 'Brazil'].iloc[0]
        years = [int(col) for col in df.columns if col != 'country' and int(col) <= 2050]  # noqa: E501
        france_population = [convert_population(france_row[str(year)]) / 1_000_000 for year in years]  # noqa: E501
        belgium_population = [convert_population(belgium_row[str(year)]) / 1_000_000 for year in years]  # noqa: E501
        plt.plot(years, belgium_population, label="Brazil")
        plt.plot(years, france_population, label="France")
        plt.title("Population Projections")
        plt.xlabel("Years")
        plt.ylabel("Population")

        def format_millions(x, pos):
            return f'{int(x)}M'
        plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(format_millions))  # noqa: E501
        plt.legend()
        plt.show()
        plt.close()
    except Exception:
        return


if __name__ == "__main__":
    main()
