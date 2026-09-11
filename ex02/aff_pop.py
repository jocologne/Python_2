from load_csv import load
import matplotlib.pyplot as plt


def to_number(value):
    """Convert population string to float"""
    if isinstance(value, (int, float)):
        return float(value)
    value = str(value).strip()
    mult = {"k": 1_000, "M": 1_000_000, "B": 1_000_000_000}
    if value[-1] in mult:
        return float(value[:-1]) * mult[value[-1]]
    return float(value)


def main():
    try:
        data = load("population_total.csv")
        if data is None:
            raise AssertionError("Dataset could not be loaded")
        brazil = data[data["country"] == "Brazil"].iloc[0]
        france = data[data["country"] == "France"].iloc[0]
        years = [str(y) for y in range(1800, 2051)]
        brazil_values = brazil[years].apply(to_number)
        france_values = france[years].apply(to_number)
        plt.plot(years, brazil_values / 1_000_000, label="Brazil")
        plt.plot(years, france_values / 1_000_000, label="France")
        plt.legend()
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        step = 40
        plt.xticks(years[::step])
        plt.yticks()
        plt.savefig("plot.png")
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
