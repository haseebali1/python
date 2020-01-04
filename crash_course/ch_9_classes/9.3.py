# Users

from classes.user import *

user1 = User("John", "Smith", "jsmith", "10/23/1945")
user2 = User("Michael", "Jordan", "mjordan", "02/17/1963")
user3 = User("Courteney", "Cox", "ccox1964", "06/15/1964")

user1.greet_user()
user1.describe_user()
print()

user2.greet_user()
user2.describe_user()
print()

user3.greet_user()
user3.describe_user()
