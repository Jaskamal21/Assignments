year = int(input("Please enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("It's a 'leap year'")
else:
    print("It's a not 'leap year'")