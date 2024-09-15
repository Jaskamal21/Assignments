numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    if user_input == "":
        break

    numbers.append(float(user_input))

numbers.sort(reverse=True)

print("The five greatest numbers are:")
for i in range(min(5, len(numbers))):
    print(numbers[i])
