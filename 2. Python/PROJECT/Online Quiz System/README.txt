QuizMaster - Online Quiz System with Performance Analytics
CDAC Module End Project

HOW TO SETUP AND RUN
---------------------

Step 1 - Install libraries
   pip install mysql-connector-python pandas numpy matplotlib

Step 2 - Only change your MySQL password in db.py
   Open db.py and on line 8 and 18 change:
       password="root"
   to your actual MySQL password.
   That's it. No need to create database manually.

Step 3 - Run the project
   python main.py

   The database and tables are created automatically on first run.

FILES IN THIS PROJECT
---------------------
main.py        - starting point of the project
db.py          - handles mysql database connection and queries
user.py        - register and login
validators.py  - input validation using regex
question.py    - Question class and loading questions from csv
quiz_engine.py - runs the quiz, TimedQuiz inherits from QuizEngine
analytics.py   - shows performance report using pandas and numpy
charts.py      - draws charts using matplotlib
questions.csv  - 40 questions (10 each for Pandas, Matplotlib, Seaborn, MySQL)
results.csv    - gets created automatically after first quiz

OOP CONCEPTS
------------
Class        - Database, User, Question, QuestionBank, QuizEngine, TimedQuiz, Analytics, Charts
Encapsulation- self.__db in user.py and analytics.py (private variable)
Inheritance  - TimedQuiz class extends QuizEngine class
Polymorphism - run() method is different in QuizEngine and TimedQuiz
Exception    - try/except used in every file
