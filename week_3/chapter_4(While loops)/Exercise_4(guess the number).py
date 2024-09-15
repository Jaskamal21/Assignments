import random

number_to_guess = random.randint(1,10)

while True:
    user_guess = int(input("Guess a number between 1 and 10: "))

    if user_guess < number_to_guess:
        print("Your guess is too low")
    elif user_guess > number_to_guess:
        print("Your guess is too high")
    else:
        print("You guessed correctly.")
        break