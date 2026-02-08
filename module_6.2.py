import random

def dice(sides):
    return random.randint(1,sides)

max_sides = int(input("enter number of sides of the dice: "))
rolls = 0
while rolls != max_sides:
    rolls = dice(max_sides)
    print(rolls)
