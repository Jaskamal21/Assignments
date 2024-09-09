while True:
    value = float(input("Enter value in inches or enter negative value to exit : "))
    if value < 0:
        print("Negative value entered")
        break

    inch_to_cm = value * 2.54
    print(f"{value} is equal to {inch_to_cm:.2f}")