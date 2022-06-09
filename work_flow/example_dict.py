my_car = {'x_position': 0, 'y_position': 25, 'speed': 'rocket'}
print(f"Original position {my_car['x_position']}")
# The car move right
# calculate the amount of displacement based on the current speed
if my_car['speed'] == 'slow':
    x_increment = 1
elif my_car['speed'] == 'medium':
    x_increment = 2
else:
    # the car move fast
     x_increment = 3
# the new position is equal to the sum of the old position and the increase
my_car['x_position'] = my_car['x_position'] + x_increment

print(f"New position: {my_car['x_position']}")
