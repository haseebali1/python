#User

class User:
    def __init__(self, first_name, last_name, username, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.birthday = birthday

    def describe_user(self):
        print (f"Name : {self.first_name} {self.last_name}")
        print (f"Username: {self.username}")
        print (f"Birthday : {self.birthday}")


    def greet_user(self):
        print (f"Welcome Back! {self.first_name}")

# privileges

class Privileges:
    def __init__(self, privileges = ["can delete user", "can add post",
        "can delete post"]):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print("\t" + privilege)
# Admin

class Admin(User):
    def __init__(self, first_name, last_name, username, birthday):
        super().__init__(first_name, last_name, username, birthday)
        self.privileges = Privileges()
