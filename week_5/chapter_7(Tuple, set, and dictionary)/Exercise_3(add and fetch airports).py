airport_collection= {}

def add_airports():
    ICAO = input("Enter ICAO code: ").upper()
    name = input("Enter airport name: ")
    airport_collection[ICAO] = name
    print(f'{name} added with ICAO code: {ICAO}\n')

def fetch_airports():
    ICAO = input("Enter ICAO code: ").upper()
    if ICAO in airport_collection:
        print(f'ICAO code: {ICAO}'),
        print(f'Airport name: {airport_collection[ICAO]}\n')
    else:
        print(f'No match found for ICAO code: {ICAO}\n')

def add_or_fetch_airports():
    while True:
        print("1. Add airport")
        print("2. Fetch airports")
        print("3. Exit")
        choose = int(input("Enter your choice(1,2,3): "))

        if choose == 1:
            add_airports()
        elif choose == 2:
            fetch_airports()
        elif choose == 3:
            print(f"Thank you!, for visiting")
            break
        else:
            print(f"Invalid choice")

add_or_fetch_airports()
