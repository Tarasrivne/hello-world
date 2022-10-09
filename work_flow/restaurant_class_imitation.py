class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        long_name = f" {self.restaurant_name}, {self.cuisine_type}"
        return long_name

    def set_number_served(self, served_tables):
        self.number_served = served_tables
        if served_tables > 8 and served_tables < 10:
            print('thr restaurant is half full')
        else:
            print("restaurant is empty")

    def increment_tables(self, tables):
        self.number_served += tables

    def display_served(self):
        print(f" this restaurant has reserved tables {self.number_served}")

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ()
        self.portion = 0
    def ice_cream_flavors(self, ice_cream, portion):
        self.flavors += ice_cream, portion
        self.portion += 8
        print(f"we have the following ice cream flavors {self.flavors} only {self.portion} portion ")



my_icecream = IceCreamStand('chocolate', 'cream',)
print(my_icecream.describe_restaurant())
my_icecream.ice_cream_flavors('cherry', 'watermelon')