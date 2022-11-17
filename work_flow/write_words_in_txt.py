

try:
    filename = 'C:\\Users\\Admin777\\Desktop\\python\\text_by_python.txt'
except FileNotFoundError:
    print(f"Sorry, the file {filename} dosn't exist")
else:
    with open(filename, 'w') as file_object:
        file_object.write("I leaning Python ")
