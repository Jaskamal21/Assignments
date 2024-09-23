def add_names():
    names_set = set()

    while True:
        name = input("Enter a name (or press Enter to stop): ").strip()

        if name == "":
            break

        if name in names_set:
            print("Existing name")
        else:
            print("New name")
            names_set.add(name)

    print("\nNames entered:")
    for name in names_set:
        print(name)


add_names()
