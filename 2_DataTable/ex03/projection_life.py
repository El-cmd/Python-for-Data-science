from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def main():
    """
    Charge un fichier CSV et affiche la projection
    de la longévité de la France dans un graph.
    """
    try:
        df = load("life_expectancy_years.csv")
        df2 = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        plt.plot(df2['1900'], df['1900'], 'bo')
        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")

        # Formater l'axe X pour afficher 100, 1K, 10K, etc.
        def format_income(x, pos):
            """
            Formate les valeurs de l'axe X pour afficher 100, 1K, 10K, etc.
            """
            if x >= 1000:
                return f'{int(x/1000)}K'
            else:
                return f'{int(x)}'
        plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(format_income))  # noqa: E501
        plt.show()
        plt.close()
    except Exception:
        return


if __name__ == "__main__":
    main()
