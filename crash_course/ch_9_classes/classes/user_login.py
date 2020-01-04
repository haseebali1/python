#User

class User:
    def __init__(self, first_name, last_name, username, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.birthday = birthday
        self.login_attempts = 0

    def describe_user(self):
        print (f"Name : {self.first_name} {self.last_name}")
        print (f"Username: {self.username}")
        print (f"Birthday : {self.birthday}")


    def greet_user(self):
        print (f"Welcome Back! {self.first_name}")

    def incrememt_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
