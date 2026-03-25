import mysql.connector
from mysql.connector import Error


class Database:

   def __init__(self):
    try:
        temp_conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="brucewayne"      
        )
        temp_cursor = temp_conn.cursor()
        temp_cursor.execute("CREATE DATABASE IF NOT EXISTS quiz_system")
        temp_cursor.close()
        temp_conn.close()

        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="brucewayne", 
            database="quiz_system"
        )
        self.cursor = self.conn.cursor()
        print("Database connected successfully!")
        self.create_tables()

    except Error as e:
        print(f"Error connecting to database: {e}")
        self.conn = None
        self.cursor = None

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id       INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50)  NOT NULL UNIQUE,
                email    VARCHAR(100) NOT NULL UNIQUE,
                password VARCHAR(100) NOT NULL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS results (
                id           INT AUTO_INCREMENT PRIMARY KEY,
                user_id      INT NOT NULL,
                username     VARCHAR(50),
                score        INT NOT NULL,
                total        INT NOT NULL,
                topic        VARCHAR(50),
                attempt_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)
        self.conn.commit()

    def add_user(self, username, email, password):
        query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (username, email, password))
        self.conn.commit()

    def save_result(self, user_id, username, score, total, topic):
        query = "INSERT INTO results (user_id, username, score, total, topic) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(query, (user_id, username, score, total, topic))
        self.conn.commit()

    def get_user_by_username(self, username):
        self.cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        return self.cursor.fetchone()

    def get_all_results(self, user_id):
        self.cursor.execute("SELECT * FROM results WHERE user_id = %s ORDER BY attempt_date", (user_id,))
        return self.cursor.fetchall()

    def get_all_users(self):
        self.cursor.execute("SELECT id, username, email FROM users")
        return self.cursor.fetchall()

    def update_password(self, user_id, new_password):
        query = "UPDATE users SET password = %s WHERE id = %s"
        self.cursor.execute(query, (new_password, user_id))
        self.conn.commit()
        print("Password updated successfully!")

    def delete_result(self, result_id):
        self.cursor.execute("DELETE FROM results WHERE id = %s", (result_id,))
        self.conn.commit()
        print(f"Result #{result_id} deleted.")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print("Database connection closed.")
