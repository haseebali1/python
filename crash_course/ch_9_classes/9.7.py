# Users

from classes.user import *

user1 = User("John", "Smith", "jsmith", "10/23/1945")

user1.greet_user()
user1.describe_user()
print()

admin1 = Admin("I am", "Admin", "admin", "1/12/2000")
admin1.greet_user()
admin1.describe_user()
print()

print("Priveleges : ")
admin1.privileges.show_privileges()

