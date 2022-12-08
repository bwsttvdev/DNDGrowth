class Dice:
    def __init__(self):
        self.sides = 20
 
    def roll(self):
        import random
        number = random.randint(1, self.sides)
        return number
 
d20 = Dice()
print(d20.roll())
 
class D4(Dice):
    def __init__(self):
        self.sides = 4

d4 = D4()
print(d4.roll())
 
class D6(Dice):
    def __init__(self):
        self.sides = 6

d6 = D6()
print(d6.roll())
 
class D8(Dice):
    def __init__(self):
        self.sides = 8

d8 = D8()
print(d8.roll())
 
class D10(Dice):
    def __init__(self):
        self.sides = 10

d10 = D10()
print(d10.roll())
 
class D12(Dice):
    def __init__(self):
        self.sides = 12

d12 = D12()
print(d12.roll())
