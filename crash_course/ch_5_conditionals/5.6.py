# Hello Admin

users_list = ["john", "mike", "sam", "admin", "bob", "carl"]

for user in users_list:
    if user == "admin":
        print (f"Hello {user.title()}, would you like to see a status report?")
    else:
        print (f"Hello {user.title()}, Thank you for logging in again.")
