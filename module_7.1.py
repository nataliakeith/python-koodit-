season = ("Winter", "Spring", "Summer", "Autumn")

number = int(input("Enter a month (1-12): "))

if number >= 3 and number <= 5:
    print(season[1])
elif number >= 6 and number <= 8:
    print(season[2])
elif number >= 9 and number <= 11:
    print(season[3])
else:
    print(season[0])



