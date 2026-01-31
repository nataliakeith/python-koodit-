import random

N = int(input("How many points?: "))
n = 0
generated_points = 0
while generated_points < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x*x + y*y < 1:
        n += 1

    generated_points += 1

pi = 4 * n / N
print(pi)


