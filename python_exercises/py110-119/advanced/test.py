import re

def invalid_input(input):
    # pattern = r'[^\d\s]'
    # if re.search(pattern, input) or input == '':
        # return True

    only_numbers = ''.join(input.split()).isdigit()

    if only_numbers:
        return False
    else:
        return True

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (list): A list of numbers

    Returns:
        float: The average of the numbers
    """
    total = 0
    for num in numbers:
        total += num

    average = total / len(numbers)
    return average

def main():
    # Get user input
    print("Enter numbers separated by spaces:")
    user_input = input()

    if invalid_input(user_input):
        print('Not a valid input. Please follow instructions.')
        return main()

    # Convert input to list of numbers
    numbers = []
    for num in user_input.split():
        numbers.append(int(num))

    # Calculate and display the average
    result = calculate_average(numbers)
    print(f"The average is: {result}")

if __name__ == "__main__":
    main()
