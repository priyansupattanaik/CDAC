import matplotlib.pyplot as plt
import numpy as np


class Charts:

    def __init__(self, username):
        self.username = username

    def score_trend(self, df):
        if df is None or len(df) == 0:
            print("No data available to plot.")
            return

        attempts    = list(range(1, len(df) + 1))
        percentages = df["percentage"].tolist()
        avg         = df["percentage"].mean()

        plt.figure(figsize=(10, 5))

        plt.subplot(1, 2, 1)
        plt.plot(attempts, percentages, color="blue", marker="o",
                 linestyle="-", linewidth=1.5, label="Score %")
        plt.axhline(y=avg, color="red", linestyle="--", label=f"Avg: {avg:.1f}%")
        plt.title(f"Score Trend - {self.username}")
        plt.xlabel("Attempt Number")
        plt.ylabel("Score (%)")
        plt.ylim(0, 110)
        plt.legend()

        plt.subplot(1, 2, 2)
        topic_avg = df.groupby("topic")["percentage"].mean()
        topics    = list(topic_avg.index)
        averages  = list(topic_avg.values)
        colours   = ["skyblue", "lightgreen", "orange", "pink", "lightcoral"]

        plt.bar(topics, averages,
                color=colours[:len(topics)],
                edgecolor="black")
        plt.title("Average Score by Topic")
        plt.xlabel("Topic")
        plt.ylabel("Average Score (%)")
        plt.xticks(rotation=15)
        plt.ylim(0, 110)

        plt.tight_layout()
        filename = f"{self.username}_score_report.png"
        plt.savefig(filename)
        print(f"\nChart saved as '{filename}'")
        plt.show()

    def topic_pie_chart(self, df):
        if df is None or len(df) == 0:
            print("No data available.")
            return

        topic_counts = df["topic"].value_counts()

        plt.figure(figsize=(6, 6))
        plt.pie(
            topic_counts.values,
            labels=topic_counts.index,
            autopct="%1.1f%%",
            startangle=90,
            colors=["#66b3ff", "#99ff99", "#ffcc99", "#ff9999", "#c2c2f0"]
        )
        plt.title(f"Attempts by Topic - {self.username}")
        plt.axis("equal")

        filename = f"{self.username}_topic_pie.png"
        plt.savefig(filename)
        print(f"Pie chart saved as '{filename}'")
        plt.show()

    def score_histogram(self, df):
        if df is None or len(df) < 3:
            print("Need at least 3 attempts for histogram.")
            return

        scores = df["percentage"].values

        plt.figure(figsize=(7, 4))
        plt.hist(scores, bins=5, color="steelblue", edgecolor="black")
        plt.title(f"Score Distribution - {self.username}")
        plt.xlabel("Score (%)")
        plt.ylabel("Frequency")
        plt.tight_layout()

        filename = f"{self.username}_histogram.png"
        plt.savefig(filename)
        print(f"Histogram saved as '{filename}'")
        plt.show()
