# Addition Calculator

while True:
    num1 = input ("Enter a number : ")
    num2 = input ("Enter another number : ")

    try:
        answer = int(num1) + int(num2)
    except ValueError:
        print("Enter two numbers")
    else:
        print (answer)
