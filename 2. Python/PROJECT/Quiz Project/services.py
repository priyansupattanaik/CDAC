from db import get_connection
from validators import validate_username, validate_email, validate_password
from models import QuizUser

# Create (C in CRUD)
def register():
    try:
        # Get details from user
        name = input("Enter Name: ")
        username = input("Enter Username (3-20 chars alphanumeric): ")
        email = input("Enter Email: ")
        password = input("Enter password: ")
        
        # Validation using Regular Expressions
        if not validate_username(username):
            print("Invalid Username format.")
            return
        if not validate_email(email):
            print("Invalid Email format.")
            return
        if not validate_password(password):
            print("Invalid Password format.")
            return

        con = get_connection()
        if con is None: return
        
        cursor = con.cursor()
        query = "INSERT INTO users(name, username, email, password) VALUES(%s, %s, %s, %s)"
        
        cursor.execute(query, (name, username, email, password))
        con.commit()
        print("\n=== Registered Successfully! ===")
        
    except Exception as e:
        print(f"Error while registering: {e}")
    finally:
        try:
            cursor.close()
            con.close()
        except: pass

# Read (R in CRUD)
def login():
    try:
        username = input("Enter Username: ")
        password = input("Enter password: ")

        con = get_connection()
        if con is None: return None
            
        cursor = con.cursor()
        query = "SELECT id, name, username, email FROM users WHERE username = %s AND password = %s"
        
        cursor.execute(query, (username, password))
        user_row = cursor.fetchone() 
        
        if user_row:
            user_id, name, db_username, email = user_row
            
            # Using OOP Concept: Class instantiation
            logged_in_user = QuizUser(user_id, name, db_username, email)
            # Using Encapsulation
            logged_in_user.set_password(password) 
            
            print(f"\n+++ Login Successful! +++")
            return logged_in_user
        else:
            print("\nInvalid Details. Try again.")
            return None
            
    except Exception as e:
        print(f"Error while logging in: {e}")
        return None
    finally:
        try:
            cursor.close()
            con.close()
        except: pass

# Read Data (R in CRUD)
def get_user_data(user_id):
    try:
        con = get_connection()
        if con is None: return None
            
        cursor = con.cursor()
        # Fixed query to match live schema which uses 'user_id' instead of 'fk'
        query = "SELECT u.name, r.score, r.total FROM results r JOIN users u ON r.user_id = u.id WHERE u.id = %s"
        
        cursor.execute(query, (user_id,))
        records = cursor.fetchall()
        return records
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
    finally:
        try:
            cursor.close()
            con.close()
        except: pass

# Implement Update (U in CRUD) - Change Password
def update_password(user_obj):
    try:
        new_password = input("Enter new password: ")
        if not validate_password(new_password):
            print("Invalid Password format.")
            return
            
        con = get_connection()
        if con is None: return
        
        cursor = con.cursor()
        query = "UPDATE users SET password = %s WHERE id = %s"
        cursor.execute(query, (new_password, user_obj.user_id))
        con.commit()
        
        user_obj.set_password(new_password)
        print("-> Password Successfully Updated!")
        
    except Exception as e:
        print(f"Error updating password: {e}")
    finally:
        try:
            cursor.close()
            con.close()
        except: pass

# Implement Delete (D in CRUD) - Delete Account
def delete_account(user_id):
    try:
        confirm = input("Are you SURE you want to delete your account? (yes/no): ")
        if confirm.lower() == 'yes':
            con = get_connection()
            if con is None: return False
            
            cursor = con.cursor()
            # Manually delete results first to avoid foreign key constraint errors
            cursor.execute("DELETE FROM results WHERE user_id = %s", (user_id,))
            # Then delete the user
            cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
            con.commit()
            print("-> Account and all associated data Deleted FOREVER.")
            return True
        else:
            print("-> Account deletion cancelled.")
            return False
            
    except Exception as e:
        print(f"Error deleting account: {e}")
        return False
    finally:
        try:
            cursor.close()
            con.close()
        except: pass

# Save Quiz Results (Create in Results Table)
def save_result(user_id, score, total):
    try:
        con = get_connection()
        if con is None: return
            
        cursor = con.cursor()
        # Fixed query to match live schema which uses 'user_id' instead of 'fk'
        query = "INSERT INTO results(user_id, score, total) VALUES(%s, %s, %s)"
        
        cursor.execute(query, (user_id, score, total))
        con.commit()
        print("-> Result Saved to Database Successfully.")
    except Exception as e:
        print(f"Error saving result: {e}")
    finally:
        try:
            cursor.close()
            con.close()
        except: pass
