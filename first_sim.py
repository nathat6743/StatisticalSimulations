import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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

def init_plot(bars, num_rolls, ax):
    """Initial setup for the plot."""
    ax.set_ylim(0, num_rolls // 6 + num_rolls * 0.1)  # Set y-axis limit
    return bars    

def update(frame, bars, cumulative_rolls,num_rolls,num_frames):
    new_rolls = roll_die(int(num_rolls/num_frames))
    # Calculate cumulative frequencies
    cumulative_rolls.extend(new_rolls)
    values, counts = calculate_frequencies(cumulative_rolls)
    for bar, count in zip(bars, counts):
        bar.set_height(count)

    return bars

def run_animation(fig, ax, num_rolls,num_frames):
    values = np.arange(1, 7)  # Die faces: 1 to 6
    counts = np.zeros_like(values)  # Initial counts
    
    bars = ax.bar(values, counts, tick_label=values)
    ax.set_title("Die Roll Frequencies Over Time")
    ax.set_xlabel("Die Face")
    ax.set_ylabel("Frequency")

    cumulative_rolls = []

    # Create animation object
    ani = FuncAnimation(fig, update, frames=num_frames,
                        fargs=(bars, cumulative_rolls,num_rolls,num_frames), init_func=lambda: init_plot(bars, num_rolls, ax), 
                        blit=True, repeat=False)
    
    plt.show()
    

def main():
    num_rolls = 10000
    num_frames = 100
    fig, ax = plt.subplots()
    run_animation(fig, ax, num_rolls,num_frames)

if __name__ == "__main__":
    main()