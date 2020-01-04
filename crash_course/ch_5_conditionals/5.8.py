# Checking Usernames

current_users = ["sam", "Jack", "JAMES", "apple", "eagle", "catlover"]

new_users = ["jack", "james", "Mike", "Freedom", "frank"]
#new_users = []

copy = [ user.lower() for user in current_users ]

if new_users:
    for users in new_users:
        if users.lower() in copy:
            print (f"{users}, is already taken. Please choose another")
        else:
            print (f"{users}, is available")
else:
    print ("No New Users")
