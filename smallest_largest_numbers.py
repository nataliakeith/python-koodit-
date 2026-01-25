number = input("enter the number: ")
smallest = int(number)
biggest = int(number)
number = input("enter the number: ")
while number != "":
    number2 = int(number)
    if number2 < smallest:
      smallest = number2
    if number2 > biggest:
        biggest = number2
    number = input("enter the number: ")

print(smallest, biggest)






