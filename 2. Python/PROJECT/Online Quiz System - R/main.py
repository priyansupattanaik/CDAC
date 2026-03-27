from db import Database
from user import User
from quiz_engine import QuizEngine, TimedQuiz
from analytics import Analytics
from charts import Charts

# Main entry point of the application, handling user registration, login, and the main menu loop.
def main():
    print("=== Welcome to QuizMaster ===")
    print("Online Quiz System with Analytics")
    print("=" * 35)

    db = Database()

    if db.conn is None:
        print("Cannot connect to database. Check password in db.py")
        return

    user = User(db)

    while True:
        print("\n--- Main Menu ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        ch = input("Enter choice: ").strip()

        if ch == "1":
            user.register()

        elif ch == "2":
            ok = user.login()
            if ok:
                user_menu(db, user)
                user.logout()

        elif ch == "3":
            print("Goodbye!")
            db.close()
            break

        else:
            print("Enter 1, 2 or 3 only.")


def user_menu(db, user):
    while True:
        print("\n--- Hello " + user.username + "! ---")
        print("1. Start Normal Quiz")
        print("2. Start Timed Quiz")
        print("3. View Performance Report")
        print("4. View Charts")
        print("5. Change Password")
        print("6. Logout")

        ch = input("Enter choice: ").strip()

        if ch == "1":
            q = QuizEngine(db, user.user_id, user.username)
            q.run()

        elif ch == "2":
            q = TimedQuiz(db, user.user_id, user.username)
            q.run()

        elif ch == "3":
            a = Analytics(db, user.user_id, user.username)
            a.show_report()

        elif ch == "4":
            a = Analytics(db, user.user_id, user.username)
            df = a.get_data()

            if df is not None:
                c = Charts(user.username)
                print("\nWhich chart do you want?")
                print("1. Score Trend Line Chart")
                print("2. Score Histogram")
                print("3. All Charts")

                ch2 = input("Choice: ").strip()
                if ch2 == "1":
                    c.score_trend(df)
                elif ch2 == "2":
                    c.histogram(df)
                elif ch2 == "3":
                    c.score_trend(df)
                    c.histogram(df)
                else:
                    print("Invalid choice.")
            else:
                print("Give atleast one quiz first!")

        elif ch == "5":
            user.change_password()

        elif ch == "6":
            break

        else:
            print("Enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
