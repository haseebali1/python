# Cars

#import cars_modules
#import cars_modules as cm

#from cars_modules import make_car
#from cars_modules import make_car as mc

from cars_modules import *

car = make_car("toyota", "camry", color = "blue", year = 2018,
        vin = "324dsdl", transmission = "automatic")

for key, value in car.items():
    print (key.title() + " : " + str(value).upper())
