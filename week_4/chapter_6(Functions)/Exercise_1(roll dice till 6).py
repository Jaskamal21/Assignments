import random

def dice_rolled():
    return random.randint(1,6)

def roll_till_6():
    roll = dice_rolled()
    while roll != 6:
        print(roll)
        roll = dice_rolled()
    print(roll)

roll_till_6()