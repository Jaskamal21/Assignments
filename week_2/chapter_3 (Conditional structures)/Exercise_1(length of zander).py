size_limit = 42

zander_length = float(input("Enter your zander length in centimeters: "))
difference = size_limit - zander_length

if zander_length < size_limit:
    print(f"The length of zander is small. It is {difference:.2f}cm short to catch the fish")

else:
    print(f"The zander meets the size limit")
