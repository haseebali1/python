# Pizza Toppings

prompt = "\nPlease enter a pizza topping"
prompt += "\nEnter 'quit' to finish adding : "

topping = ""
while topping != 'quit':
    topping = input(prompt)

    if topping != 'quit':
        print ("Adding topping : " + topping)
