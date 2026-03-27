import mysql.connector

def get_connection():
    try:
        con = mysql.connector.connect(
            host="localhost",
            database="quiz_system",
            user="root",
            password="brucewayne" # Change if needed
        )
        return con
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def create_tables():
    con = get_connection()
    if con is None:
        return
        
    cursor = con.cursor()
    
    # 1. Automatic table creation for 'users' with an email column
    # Notice we support full CRUD by setting up an auto-increment primary key
    users_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        username VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL,
        password VARCHAR(100) NOT NULL
    )
    """
    
    # 2. Automatic table creation for 'results'
    # Adding ON DELETE CASCADE so if a user is deleted, their results are too
    results_table_query = """
    CREATE TABLE IF NOT EXISTS results (
        id INT AUTO_INCREMENT PRIMARY KEY,
        fk INT,
        score INT,
        total INT,
        FOREIGN KEY (fk) REFERENCES users(id) ON DELETE CASCADE
    )
    """
    
    try:
        cursor.execute(users_table_query)
        cursor.execute(results_table_query)
        con.commit()
    except mysql.connector.Error as e:
        print(f"Database Initialization Error: {e}")
    finally:
        cursor.close()
        con.close()

# Call this immediately when db is imported to hit the "create table automatically" requirement
try:
    create_tables()
except Exception as e:
    print(f"Failed to auto-create tables: {e}")