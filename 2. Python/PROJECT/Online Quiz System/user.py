from validators import check_username, check_email, check_password

class User:

    def __init__(self, db):
        # db is private so outside code cannot access it directly
        self.__db = db
        self.username = None
        self.user_id = None
        self.logged_in = False

    def register(self):
        print("\n--- Register ---")
        try:
            uname = input("Enter username: ").strip()
            email = input("Enter email: ").strip()
            pwd = input("Enter password: ").strip()

            # validate all inputs first
            check_username(uname)
            check_email(email)
            check_password(pwd)

            # check if username already taken
            if self.__db.get_user(uname):
                print("Username already taken. Try another.")
                return False

            self.__db.add_user(uname, email, pwd)
            print("Account created! Please login now.")
            return True

        except ValueError as e:
            print("Error:", e)
            return False
        except Exception as e:
            print("Something went wrong:", e)
            return False

    def login(self):
        print("\n--- Login ---")
        try:
            uname = input("Username: ").strip()
            pwd = input("Password: ").strip()

            user = self.__db.get_user(uname)

            if user is None:
                print("Username not found. Please register first.")
                return False

            # user[3] is the password column
            if user[3] != pwd:
                print("Wrong password.")
                return False

            # store user details after successful login
            self.username = uname
            self.user_id = user[0]
            self.logged_in = True
            print("Login successful! Welcome", uname)
            return True

        except Exception as e:
            print("Login error:", e)
            return False

    def change_password(self):
        print("\n--- Change Password ---")
        try:
            new_pwd = input("Enter new password: ").strip()
            check_password(new_pwd)
            self.__db.update_password(self.user_id, new_pwd)
        except ValueError as e:
            print("Error:", e)

    def logout(self):
        self.username = None
        self.user_id = None
        self.logged_in = False
        print("Logged out.")
