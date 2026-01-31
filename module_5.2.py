number = input("enter number: ")
numbers = []

while number != "":
    numbers.append(int(number))
    number = input("enter number:")

numbers.sort(reverse=True)
print(numbers[:5])











