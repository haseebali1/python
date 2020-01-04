# Guest

filename = 'files/programming_poll.txt'

while True:
    reason = input("Enter the reason you like programming.\
Enter quit to exit : ")

    if reason == 'quit':
        break

    print(reason)

    with open(filename, 'a+') as file_object:
        file_object.write(reason + "\n")

with open(filename) as file_object:
    for line in file_object.readlines():
        print ( line.rstrip() )
