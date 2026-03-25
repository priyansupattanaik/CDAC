import pandas as pd
import numpy as np


class Analytics:

    def __init__(self, db, user_id, username):
        self.__db       = db
        self.__user_id  = user_id
        self.__username = username

    def __load_data(self):
        rows = self.__db.get_all_results(self.__user_id)
        if not rows:
            return None
        df = pd.DataFrame(rows, columns=["id", "user_id", "username", "score", "total", "topic", "date"])
        df["percentage"] = (df["score"] / df["total"] * 100).round(1)
        return df

    def show_performance(self):
        df = self.__load_data()

        if df is None:
            print("\nNo quiz attempts found. Give a quiz first!")
            return None

        print("\n" + "=" * 45)
        print(f"    PERFORMANCE REPORT  -  {self.__username}")
        print("=" * 45)

        print(f"\n  Total attempts   :  {len(df)}")
        print(f"  Average score    :  {df['percentage'].mean():.1f}%")
        print(f"  Best score       :  {df['percentage'].max():.1f}%")
        print(f"  Lowest score     :  {df['percentage'].min():.1f}%")

        scores = df["percentage"].values
        print(f"  Std deviation    :  {np.std(scores):.2f}")
        print(f"  Median score     :  {np.median(scores):.1f}%")

        print("\n  Topic-wise Average:")
        topic_avg  = df.groupby("topic")["percentage"].mean()
        topic_dict = topic_avg.to_dict()

        for topic, avg in topic_dict.items():
            bar = "#" * int(avg // 10)
            print(f"  {topic:12s}  :  {avg:.1f}%  {bar}")

        print("\n  Last 5 attempts:")
        print(f"  {'Topic':<15} {'Score':<10} {'%':<8} {'Date'}")
        print("  " + "-" * 45)

        recent = df.tail(5)
        for _, row in recent.iterrows():
            date_str = str(row["date"])[:16]
            print(f"  {row['topic']:<15} {row['score']}/{row['total']:<8} {row['percentage']:.1f}%    {date_str}")

        print("=" * 45)
        return df

    def get_dataframe(self):
        return self.__load_data()
