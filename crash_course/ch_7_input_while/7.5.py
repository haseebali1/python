# movie ticket

prompt = "How old are you? : "

age = ""
total = 0
toddler = 0
child = 0
adult = 0

while age != "quit":
    age = input(prompt)

    if age == "quit":
        break;
    elif int(age) < 3:
        print ("Your ticket is free")
        toddler += 1
    elif int(age) < 12:
        print ("Your ticket is $10")
        total += 10
        child += 1
    else:
        print ("Your ticket is $15")
        total += 15
        adult += 1

message = "\nThe ticket total for "

if toddler > 0:
    message += "\n" + str(toddler) + " toddler(s)"
if child > 0:
    message += "\n" + str(child) + " child(ren)"
if adult > 0:
    message += "\n" + str(adult) + " adult(s)"

message += " is $" + str(total)

print (message)

