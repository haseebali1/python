# Deli

sandwich_orders = [ "pastrami", "tuna", "pastrami", "meatball", \
    "pastrami", "chicken" ]

finished_sandwiches = []

print("The deli has run out of pastrami sandwiches\n" )

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print ("I am making " + sandwich + " sandwich.")
    finished_sandwiches.append(sandwich)

print()

for finished in finished_sandwiches:
    print ("Made sandwich : " + finished)
