# Sandwiches

# Takes an arbitrary number of arguments, basically pointer array
def build_sandwich(*toppings):
    print ("\nThe toppings in your sandwhich are : " )
    for topping in toppings:
        print ( topping )

build_sandwich("bacon")
build_sandwich("bacon", "lettuce")
build_sandwich("bacon", "lettuce", "tomato")
