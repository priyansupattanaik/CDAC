import csv
import time
from datetime import datetime
from question import QuestionBank
from validators import validate_answer


class QuizEngine:

    def __init__(self, db, user_id, username):
        self._db       = db
        self._user_id  = user_id
        self._username = username
        self._bank     = QuestionBank()
        self._score    = 0
        self._total    = 0
        self._topic    = "All"

    def _pick_topic(self):
        topics = self._bank.get_topics()
        print("\nAvailable Topics:")
        topic_list = ["All"] + list(topics.keys())
        for i, t in enumerate(topic_list):
            if t == "All":
                print(f"  {i}. All Topics")
            else:
                print(f"  {i}. {t}  ({topics[t]} questions)")

        try:
            choice = int(input("\nChoose topic number: "))
            if 0 <= choice < len(topic_list):
                self._topic = topic_list[choice]
            else:
                self._topic = "All"
        except ValueError:
            self._topic = "All"

    def _ask_question_count(self):
        try:
            count = int(input("How many questions do you want? (1-10): "))
            count = max(1, min(count, 10))
        except ValueError:
            count = 5
        return count

    def run(self):
        print("\n" + "=" * 40)
        print("          QUIZ STARTING!")
        print("=" * 40)

        self._pick_topic()
        count     = self._ask_question_count()
        questions = self._bank.get_questions(self._topic, count)

        self._total = len(questions)
        self._score = 0
        wrong_ones  = []

        for i, q in enumerate(questions, 1):
            q.display(i)
            while True:
                answer = input("\nYour answer (A/B/C/D): ").strip()
                try:
                    validate_answer(answer)
                    break
                except ValueError as e:
                    print(f"  {e}")

            if q.is_correct(answer):
                self._score += 1
                print("  Correct!")
            else:
                print(f"  Wrong! The correct answer was: {q.answer}")
                wrong_ones.append((q.text, q.answer))

        self._save_result()
        self._show_result(wrong_ones)

    def _save_result(self):
        self._db.save_result(
            self._user_id,
            self._username,
            self._score,
            self._total,
            self._topic
        )
        try:
            with open("results.csv", "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([
                    self._username,
                    self._score,
                    self._total,
                    round((self._score / self._total) * 100, 1),
                    self._topic,
                    datetime.now().strftime("%Y-%m-%d %H:%M")
                ])
        except Exception as e:
            print(f"Could not save to results.csv: {e}")

    def _show_result(self, wrong_ones):
        percentage = round((self._score / self._total) * 100, 1)

        if percentage >= 80:
            grade = "A  - Excellent!"
        elif percentage >= 60:
            grade = "B  - Good"
        elif percentage >= 40:
            grade = "C  - Average"
        else:
            grade = "F  - Need more practice"

        print("\n" + "=" * 40)
        print("            YOUR RESULT")
        print("=" * 40)
        print(f"  Score      :  {self._score} / {self._total}")
        print(f"  Percentage :  {percentage}%")
        print(f"  Grade      :  {grade}")

        if wrong_ones:
            print("\n  Questions you got wrong:")
            for text, correct in wrong_ones:
                print(f"  - {text[:50]}...  Ans: {correct}")

        print("=" * 40)
        print("  Result saved successfully!")


class TimedQuiz(QuizEngine):

    def __init__(self, db, user_id, username, time_limit=30):
        super().__init__(db, user_id, username)
        self.time_limit = time_limit

    def run(self):
        print("\n" + "=" * 40)
        print(f"   TIMED QUIZ  ({self.time_limit} sec per question)")
        print("=" * 40)

        self._pick_topic()
        count     = self._ask_question_count()
        questions = self._bank.get_questions(self._topic, count)

        self._total = len(questions)
        self._score = 0
        wrong_ones  = []

        for i, q in enumerate(questions, 1):
            q.display(i)
            print(f"  [You have {self.time_limit} seconds]")

            start_time = time.time()
            answer     = input("\nYour answer (A/B/C/D): ").strip()
            elapsed    = time.time() - start_time

            if elapsed > self.time_limit:
                print(f"  Time's up! ({elapsed:.1f}s) - question skipped.")
                wrong_ones.append((q.text, q.answer))
                continue

            try:
                validate_answer(answer)
            except ValueError:
                print("  Invalid input - skipped.")
                wrong_ones.append((q.text, q.answer))
                continue

            if q.is_correct(answer):
                self._score += 1
                print(f"  Correct!  (answered in {elapsed:.1f}s)")
            else:
                print(f"  Wrong! Correct answer: {q.answer}")
                wrong_ones.append((q.text, q.answer))

        self._save_result()
        self._show_result(wrong_ones)
