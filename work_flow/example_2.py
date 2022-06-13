favorite_languages = {
    'first_name': 'Nick',
    'last_name': 'Luck ',
    'age': '32',
    'city': 'new york',
   }
language = favorite_languages.get('Nick', 'this name is missing')
print(f" 1Th name {language}.")
print(favorite_languages['last_name'].title())
print(favorite_languages['city'].title())
