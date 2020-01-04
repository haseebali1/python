# Users

from classes.user_login import *

user1 = User("John", "Smith", "jsmith", "10/23/1945")

user1.greet_user()
user1.describe_user()
print()

print ("Login attempts : " + str(user1.login_attempts))

user1.incrememt_login_attempts()
user1.incrememt_login_attempts()
user1.incrememt_login_attempts()
user1.incrememt_login_attempts()
user1.incrememt_login_attempts()

print ("Login attempts : " + str(user1.login_attempts))

user1.reset_login_attempts()

print ("Login attempts : " + str(user1.login_attempts))
