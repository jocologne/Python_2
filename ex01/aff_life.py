from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Plot a country life expectancy graph"""
    try:
        data = load("life_expectancy_years.csv")
        if data is None:
            raise AssertionError("Dataset could not be loaded")
        values = data[data["country"] == "Brazil"]
        if values.empty:
            raise AssertionError("Country not found")
        line = values.iloc[0]
        years = line.drop("country")
        plt.plot(years.index, years.values)
        plt.title("Brazil life expectancy projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        step = 40
        plt.xticks(years.index[::step])
        plt.savefig("plot.png")
    except Exception as error:
        print(f"Error, {error}")


if __name__ == "__main__":
    main()
