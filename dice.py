from random import randint


class Die:
    def __init__(self):
        self.sides = int(input('Enter no of sides of die\t'))

    def roll_die(self):
        print(randint(1, self.sides))


call = Die()
call.roll_die()
