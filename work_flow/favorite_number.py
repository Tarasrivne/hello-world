import json
def favorite_numb():
    filename = 'number.json'
    try:
        with open(filename) as f:
            user_numb = json.load(f)
    except FileNotFoundError:
        user_numb = input("What is your favorite number?")
        with open(filename, 'w') as f:
            json.dump(user_numb, f)
            print(f"I will remember your favorite number is  {user_numb}")
    else:
        print(f"Hi, your favorite number is {user_numb} is it right?")

favorite_numb()