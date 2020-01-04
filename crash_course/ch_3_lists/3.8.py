# Seeing the World

places_to_visit = ["London", "Japan", "Saudia Arabia", "Iraq", "France"]

print("Original List: ")
print(places_to_visit)

print("\nList sorted only for ouput")
print(sorted(places_to_visit))

print("\nList is still in original order")
print(places_to_visit)

print("\nList temporarily sorted in reverse for output")
print(sorted(places_to_visit, reverse=True))

print("\nList is still in original order")
print(places_to_visit)

places_to_visit.reverse()

print("\nList is in reverse order from original list")
print(places_to_visit)

places_to_visit.reverse()

print("\nList is in original order after reverse again")
print(places_to_visit)

places_to_visit.sort()

print("\nList is now permanently sorted")
print(places_to_visit)

places_to_visit.sort(reverse=True)

print("\nList is now permanently sorted in reverse")
print(places_to_visit)
