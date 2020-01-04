# Restaurant

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaturant(self):
        print (f"{self.restaurant_name} is a {self.cuisine_type} resturant")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open from 10 AM to 11 PM")

# Ice Cream Stand

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Vanilla", "Chocolate", "Cookies and Cream",
                "Rocky Road"]

    def display_flavors(self):
        for flavor in self.flavors:
            print("\t" + flavor)
