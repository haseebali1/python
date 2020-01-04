# Battery Upgrade

from classes.car import ElectricCar

mytesla = ElectricCar("tesla", "model s", 2019)

print (mytesla.get_descriptive_name())

mytesla.read_odometer()

mytesla.update_odometer(311)

mytesla.read_odometer()

mytesla.increment_odometer(5000)
mytesla.read_odometer()

mytesla.battery.describe_battery()
mytesla.battery.get_range()

mytesla.battery.upgrade_battery()

mytesla.battery.describe_battery()
mytesla.battery.get_range()

mytesla.battery.upgrade_battery()
