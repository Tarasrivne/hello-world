unconfirmed_cars = ['audi', 'bmw', 'acura', 'honda']
confirmed_cars = []
while unconfirmed_cars:
     cars_pop = unconfirmed_cars.pop()
     print(f"confirmed cars {cars_pop.title()}")
     confirmed_cars.append(cars_pop)
for verifed_cars in confirmed_cars:
    print(f"{verifed_cars} -- this car is verifed")
