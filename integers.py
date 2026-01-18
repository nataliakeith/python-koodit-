from math import prod

a =int(input("first integers: "))
b =int(input("second integers: "))
c =int(input("third integers: "))

sum = a + b + c
prod = a * b * c
average = sum / 3

print("sum is " + str(sum))
print("product is " + str(prod))
print("average is " + str(average))
