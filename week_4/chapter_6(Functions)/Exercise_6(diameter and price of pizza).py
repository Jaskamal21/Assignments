import math

def pizza_unit_price(diameter, price):
    radius_m = (diameter / 2) / 100
    area_m2 = math.pi * (radius_m ** 2)
    unit_price = price / area_m2
    return unit_price


def value_for_money():
    diameter1 = float(input("Enter the diameter of the first pizza in centimeters: "))
    price1 = float(input("Enter the price of the first pizza in euros: "))

    diameter2 = float(input("Enter the diameter of the second pizza in centimeters: "))
    price2 = float(input("Enter the price of the second pizza in euros: "))

    unit_price1 = pizza_unit_price(diameter1, price1)
    unit_price2 = pizza_unit_price(diameter2, price2)

    print(f"Unit price of the first pizza: {unit_price1:.2f} €/m²")
    print(f"Unit price of the second pizza: {unit_price2:.2f} €/m²")

    if unit_price1 < unit_price2:
        print("The first pizza offers better value for money.")
    elif unit_price2 < unit_price1:
        print("The second pizza offers better value for money.")
    else:
        print("Both pizzas offer the same value for money.")

value_for_money()
