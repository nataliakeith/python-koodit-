import random
dice = int(input("how many dices to roll: "))
total = 0

for n in range(dice):
    roll = random.randint(1,6)
    total = total + roll
print(total)


