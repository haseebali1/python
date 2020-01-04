# Learning Python

filename = 'files/learning_python.txt'

print("Reading all the contenets and then printing")
with open(filename) as file_object:
    contents = file_object.read()

print(contents.replace('Python', 'C').rstrip())

print("\nReading all the content line by line, and then printing them")
with open(filename) as file_object:
    for line in file_object:
        print(line.replace('Python','C').rstrip())

print("\nStoring the lines in a list and then printing them")
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.replace('Python', 'C').rstrip())


