def gallons(number):
    return number * 3.78541

volume = float(input("enter a volume in gallon: "))
conversion = 0
while volume >= 0:
    conversion = gallons(volume)
    print(conversion)
    volume = float(input("enter a volume in gallon: "))
