#Dream Vacation

vacations = {}

polling = True

while polling:
    name = input("\nWhat is your name? ")
    place = input("If you could visit one place in the world, where would you"
            + " go? ")

    vacations[name] = place

    repeat = input("Would another person like to add the dream vacation? ")

    if repeat == 'no':
        polling = False

print()
for name in vacations:
    print (name.title() + " Would like to visit " + vacations[name].title() +
            ".")
