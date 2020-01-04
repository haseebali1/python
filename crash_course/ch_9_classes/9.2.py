# Restaurant

# in order to import from a subfolder need to touch a __init__.py file in that
# folder.

from classes.restaurant import *

restaurant1 = Restaurant("Yoshinoya", "Japanese")
restaurant2 = Restaurant("Del Taco", "Mexican")
restaurant3 = Restaurant("McDonalds", "Western")

restaurant1.describe_restaturant()
restaurant2.describe_restaturant()
restaurant3.describe_restaturant()
