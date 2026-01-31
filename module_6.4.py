def list_of_integers(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total
numbers = [1, 2, 3]
result = list_of_integers(numbers)
print(result)

