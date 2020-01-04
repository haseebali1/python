# Guest

filename = 'files/guest_list.txt'

while True:
    name = input("Enter your name. Enter quit to exit : ")
    print("Hello " + name.title() + "\n")

    if name == 'quit':
        break

    with open(filename, 'a') as file_object:
        file_object.write("Hello " + name.title() + "\n")

with open(filename) as file_object:
    for line in file_object.readlines():
        print ( line.rstrip() )
