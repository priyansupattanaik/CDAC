import matplotlib.pyplot as plt
import numpy as np

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

        # two charts side by side using subplot
        plt.figure(figsize=(10, 5))

        # left chart - line chart showing score over attempts
        plt.subplot(1, 2, 1)
        plt.plot(attempts, scores, color="blue", marker="o", label="Score %")
        plt.axhline(y=avg, color="red", linestyle="--", label="Average: " + str(round(avg, 1)) + "%")
        plt.title("Score Trend - " + self.username)
        plt.xlabel("Attempt No.")
        plt.ylabel("Score (%)")
        plt.ylim(0, 110)
        plt.legend()

        # right chart - bar chart of topic averages
        plt.subplot(1, 2, 2)
        topic_avg = df.groupby("topic")["percentage"].mean()
        topics = list(topic_avg.index)
        values = list(topic_avg.values)
        colors = ["skyblue", "lightgreen", "orange", "pink"]
        plt.bar(topics, values, color=colors[:len(topics)], edgecolor="black")
        plt.title("Topic-wise Average")
        plt.xlabel("Topic")
        plt.ylabel("Avg Score (%)")
        plt.xticks(rotation=15)
        plt.ylim(0, 110)

        plt.tight_layout()
        fname = self.username + "_score_trend.png"
        plt.savefig(fname)
        print("Chart saved as", fname)
        plt.show()

    def pie_chart(self, df):
        if df is None or len(df) == 0:
            print("No data to plot.")
            return

        # count how many times each topic was attempted
        topic_counts = df["topic"].value_counts()

        plt.figure(figsize=(6, 6))
        plt.pie(
            topic_counts.values,
            labels=topic_counts.index,
            autopct="%1.1f%%",
            startangle=90,
            colors=["#66b3ff", "#99ff99", "#ffcc99", "#ff9999"]
        )
        plt.title("Attempts by Topic - " + self.username)
        plt.axis("equal")

        fname = self.username + "_pie_chart.png"
        plt.savefig(fname)
        print("Pie chart saved as", fname)
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
