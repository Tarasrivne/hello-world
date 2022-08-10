favorite_places = {
    'Anton': ['corn_beecon', 'Mount', 'leak'],
    'Lana': ['wood', 'leak', 'central_park'],
    'Fedor': ['mount_hill','pool']
    }
for k, y in favorite_places.items():
    print(f"{k.title()} most like to go on weekends")
    for places in y:
        print(f"\t{places.title()}")


