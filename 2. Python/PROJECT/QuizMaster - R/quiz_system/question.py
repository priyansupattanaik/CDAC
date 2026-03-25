import csv
import numpy as np


class Question:

    def __init__(self, text, option_a, option_b, option_c, option_d, answer, topic):
        self.text   = text
        self.topic  = topic
        self.answer = answer.strip().upper()
        self.options = {
            "A": option_a,
            "B": option_b,
            "C": option_c,
            "D": option_d
        }

    def display(self, number):
        print(f"\nQ{number}. {self.text}")
        for key, value in self.options.items():
            print(f"   {key}.  {value}")

    def is_correct(self, user_answer):
        return user_answer.strip().upper() == self.answer


class QuestionBank:

    def __init__(self, filepath="questions.csv"):
        self.filepath      = filepath
        self.all_questions = []
        self.load_from_csv()

    def load_from_csv(self):
        try:
            with open(self.filepath, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    q = Question(
                        row["question"],
                        row["option_a"],
                        row["option_b"],
                        row["option_c"],
                        row["option_d"],
                        row["answer"],
                        row["topic"]
                    )
                    self.all_questions.append(q)
            print(f"{len(self.all_questions)} questions loaded from {self.filepath}")

        except FileNotFoundError:
            print(f"Error: {self.filepath} not found.")
            raise

    def get_topics(self):
        topic_count = {}
        for q in self.all_questions:
            if q.topic in topic_count:
                topic_count[q.topic] += 1
            else:
                topic_count[q.topic] = 1
        return topic_count

    def get_questions(self, topic=None, count=5):
        if topic and topic != "All":
            pool = [q for q in self.all_questions if q.topic == topic]
        else:
            pool = self.all_questions

        if len(pool) == 0:
            print("No questions found for this topic.")
            return []

        indices = np.arange(len(pool))
        np.random.shuffle(indices)
        return [pool[i] for i in indices[:count]]
