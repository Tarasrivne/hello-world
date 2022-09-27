class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def print_attributes(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def describe(self):
        print(f"The name of the restaurant is {self.restaurant_name} and the cuise type is {self.cuisine_type}")

    def is_open(self,hour):
        if hour > 9 and hour < 18:
            return True
        else:
            return False

taras_restaurant = Restaurant('Taras','Ukrainian')
print(f"restaurant name {taras_restaurant.restaurant_name}")
taras_restaurant.print_attributes()
taras_restaurant.describe()
print(taras_restaurant.is_open(9.30))
