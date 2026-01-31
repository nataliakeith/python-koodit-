def remove_odd(numbers):
    even_numbers = []
    for n in numbers:
            if n % 2 == 0:
                even_numbers.append(n)
    return even_numbers
normal_list= [1,2,3,4]
filtered = remove_odd(normal_list)

print("Normal list: ", normal_list)
print("filtered list:", filtered)
