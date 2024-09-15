import random

num_of_rolls = int(input("How many dice to rolls? "))

total_sum = 0

for i in range(num_of_rolls):
    roll = random.randint(1,6)
    total_sum += roll

print(f"The total sum of dice roll is {total_sum}")
