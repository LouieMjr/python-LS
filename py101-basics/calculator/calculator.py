# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.


from os import system

def get_number_from_user(called):
    first_or_second = 'First' if called == 1 else 'Second'
    try:
        num = float(input(f'Enter the {first_or_second} number: '))
        return num
    except:
        system('clear')
        print('Not a valid input. Make sure input is a number!')
        return get_number_from_user(called)


def welcome_to_calculator():
    print('Welcome to Calculator')
    called = 1
    print(get_number_from_user(called))
    called += 1
    print(get_number_from_user(called))

welcome_to_calculator()
