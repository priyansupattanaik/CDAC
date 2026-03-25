import csv
import numpy as np

class Question:

    def __init__(self, text, a, b, c, d, answer, topic):
        self.text = text
        self.topic = topic
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
                    row["answer"],
                    row["topic"]
                )
                self.questions.append(q)
            f.close()
            print(str(len(self.questions)) + " questions loaded.")
        except FileNotFoundError:
            print("questions.csv not found!")
            raise

    def get_topics(self):
        # count how many questions per topic using a dictionary
        topic_count = {}
        for q in self.questions:
            if q.topic in topic_count:
                topic_count[q.topic] += 1
            else:
                topic_count[q.topic] = 1
        return topic_count

    def get_questions(self, topic, count):
        # filter questions by topic
        if topic == "All":
            pool = self.questions
        else:
            pool = []
            for q in self.questions:
                if q.topic == topic:
                    pool.append(q)

        if len(pool) == 0:
            print("No questions found for this topic.")
            return []

        # use numpy to randomly pick questions
        indexes = np.arange(len(pool))
        np.random.shuffle(indexes)
        selected = []
        for i in indexes[:count]:
            selected.append(pool[i])
        return selected
