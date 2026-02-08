
airports = {}
print("To enter a new airport press: 1")
print("To fetch information of a existing airport press: 2")
print("If you wish to quit press: 3")

option = input("Choose a option: ")

while option != "3":
    if option == "1":
        icao = input("Enter ICAO code:")
        airport = input("Enter airport name: ")
        airports[icao] = airport
        print("Airport registered.")
    elif option == "2":
        fetch = input("Enter ICAO code: ")
        if fetch in airports:
            print("Airport name: ", airports[fetch])
        else:
            print("Invalid")
    elif option == "3":
        break
    option = input("Choose a option: ")



