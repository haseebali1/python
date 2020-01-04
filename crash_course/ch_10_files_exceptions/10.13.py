# Verify User

import json

filename = 'files/user.json'

def get_stored_username():
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    try:
        username = input("Enter your username : ")
        with open(filename, 'w') as f:
            json.dump(username, f)
    except FileNotFoundError:
        pass
    else:
        return username

def greet_user():
    username = get_stored_username()

    if username:
        print("The current username that I have is " + username)
        correct_user = input("If this is correct enter y else enter no : ")
        if correct_user == "y":
            print("Welcome Back, " + username)
        else:
            username = get_new_username()
            print("We will remember you " + username)
    else:
        username = get_new_username()
        print("We will remember you " + username)

greet_user()
