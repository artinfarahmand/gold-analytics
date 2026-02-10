

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from src.preprocessing import get_event_window_returns

def plot_event_window(gold, events, window=5):

    sns.set(style="whitegrid")

    returns_df = get_event_window_returns(gold, events, window)

    plt.figure(figsize=(12, 6))

    for et in returns_df["type"].unique():
        temp = returns_df[returns_df["type"] == et]
        mean_returns = temp.groupby("day_relative")["return"].mean()
        plt.plot(mean_returns.index, mean_returns.values, label=et)

    plt.axvline(0, color="red", linestyle="--", label="Event Day")
    plt.xlabel("Days From Event")
    plt.ylabel("Average Daily Return")
    plt.title("Gold Return Around Economic Events")
    plt.legend()
    plt.show()
