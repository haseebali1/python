# Deli

sandwich_orders = [ "tuna", "meatball", "pastrami", "chicken" ]

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print ("I am making " + sandwich + " sandwich.")
    finished_sandwiches.append(sandwich)

for finished in finished_sandwiches:
    print ("Made sandwich : " + finished)
