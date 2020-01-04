# Changing Guest List

guest_list = [ "Charles", "Jackson", "Laurel", "Ashley", "Williams"]

message = "you are invited to my party on MM/DD/YYYY"

print( f"{guest_list[0]}, {message}")
print( f"{guest_list[1]}, {message}")
print( f"{guest_list[2]}, {message}")
print( f"{guest_list[3]}, {message}")
print( f"{guest_list[4]}, {message}")

guest_not_coming = "Jackson"
guest_list.remove(guest_not_coming)

print( f"\n{guest_not_coming}, can't make it\n")

guest_list.append("Bob")

print( f"{guest_list[0]}, {message}")
print( f"{guest_list[1]}, {message}")
print( f"{guest_list[2]}, {message}")
print( f"{guest_list[3]}, {message}")
print( f"{guest_list[4]}, {message}")
