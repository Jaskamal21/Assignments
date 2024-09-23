def gallons_to_litres(gallons):
    litre = gallons * 3.78541
    return litre

def convert_gallons():
    while True:
        gallons = float(input("Enter gallons or enter negative value to: "))
        if gallons < 0:
            print("Program ends, you entered negative value")
            break

        litre = gallons_to_litres(gallons)
        print(f"Value of {gallons} gallons in litres is {litre:.2f}")
        break

convert_gallons()