# Divide by Zero exception

num1 = input ("Enter Number 1 : ")
num2 = input ("Enter Number 2 : ")

try:
    answer = int(num1) / int(num2)
except ZeroDivisionError:
    print ("you cant divide by zero!")
except ValueError:
    print ("Enter Two Numbers")
else:
    print (answer)
