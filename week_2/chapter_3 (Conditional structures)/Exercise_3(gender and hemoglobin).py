gender = input("Enter your gender ('male/female'): ").lower()
hemoglobin = float(input("Enter your hemoglobin(g/l): "))

if gender == "male":
    if hemoglobin < 134:
        print("Your hemoglobin is low")
    elif 134 <= hemoglobin <= 167 :
        print("Your hemoglobin is normal")
    elif hemoglobin > 167 :
        print("Your hemoglobin is high")
elif gender == "female":
    if hemoglobin < 117:
        print("Your hemoglobin is low")
    elif 117 <= hemoglobin <= 155 :
        print("Your hemoglobin is normal")
    else:
        print("Your hemoglobin is high")
else:
    print("Invalid gender or hemoglobin. Please enter either 'male' or 'female' and hemoglobin in 'g/l' format")