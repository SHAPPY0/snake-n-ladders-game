import random

class Dice:
    def __init__(self, num):
        self.diceNum = num
        self.diceChoices = [n for n in range(1, (6 * self.diceNum) + 1)]

    def Roll(self):
        return random.choice(self.diceChoices)