import random
sides = int(input("how many sides dice has: "))

def dice(sides):
    return random.randint(1, sides)
roll = 0
while roll!= sides:
    roll = dice(sides)
    print(roll)

