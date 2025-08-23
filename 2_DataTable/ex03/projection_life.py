import pandas as pd
from load_csv import load
import matplotlib.pyplot as plt

def main():
    df = load("life_expectancy_years.csv")
    df2 = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    


if __name__ == "__main__":
    main()
    