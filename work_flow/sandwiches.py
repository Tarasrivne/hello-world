sandwiches = ['king_sand', 'pop_sand', 'tiny_sand', 'family_sand']
order_sandwiches = []
while sandwiches:
    current_ofer = sandwiches.pop() #remove the last element of the list
    print(f"I made you {current_ofer}")
    order_sandwiches.append(current_ofer)# add to list
print("\nusers have been ordered")
for finish_sand in order_sandwiches:
    print(finish_sand)