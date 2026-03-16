#Ex: Udemy online platform application:
# - class variable
# - constructors
# - 1 static method
# - multiple objects

class udemyPlatform:
    user = 0
    name = "Udemy"

    def __init__(self, username):
        self.name = username
        udemyPlatform.user += 1

    @classmethod
    def count(cls):
        print("Total users:",cls.user)

user1 = udemyPlatform("Alice")
user2 = udemyPlatform("Bob")
user3 = udemyPlatform("Charlie")
user4 = udemyPlatform("David")
user5 = udemyPlatform("Eve")
udemyPlatform.count()