# favorite Number

import json

favorite_number = input("Enter your favorite number : ")

filename = 'files/favorite_number.json'
with open(filename, 'w') as f:
    json.dump(favorite_number, f)
