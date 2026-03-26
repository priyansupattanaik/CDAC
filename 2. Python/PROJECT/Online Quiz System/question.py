import csv
import numpy as np

# Class to represent a single question and QuestionBank to manage multiple questions loaded from CSV.
class Question:

    def __init__(self, text, a, b, c, d, answer):
        self.text = text
        self.answer = answer.strip().upper()
        # storing options in a dictionary
        self.options = {"A": a, "B": b, "C": c, "D": d}

    def show(self, num):
        print("\nQ" + str(num) + ". " + self.text)
        for key in self.options:
            print("  " + key + ". " + self.options[key])

    def is_correct(self, user_ans):
        return user_ans.strip().upper() == self.answer


class QuestionBank:

    def __init__(self):
        self.questions = []
        self.load_questions()

    def load_questions(self):
        try:
            f = open("questions.csv", "r")
            reader = csv.DictReader(f)
            for row in reader:
                q = Question(
                    row["question"],
                    row["option_a"],
                    row["option_b"],
                    row["option_c"],
                    row["option_d"],
                    row["answer"]
                )
                self.questions.append(q)
            f.close()
            print(str(len(self.questions)) + " questions loaded.")
        except FileNotFoundError:
            print("questions.csv not found!")
            raise

    def get_questions(self, count):
        pool = self.questions
        if len(pool) == 0:
            print("No questions found.")
            return []

        # use numpy to randomly pick questions
        indexes = np.arange(len(pool))
        np.random.shuffle(indexes)
        selected = []
        for i in indexes[:count]:
            selected.append(pool[i])
        return selected
