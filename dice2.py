from random import randint


class Dice2:
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        for i in range(1, 11):
            print(randint(1, self.sides))

    def new_die(self, side):
        self.sides = side
        call.roll_die()


call = Dice2()
call.roll_die()
call.new_die(10)
call.new_die(20)
