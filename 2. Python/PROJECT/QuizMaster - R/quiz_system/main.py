from db import Database
from user import User
from quiz_engine import QuizEngine, TimedQuiz
from analytics import Analytics
from charts import Charts


def main():
    print("=" * 45)
    print("     WELCOME TO QUIZMASTER")
    print("     Online Quiz System with Analytics")
    print("=" * 45)

    db = Database()

    if db.conn is None:
        print("\nCould not connect to database. Please check your MySQL settings in db.py")
        return

    user = User(db)

    while True:
        print("\n" + "-" * 30)
        print("   MAIN MENU")
        print("-" * 30)
        print("  1. Register")
        print("  2. Login")
        print("  3. Exit")
        print("-" * 30)

        choice = input("Enter choice: ").strip()

        if choice == "1":
            user.register()

        elif choice == "2":
            success = user.login()
            if success:
                user_menu(db, user)
                user.logout()

        elif choice == "3":
            print("\nThank you for using QuizMaster. Goodbye!")
            db.close()
            break

        else:
            print("Invalid choice. Enter 1, 2 or 3.")


def user_menu(db, user):
    while True:
        print("\n" + "=" * 35)
        print(f"  Hello, {user.username}!")
        print("=" * 35)
        print("  1. Start Quiz  (Normal)")
        print("  2. Start Quiz  (Timed - 30 sec/question)")
        print("  3. View My Performance")
        print("  4. View My Charts")
        print("  5. Change Password")
        print("  6. Logout")
        print("-" * 35)

        choice = input("Enter choice: ").strip()

        if choice == "1":
            quiz = QuizEngine(db, user.user_id, user.username)
            quiz.run()

        elif choice == "2":
            quiz = TimedQuiz(db, user.user_id, user.username, time_limit=30)
            quiz.run()

        elif choice == "3":
            analytics = Analytics(db, user.user_id, user.username)
            analytics.show_performance()

        elif choice == "4":
            analytics = Analytics(db, user.user_id, user.username)
            df = analytics.get_dataframe()

            if df is not None:
                ch = Charts(user.username)
                print("\nWhich chart?")
                print("  1. Score Trend + Topic Bar Chart")
                print("  2. Topic Pie Chart")
                print("  3. Score Histogram")
                print("  4. All Charts")

                c = input("Choice: ").strip()
                if c == "1":
                    ch.score_trend(df)
                elif c == "2":
                    ch.topic_pie_chart(df)
                elif c == "3":
                    ch.score_histogram(df)
                elif c == "4":
                    ch.score_trend(df)
                    ch.topic_pie_chart(df)
                    ch.score_histogram(df)
                else:
                    print("Invalid choice.")
            else:
                print("Give at least one quiz first!")

        elif choice == "5":
            user.change_password()

        elif choice == "6":
            break

        else:
            print("Enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
