# Restaurant

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaturant(self):
        print (f"{self.restaurant_name} is a {self.cuisine_type} resturant")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open from 10 AM to 11 PM")

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, served):
        self.number_served += served
