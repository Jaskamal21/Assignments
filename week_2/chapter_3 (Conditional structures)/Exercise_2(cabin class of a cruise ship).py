LUX = 'upper-deck cabin with a balcony'
A = 'above the car deck, equipped with a window'
B = 'windowless above the car deck'
C = 'windowless below the car deck'

cabin_class = input("Enter a cabin class of cruise ship (LUX, A, B, C): ").upper()

if cabin_class == 'LUX':
    print(f"your cabin class is {LUX}")

elif cabin_class == 'A':
    print(f"your cabin class is {A}")

elif cabin_class == 'B':
    print(f"your cabin class is {B}")

elif cabin_class == 'C':
    print(f"your cabin class is {C}")

else:
    print('Invalid cabin class')


