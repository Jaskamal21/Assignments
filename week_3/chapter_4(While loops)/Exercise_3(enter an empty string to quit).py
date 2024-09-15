largest = None
smallest = None

while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    if user_input == "":
        break

    try:
        number = float(user_input)

        if smallest is None or number < smallest:
            smallest = number
        if largest is None or number > largest:
            largest = number

    except ValueError:
        print("Invalid input! Please enter a valid number.")

if smallest is not None and largest is not None:
    print(f"Smallest number: {smallest}")
    print(f"Largest number: {largest}")
else:
    print("No valid numbers were entered.")
