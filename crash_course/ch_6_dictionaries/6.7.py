# Person

person1 = { 'first_name' : 'John', 'last_name' : 'Smith', 'age' : 20, \
'location' : 'California'}

person2 = { 'first_name' : 'Adam', 'last_name' : 'Wilson', 'age' : 63, \
'location' : 'New York'}

person3 = { 'first_name' : 'Alice', 'last_name' : 'Pringle', 'age' : 34, \
'location' : 'Missouri'}

people = [ person1, person2, person3 ]

for person in people:
    print ( f"Name : {person['first_name']} {person['last_name']}")
    print ( f"Age : {person['age']}")
    print ( f"Location : {person['location']}\n")
