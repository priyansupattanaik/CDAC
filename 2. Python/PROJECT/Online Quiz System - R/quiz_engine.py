import csv
import time
from datetime import datetime
from question import QuestionBank
from validators import check_answer

# QuizEngine and TimedQuiz handle the core quiz logic, user input, and result calculation.
class QuizEngine:

    def __init__(self, db, user_id, username):
        self._db = db
        self._user_id = user_id
        self._username = username
        self._bank = QuestionBank()
        self._score = 0
        self._total = 0

    def ask_count(self):
        try:
            n = int(input("How many questions? (1-10): "))
            if n < 1:
                n = 1
            if n > 10:
                n = 10
        except ValueError:
            n = 5
        return n

    def run(self):
        print("\n=== Quiz Starting ===")
        count = self.ask_count()
        questions = self._bank.get_questions(count)

        self._total = len(questions)
        self._score = 0
        wrong = []

        for i in range(len(questions)):
            q = questions[i]
            q.show(i + 1)

            # keep asking until valid answer given
            while True:
                ans = input("Your answer (A/B/C/D): ").strip()
                try:
                    check_answer(ans)
                    break
                except ValueError as e:
                    print(e)

            if q.is_correct(ans):
                self._score += 1
                print("Correct!")
            else:
                print("Wrong! Correct answer was: " + q.answer)
                wrong.append((q.text, q.answer))

        self.save_result()
        self.show_result(wrong)

    def save_result(self):
        # save to mysql
        self._db.save_result(self._user_id, self._username, self._score, self._total)

        # also save to csv file
        try:
            f = open("results.csv", "a", newline="")
            writer = csv.writer(f)
            pct = round((self._score / self._total) * 100, 1)
            now = datetime.now().strftime("%Y-%m-%d %H:%M")
            writer.writerow([self._username, self._score, self._total, pct, now])
            f.close()
        except Exception as e:
            print("Could not save to csv:", e)

    def show_result(self, wrong):
        pct = round((self._score / self._total) * 100, 1)

        if pct >= 80:
            grade = "A - Excellent!"
        elif pct >= 60:
            grade = "B - Good"
        elif pct >= 40:
            grade = "C - Average"
        else:
            grade = "F - Need more practice"

        print("\n=== Your Result ===")
        print("Score     :", self._score, "/", self._total)
        print("Percentage:", str(pct) + "%")
        print("Grade     :", grade)

        if len(wrong) > 0:
            print("\nQuestions you got wrong:")
            for item in wrong:
                print(" -", item[0][:50], "| Ans:", item[1])

        print("Result saved!")


# TimedQuiz inherits from QuizEngine (Inheritance)
class TimedQuiz(QuizEngine):

    def __init__(self, db, user_id, username):
        super().__init__(db, user_id, username)
        self.time_limit = 30   # 30 seconds per question

    # overriding run() method from QuizEngine (Polymorphism)
    def run(self):
        print("\n=== Timed Quiz (30 sec per question) ===")
        count = self.ask_count()
        questions = self._bank.get_questions(count)

        self._total = len(questions)
        self._score = 0
        wrong = []

        for i in range(len(questions)):
            q = questions[i]
            q.show(i + 1)
            print("You have 30 seconds!")

            start = time.time()
            ans = input("Your answer (A/B/C/D): ").strip()
            taken = time.time() - start

            # check if time exceeded
            if taken > self.time_limit:
                print("Time up! (" + str(round(taken, 1)) + "s) - skipped.")
                wrong.append((q.text, q.answer))
                continue

            try:
                check_answer(ans)
            except ValueError:
                print("Invalid input - skipped.")
                wrong.append((q.text, q.answer))
                continue

            if q.is_correct(ans):
                self._score += 1
                print("Correct! Answered in " + str(round(taken, 1)) + "s")
            else:
                print("Wrong! Correct answer:", q.answer)
                wrong.append((q.text, q.answer))

        self.save_result()
        self.show_result(wrong)
