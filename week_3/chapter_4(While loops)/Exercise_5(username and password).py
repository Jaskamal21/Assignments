username = "python"
password = "rules"

attempts = 0
max_attempts = 5

while attempts < max_attempts:
    write_username = input("Enter your username: ")
    write_password = input("Enter your password: ")

    if write_username == username and write_password == password:
        print(f"Welcome {username}")
        break

    else:
        attempts += 1
        print("enter username and password again")
        if attempts == max_attempts:
            print("Access Denied")


