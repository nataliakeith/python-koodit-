import random
number = random.randint(1, 10)
guess = int(input("Guess the number: "))

while guess != number:
    if guess < number:
        guess = int(input("too low, guess again: "))
    if guess > number:
        guess = int(input("too high, guess again: "))

print("correct")


