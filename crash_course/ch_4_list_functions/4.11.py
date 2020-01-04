# Pizzas

pizzas = ["cheese", "pepperoni", "veggie"]
friend_pizzas = pizzas[:]

pizzas.append("Four Cheese")
friend_pizzas.append("Meat Lovers")

print("The pizzas I like are:")
for pizza in pizzas:
    print("\t" + pizza)

print("\nThe pizzas my friend likes are:")
for pizza in friend_pizzas:
    print("\t" + pizza)
