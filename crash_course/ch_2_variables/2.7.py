# Stripping Names

#name with leading and trailing whitespaces
name = "\t\tBruceLee\t\n"

print(f"Name: {name}")
print(f"Name: {name.lstrip()}")
print(f"Name: {name.rstrip()}")
print(f"Name: {name.strip()}")
