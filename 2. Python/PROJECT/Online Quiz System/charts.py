import matplotlib.pyplot as plt
import numpy as np

# Charts class handles generating matplotlib charts for user performance.
class Charts:

    def __init__(self, username):
        self.username = username

    def score_trend(self, df):
        if df is None or len(df) == 0:
            print("No data to plot.")
            return

        attempts = list(range(1, len(df) + 1))
        scores = df["percentage"].tolist()
        avg = df["percentage"].mean()

        plt.figure(figsize=(7, 5))
        plt.plot(attempts, scores, color="blue", marker="o", label="Score %")
        plt.axhline(y=avg, color="red", linestyle="--", label="Average: " + str(round(avg, 1)) + "%")
        plt.title("Score Trend - " + self.username)
        plt.xlabel("Attempt No.")
        plt.ylabel("Score (%)")
        plt.ylim(0, 110)
        plt.legend()

        plt.tight_layout()
        fname = self.username + "_score_trend.png"
        plt.savefig(fname)
        print("Chart saved as", fname)
        plt.show()

    def histogram(self, df):
        if df is None or len(df) < 3:
            print("Need atleast 3 attempts for histogram.")
            return

        scores = df["percentage"].values

        plt.figure(figsize=(7, 4))
        plt.hist(scores, bins=5, color="steelblue", edgecolor="black")
        plt.title("Score Distribution - " + self.username)
        plt.xlabel("Score (%)")
        plt.ylabel("Frequency")
        plt.tight_layout()

        fname = self.username + "_histogram.png"
        plt.savefig(fname)
        print("Histogram saved as", fname)
        plt.show()
