def validate_pin(pin):
    if(type(pin) != str or len(pin) not in [4,6]):
        return (False)
    for num in pin:
        if num not in "0123456789":
            return (False)
    return (True)
my_pin = validate_pin('1234')
print(my_pin)



def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

my_pin = validate_pin('1234')
print(my_pin)

