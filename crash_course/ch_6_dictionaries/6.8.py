# Pets

pet1 = { 'name' : 'Sam', 'type' : 'Dog', 'owner' : 'Kate' }
pet2 = { 'name' : 'Slowey', 'type' : 'Turtle', 'owner' : 'Virginia' }
pet3 = { 'name' : 'Mittens', 'type' : 'Cat', 'owner' : 'Jack' }
pet4 = { 'name' : 'Bonnie', 'type' : 'Dog', 'owner' : 'Steve' }
pet5 = { 'name' : 'Gladis', 'type' : 'Bunny', 'owner' : 'Caroline' }

pets = [ pet1, pet2, pet3, pet4, pet5 ]

for pet in pets:
    print (f"Name : {pet['name']}")
    print (f"Type : {pet['type']}")
    print (f"Owner : {pet['owner']}\n")
