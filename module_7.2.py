name = input("Enter a name: ")
names = set()

while name != "":
    names.add(name)
    name = input("Enter a name: ")
    if name == "":
        break
    if name in names:
        print("Existing name")
    else:
        print("New name")

for n in names:
        print(n)

