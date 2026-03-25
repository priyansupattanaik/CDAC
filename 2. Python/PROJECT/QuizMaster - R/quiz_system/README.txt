========================================
   QUIZMASTER — Online Quiz System
   with Performance Analytics
========================================

SETUP INSTRUCTIONS
------------------

STEP 1 — Install required Python libraries
   pip install mysql-connector-python pandas numpy matplotlib

STEP 2 — Create the MySQL database
   Open MySQL command line or MySQL Workbench and run:
   CREATE DATABASE quiz_system;

STEP 3 — Set your MySQL password in db.py
   Open db.py and find this line (line 9):
       password="root"
   Change "root" to your actual MySQL root password.
   Save the file.

STEP 4 — Run the project
   Open terminal / command prompt in the quiz_system folder and run:
       python main.py

   Tables (users, results) are created automatically on first run.
   questions.csv is already included with 40 questions.
   results.csv is created automatically after the first quiz attempt.

========================================
FOLDER STRUCTURE
========================================

quiz_system/
├── main.py           ← Entry point — run this file
├── db.py             ← MySQL connection and CRUD
├── user.py           ← User class: register, login, logout
├── validators.py     ← Regex validation functions
├── question.py       ← Question and QuestionBank classes
├── quiz_engine.py    ← QuizEngine and TimedQuiz classes
├── analytics.py      ← Analytics class (Pandas + NumPy)
├── charts.py         ← Charts class (Matplotlib)
├── questions.csv     ← 40 questions across 4 topics
├── results.csv       ← Auto-created after first quiz
└── README.txt        ← This file

========================================
TOPICS COVERED IN QUIZ
========================================
  - Pandas       (10 questions)
  - Matplotlib   (10 questions)
  - Seaborn      (10 questions)
  - MySQL        (10 questions)

========================================
FEATURES
========================================
  - Register and Login with regex validation
  - Normal Quiz (no time limit)
  - Timed Quiz  (30 seconds per question)
  - Performance Analytics report
  - 4 Chart types: Line, Bar, Pie, Histogram
  - Results stored in MySQL + results.csv

========================================
OOP CONCEPTS USED
========================================
  - Classes & Objects  : All 8 .py files
  - Encapsulation      : __db in user.py and analytics.py
  - Inheritance        : TimedQuiz extends QuizEngine
  - Polymorphism       : run() method overridden in TimedQuiz
  - Exception Handling : try/except in every file

========================================
NOTE
========================================
  Password is stored in plain text (no hashing).
  This is intentional for simplicity at CDAC module level.
========================================
