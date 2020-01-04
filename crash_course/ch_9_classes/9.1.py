# Restaurant

# in order to import from a subfolder need to touch a __init__.py file in that
# folder.

from classes.restaurant import *

restaurant = Restaurant("Yoshinoya", "Japanese")

print ("Name : " + restaurant.restaurant_name)
print ("Cuisine Type : " + restaurant.cuisine_type)

restaurant.describe_restaturant()
restaurant.open_restaurant()
