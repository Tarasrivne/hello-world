responses = {}
flag = True
while flag:
    name = input('what is your name ')
    response = input('which car did you choose ')
    responses[name] = response

    repeat = input("do you want to continue choosing yes/no ")
    if repeat == 'no':
        flag = False
    elif repeat != 'yes':
        print("write corect")

print('\n----Results-----')
for k, v in responses.items():
    print(f"{k.title()} would like {v.title()}.")