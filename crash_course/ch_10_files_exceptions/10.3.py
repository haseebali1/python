# Guest

name = input("Enter your name : ")
filename = 'files/guest.txt'

with open(filename, 'w') as file_object:
    file_object.write(name)

with open(filename) as file_object:
    for line in file_object.readlines():
        print ( line )
