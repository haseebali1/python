# Restaurant

# in order to import from a subfolder need to touch a __init__.py file in that
# folder.

from classes.restaurant_served import *

restaurant = Restaurant("Yoshinoya", "Japanese")

print ("Name : " + restaurant.restaurant_name)
print ("Cuisine Type : " + restaurant.cuisine_type)

restaurant.describe_restaturant()
restaurant.open_restaurant()
restaurant.set_number_served(180)
print ("number served : " + str(restaurant.number_served))

restaurant.increment_number_served(100)
print ("number served : " + str(restaurant.number_served))
