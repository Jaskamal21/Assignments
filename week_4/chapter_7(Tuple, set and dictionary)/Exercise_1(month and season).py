seasons = ("Winter", "Spring", "Summer", "Autumn")

def get_season(month):
    if month in (12, 1, 2):
        return seasons[0]
    elif month in (3, 4, 5):
        return seasons[1]
    elif month in (6, 7, 8):
        return seasons[2]
    elif month in (9, 10, 11):
        return seasons[3]
    else:
        return None


def check_season():
    month = int(input("Enter the number of a month (1-12): "))

    season = get_season(month)

    if season:
        print(f"The season is {season}.")
    else:
        print("Invalid month. Please enter a number between 1 and 12.")


check_season()
