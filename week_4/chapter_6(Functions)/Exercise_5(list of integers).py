def remove_odd_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers

def list():
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even_list = remove_odd_numbers(original_list)

    print(f"Original list: {original_list}")
    print(f"List with only even numbers: {even_list}")

list()
