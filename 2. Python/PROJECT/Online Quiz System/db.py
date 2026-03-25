import mysql.connector

# this file handles all database related work

class Database:

    def __init__(self):
        try:
            temp = mysql.connector.connect(
                host="localhost",
                user="root",
                password="brucewayne"
            )
            tc = temp.cursor()
            tc.execute("CREATE DATABASE IF NOT EXISTS quiz_system")
            tc.close()
            temp.close()

            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="brucewayne",
                database="quiz_system"
            )
            self.cursor = self.conn.cursor()
            print("Database connected!")
            self.make_tables()

        except Exception as e:
            print("Database error:", e)
            self.conn = None
            self.cursor = None

    def make_tables(self):
        # create users table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) NOT NULL UNIQUE,
                email VARCHAR(100) NOT NULL UNIQUE,
                password VARCHAR(100) NOT NULL
            )
        """)

        # create results table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS results (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                username VARCHAR(50),
                score INT NOT NULL,
                total INT NOT NULL,
                topic VARCHAR(50),
                attempt_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)
        self.conn.commit()

    # add new user to database
    def add_user(self, username, email, password):
        sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (username, email, password))
        self.conn.commit()

    # save quiz result to database
    def save_result(self, user_id, username, score, total, topic):
        sql = "INSERT INTO results (user_id, username, score, total, topic) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (user_id, username, score, total, topic))
        self.conn.commit()

    # get user details by username
    def get_user(self, username):
        self.cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        return self.cursor.fetchone()

    # get all results of a user
    def get_results(self, user_id):
        self.cursor.execute("SELECT * FROM results WHERE user_id = %s ORDER BY attempt_date", (user_id,))
        return self.cursor.fetchall()

    # update password
    def update_password(self, user_id, new_password):
        self.cursor.execute("UPDATE users SET password = %s WHERE id = %s", (new_password, user_id))
        self.conn.commit()
        print("Password changed successfully!")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print("Database closed.")
