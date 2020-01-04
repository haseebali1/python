# favorite Number Remembered

import json

filename = 'files/favorite_number.json'

try:
    with open(filename) as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    favorite_number = input("Enter your favorite number : ")

    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
        print("We will remember your favorite number " + favorite_number)
else:
    print("I know your favorite number! It's " + favorite_number)
