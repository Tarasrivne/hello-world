def print_cars(unprinted_design, completed_models):
    while unprinted_design:
        curent_cars = unprinted_design.pop()
        print(f"show what printed {curent_cars}")
        completed_models.append(curent_cars)

def show_completed_cars(completed_models):
    print("/n the following models has been printed")
    for finish_cars in completed_models:
        print(finish_cars)

unprinted_design = ['ford_t1', 'mercedes_a150', 'bmw_3', 'mada_3']
completed_models = []

print_cars(unprinted_design, completed_models)
show_completed_cars(completed_models)


