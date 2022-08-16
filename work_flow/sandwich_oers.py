sandwich = ['dubl_send', 'chiburger', 'chiken_burg', 'german_big_burg']
sandwich_finish = []

while sandwich:
    reserch = sandwich.pop()
    print(f'you chose this sandwiches {reserch}')
    sandwich_finish.append(reserch)

print("\nthe customer chose are:")
for sandwich_fin in sandwich_finish:
    print(sandwich_fin.title())