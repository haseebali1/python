# Shrinking Guest List

guest_list = [ "Charles", "Jackson", "Laurel", "Ashley", "Williams"]

message = "you are invited to my party on MM/DD/YYYY"

guest_list.insert(0, "Michael")
guest_list.insert(3, "Adam")
guest_list.append("Karen")

print( "My new table did not arrive on time, I can only invite two people\n")

print( f"{guest_list.pop(0)}, I am sorry, but there is not enough room")
print( f"{guest_list.pop()}, I am sorry, but there is not enough room")
print( f"{guest_list.pop(0)}, I am sorry, but there is not enough room")
print( f"{guest_list.pop(3)}, I am sorry, but there is not enough room")
print( f"{guest_list.pop()}, I am sorry, but there is not enough room")
print( f"{guest_list.pop(1)}, I am sorry, but there is not enough room\n")
print( f"{guest_list[0]}, {message}")
print( f"{guest_list[1]}, {message}")

del guest_list[0]
del guest_list[0]

print()
print ( guest_list)
