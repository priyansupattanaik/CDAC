import pandas as pd
import numpy as np

# Analytics class computes statistics like average, max, min, median, and standard deviation using pandas/numpy.
class Analytics:

    def __init__(self, db, user_id, username):
        # private variables
        self.__db = db
        self.__user_id = user_id
        self.__username = username

    # private method to load data from db into a dataframe
    def __load_data(self):
        rows = self.__db.get_results(self.__user_id)
        if len(rows) == 0:
            return None
        df = pd.DataFrame(rows, columns=["id", "user_id", "username", "score", "total", "date"])
        # add percentage column
        df["percentage"] = round(df["score"] / df["total"] * 100, 1)
        return df

    def show_report(self):
        df = self.__load_data()

        if df is None:
            print("No attempts found. Give a quiz first!")
            return None

        print("\n=== Performance Report - " + self.__username + " ===")
        print("Total attempts :", len(df))
        print("Average score  :", round(df["percentage"].mean(), 1), "%")
        print("Best score     :", df["percentage"].max(), "%")
        print("Lowest score   :", df["percentage"].min(), "%")

        # using numpy for std deviation and median
        scores = df["percentage"].values
        print("Std Deviation  :", round(np.std(scores), 2))
        print("Median score   :", np.median(scores), "%")

        # last 5 attempts using tail
        print("\nLast 5 attempts:")
        last5 = df.tail(5)
        for index, row in last5.iterrows():
            d = str(row["date"])[:16]
            print(" ", str(row["score"]) + "/" + str(row["total"]), "|", str(row["percentage"]) + "% |", d)

        return df

    def get_data(self):
        return self.__load_data()
