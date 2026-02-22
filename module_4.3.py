number = input("enter the number: ")
smallest = int(number)
biggest = int(number)

while number != "":
    number = int(number)
    if number < smallest:
      smallest = number
    if number > biggest:
        biggest = number
    number = input("enter the number: ")

print(smallest, biggest)






