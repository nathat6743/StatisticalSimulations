import numpy as np
import matplotlib.pyplot as plt

def roll_die(num_rolls):
    return np.random.randint(1, 7, size=num_rolls)

def calculate_frequencies(rolls):
    values, counts = np.unique(rolls, return_counts=True)
    return values, counts

def plot_frequencies(values, counts):
    plt.bar(values, counts, tick_label=values)
    plt.title("Die Roll Frequencies")
    plt.xlabel("Die Face")
    plt.ylabel("Frequency")
    plt.show()

def main():
    num_rolls = 10000
    rolls = roll_die(num_rolls)
    values, counts = calculate_frequencies(rolls)
    plot_frequencies(values, counts)

if __name__ == "__main__":
    main()