from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Plot gdp vs life expectancy for 1900"""
    try:
        life = load("life_expectancy_years.csv")
        income = load("income.csv")
        if life is None or income is None:
            raise AssertionError("Dataset could not be loaded")
        life_ = life[["country", "1900"]]
        income_ = income[["country", "1900"]]
        merged = income_.merge(life_, on="country", suffixes=("_gdp", "_life"))
        plt.scatter(merged["1900_gdp"], merged["1900_life"])
        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life expectancy")
        plt.xscale("log")
        plt.savefig("plot.png")
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
