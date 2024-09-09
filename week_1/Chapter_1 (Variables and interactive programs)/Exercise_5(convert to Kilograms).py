lots_to_grams = 13.3
pounds_to_lots = 32
talents_to_pounds = 20
grams_in_kg = 1000

talents = float(input("Enter the number of talents: "))
pounds = float(input("Enter the number of pounds: "))
lots = float(input("Enter the number of lots: "))

total_lots = (talents * talents_to_pounds * pounds_to_lots) + (pounds * pounds_to_lots) + lots
total_grams = total_lots * lots_to_grams

kilograms = int(total_grams // grams_in_kg)
grams = total_grams % grams_in_kg

print(f"The equivalent mass is: {kilograms} kg and {grams:.2f} grams")
