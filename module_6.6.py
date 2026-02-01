def pizza(diameter, price):
    return price/(3.14 * (diameter/ 200)**2)

diameter = float(input("enter diameter of first pizza: "))
price = float(input("enter price of first pizza: "))
unit1 = pizza(diameter, price)

diameter = float(input("enter diameter of second pizza: "))
price = float(input("enter price of second pizza: "))
unit2 = pizza(diameter, price)

if unit1 < unit2:
    print("Pizza 1 has better price.")
elif unit2 < unit1:
    print("Pizza 2 has better price.")
else:
    print("Same value.")

