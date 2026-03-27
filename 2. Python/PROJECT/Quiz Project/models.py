# models.py demonstrates OOP: Class, Inheritance, Encapsulation, and Polymorphism

class User:
    """Base Class demonstrating Inheritance"""
    def __init__(self, user_id, name, username, email):
        self.user_id = user_id
        self.name = name
        self.username = username
        self.email = email
        
        # Encapsulation: Private variable
        self.__password = None 
        
    # Encapsulation: Getter and Setter
    def set_password(self, password):
        try:
            self.__password = password
        except Exception as e:
            print(f"Error setting password: {e}")
            
    def get_password(self):
        try:
            return self.__password
        except Exception as e:
            print(f"Error getting password: {e}")
            return None

    def display_info(self):
        # Polymorphism: Base class implementation
        try:
            print(f"User: {self.name} | Username: {self.username}")
        except Exception as e:
            print(f"Error displaying User details: {e}")


class QuizUser(User):
    """Child Class demonstrating Inheritance from User"""
    def __init__(self, user_id, name, username, email):
        # Using super() to call the parent class constructor
        try:
            super().__init__(user_id, name, username, email)
            self.total_quizzes_taken = 0
        except Exception as e:
            print(f"Error initializing QuizUser: {e}")
            
    def display_info(self):
        # Polymorphism: Child class overrides display_info
        try:
            print(f"Quiz Player: {self.name.upper()} | Email: {self.email} | ID: {self.user_id}")
        except Exception as e:
            print(f"Error displaying QuizUser details: {e}")
            
    # Let's use a Data Structure (Dictionary) parameter here to fulfill requirements
    def load_stats_from_dict(self, stats_dict):
        try:
            if "total_quizzes" in stats_dict:
                self.total_quizzes_taken = stats_dict["total_quizzes"]
        except Exception as e:
            print(f"Error parsing dictionary: {e}")
