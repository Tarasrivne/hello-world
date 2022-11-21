def create_person(first_name, last_name, age=None):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease enter your name")
    print("(enter 'q' at any time to quite)")
    f_name = input("first_name:")
    if f_name == 'q':
        break
    l_name = input("last_name:")
    if l_name == 'q':
        break
    formated_person = create_person(f_name,l_name)
    print(f"hello {formated_person}")