# Cars

def make_car (manufacturer, make, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['make'] = make
    return car_info

car = make_car("toyota", "camry", color = "blue", year = 2018, vin = "324dsdl",
        transmission = "automatic")

for key, value in car.items():
    print (key.title() + " : " + str(value).upper())
