from math import *

character_name = "John"
character_age = 35
print("There once was a man named " + character_name + ",")
print("he was", character_age, "years old. ")
print("He really liked the name " + character_name)
print("but didn't like being {}.".format(character_age))


print(character_name.replace("o", "g"))
character_name.replace("o", "g") #does nothing
character_name.upper(); #does nothing
print (character_name)

# COMMON STRING FUNCTIONS
# character_name.title() capitalizes the first letter of each word
# character_name.lower() converts to lower
# character_name.upper() converts to upper
# character_name.islower() returns true if all char are lower else returns false
# character_name.isupper() returns true if all char are upper else returns false
# len(character_name) gives the length of the string
# character_name[0] gives the char at index
# character_name.replace("string to replace", "to replace with") replaces word or char
# character_name.index("char or word") finds the index at which the pattern matches the first time
#format strings- takes variables or text and combines them
    # fullname = f"{first_name} {last_name}"
    # message = f"Hello, {fullname.title()}!"
    #earlier than 3.5 use format
    # fullname ="{} {}".format(first_name, last_name)
# character_name.rstrip(); delete trailing whitespace
# character_name.lstrip(); delete leading whitespace
# character_name.strip() delete leading and trailing whitespace

my_num = 5
print (str(my_num + 6) + " is the number") # prints 11 is the number
print (floor(3.8))

#COMMON NUMERICAL FUNCTIONS
# str(my_num) prints the number as a string
# abs(my_num) absolute value of num
# pow(my_num , 2) my_num^2 pow
# max(num1, num2) returns the higher number
# min(num1, num2) returns the lower number
# round(num) rounds higher or lower depending on the decimal place
# floor(num) rounds down no matter what
# ceil(num) rounds up no matter what
# sqrt(num) returns the square root of a num
# 3**2 3^2 = 9
# huge_number=14_000_000_000 -> print(huge_number) >>> 14000000000

#GETTING INPUT FROM USER
#python inputs are string by default
#name = input("Enter your name: ")
#age = input("Enter your age: ")
#print("Hi " + name + "! You are " + age + " years old")
#
#num1=input("Enter a number: ")
#num2=input("Enter another number: ")
#result = float(num1) + float(num2)
#print(result)

# MAD LIB
#color=input("Enter a color: ")
#plural_noun=input("Enter a plural noun: ")
#celebrity=input("Enter a celebrity: ")
#
#print("Roses are " + color)
#print(plural_noun + " are blue")
#print("I love " + celebrity)

#LISTS -> arrays
lucky_numbers=[4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends[1] = "Mike"
print(friends)
# print(friends[1:]) print from index 1 till end
# print(friends[1:3]) print from index 1 excluding index 3
# print(friends[-1]) prints the last value in the list, -2 prints second last, and so on
# friends.append("Jack") adds jack to the end
# friends.insert(0,"Jack") adds jack at the 0 index, 0 can be any number
# del friends[0] deletes first element
# friends.pop() returns the value of the last element and deletes it
# friends.pop(0) returns the value of the first element and deletes it, can be any number
# friends.remove("Karen") finds the value in the list and deletes it
# friends.sort() sorts the list permanently
# friends.sort(reverse=True) sorts the list in reverse
# friends.sorted() temporarily sorts the list
# friends.reverse() reverses the order of the list, does not sort in reverse order. not permanent
# len(friends) size of friends how many items are in there
# friends.extends(lucky_numbers) joins lucky numbers to friends
# friends.clear() empties the list

for friend in friends:
    print(friend)

# TUPLES - immutable lists
# dimensions = (200,50)
# can access -> print (dimensions[0])
# can also do
# for dimension in dimensions:
#   print(dimension)
# can't do this -> dimension[0] = 500
# to change value have to change whole tuple variable
# dimensions = (200,50) -> dimensions = (300,250)
