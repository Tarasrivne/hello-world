filename = 'C:\\Users\\Admin777\\Desktop\\python\\text_by_python.txt'
with open(filename, 'a') as file_object:

    begin_ask = "\nWhat is your name:"
    begin_ask += "\n(Enter 'quit' when you are finished)"
    active = True
    while active:
        message = input(begin_ask)
        if message == 'quit':
            active = False
        else:
            print(f"Hello my friend {message}")
            file_object.write(message)