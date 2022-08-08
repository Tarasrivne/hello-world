people = {
    'person_1': {
        'first_name': 'Alex',
        'last_name': 'bure',
        'age': '32',
        'city': 'new york'},

    'person_2': {
        'first_name': 'don',
        'last_name': 'digidon ',
        'age': '23',
        'city': 'new jersey'},

    'person_3' : {git
        'first_name': 'klava',
        'last_name': 'koka',
        'age': '29',
        'city': 'muhosransk'}
}
for username, whole_name in people.items():
    print(f"\n Acaunt: {username}")
    full_name = f"{whole_name['first_name']} {whole_name['last_name']}"
    age_person = whole_name['age']
    location = whole_name['city']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tAge: {age_person}")
    print(f"\tCity: {location.title()}")
