# No Users

users_list = ["john", "mike", "sam", "admin", "bob", "carl"]
#users_list.clear()

if users_list:
    for user in users_list:
        if user == "admin":
#            print (f"Hello {user.title()}, would you like to see a status" +
#                    " report?")
            print (f"Hello {user.title()}, would you like to see a status \
report?")
        else:
            print (f"Hello {user.title()}, Thank you for logging in again.")
else:
    print("There are no users")
