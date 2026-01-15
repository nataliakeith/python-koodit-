talents = int(input("enter number of talents: "))
pounds = int(input("enter number of pounds: "))
lots = int(input("enter number of lots: "))

total_lots = talents * 20 * 32 + pounds  * 32 + lots
total_grams = total_lots * 13.3
kilograms = int(total_grams // 1000)
grams = total_grams % 1000
print(f"the weight is {kilograms} kilograms and {grams} grams")
