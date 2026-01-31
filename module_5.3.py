number = int(input("Enter a number: "))
prime = True

for n in range(2,number):
    if number % n == 0:
        prime = False
        break
if prime:
    print("prime")
else:
    print("not prime")




