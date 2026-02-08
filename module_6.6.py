def pizza(diameter,price):
    area = 3.14 * (diameter/200) ** 2
    return price / area

diameter1 = float(input("enter diameter of the first pizza: "))
price1 = float(input("Enter price of the first pizza: "))

diameter2 = float(input("enter diameter of the second pizza: "))
price2 = float(input("Enter price of the second pizza: "))

pizza1 = pizza(diameter1, price1)
pizza2 = pizza(diameter2,price2)
if pizza1 < pizza2:
    print("First pizza unit price is lower", pizza1)
elif pizza2 > pizza1:
    print("Second pizza unit price is lower: ", pizza2)