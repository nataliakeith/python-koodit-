uneven = []
divisor = 2
def list_of_integers(numbers):
    for number in numbers:
        if number % divisor != 0:
            uneven.append(number)
    return numbers

numbers_list = [1, 2, 3, 4]
total = list_of_integers(numbers_list)
print(total, uneven)
