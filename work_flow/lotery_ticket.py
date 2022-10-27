import random
from random import choices, randint

class Die():
    """
    Randomly chooses 4 winning numbers
    """


    def __init__(self, sides=6):
        self.sides = sides
        self.lottery_ticket = ['3','5','8','34','12','6','9','f','s','t','a','7','l']


    def lottery(self):
        # vin_comb = choice(self.lottery_ticket)
        vin_combs = random.choices(self.lottery_ticket, k=4)
        print(f"Your win number is {vin_combs}")

    def roll_metod(self):
        self.sides = randint(1,20)
        return self.sides


my_kub = Die(6)
print(my_kub.roll_metod())

my_kub = Die()
print(my_kub.roll_metod())
my_kub.lottery()
