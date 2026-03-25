from validators import validate_username, validate_email, validate_password


class User:

    def __init__(self, db):
        self.__db = db
        self.username = None
        self.user_id  = None
        self.is_logged_in = False

    def register(self):
        print("\n" + "=" * 40)
        print("          CREATE ACCOUNT")
        print("=" * 40)

        try:
            username = input("Enter username : ").strip()
            email    = input("Enter email    : ").strip()
            password = input("Enter password : ").strip()

            validate_username(username)
            validate_email(email)
            validate_password(password)

            existing = self.__db.get_user_by_username(username)
            if existing:
                print("This username is already taken. Try a different one.")
                return False

            self.__db.add_user(username, email, password)
            print(f"\nAccount created! Welcome {username}. Please login now.")
            return True

        except ValueError as e:
            print(f"Validation Error: {e}")
            return False
        except Exception as e:
            print(f"Something went wrong: {e}")
            return False

    def login(self):
        print("\n" + "=" * 40)
        print("              LOGIN")
        print("=" * 40)

        try:
            username = input("Username : ").strip()
            password = input("Password : ").strip()

            user = self.__db.get_user_by_username(username)

            if not user:
                print("Username not found. Please register first.")
                return False

            if user[3] != password:
                print("Wrong password. Please try again.")
                return False

            self.username     = username
            self.user_id      = user[0]
            self.is_logged_in = True

            print(f"\nLogin successful! Welcome back, {username} :)")
            return True

        except Exception as e:
            print(f"Login error: {e}")
            return False

    def change_password(self):
        print("\n-- Change Password --")
        try:
            new_pass = input("Enter new password : ").strip()
            validate_password(new_pass)
            self.__db.update_password(self.user_id, new_pass)
        except ValueError as e:
            print(f"Error: {e}")

    def logout(self):
        self.username     = None
        self.user_id      = None
        self.is_logged_in = False
        print("You have been logged out.")
