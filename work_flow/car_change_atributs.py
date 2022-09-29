class Car:

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return  long_name.title()

    def odometers_miles(self):
        print(f"the vehicle have {self.odometer} miles")

    def update_odometer(self, miles):
        self.odometer = miles

my_new_car = Car (2013, 'chevrolet', 'volt')
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(182)
my_new_car.odometers_miles()
# my_new_car.odometer = 777
# my_new_car.odometers_miles()