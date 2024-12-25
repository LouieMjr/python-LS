# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.


from os import system
import json

with open('./calc_messages.json', 'r') as file:
    messages = json.load(file)

def get_number_from_user(called):
    first_or_second = 'First' if called == 1 else 'Second'
    try:
        num = float(input(f'Enter the {first_or_second} number: '))
        return num
    except:
        system('clear')
        print(messages['invalid_number'])
        return get_number_from_user(called)

def get_operation_from_user():
    print(messages['which_operation'])
    user_choice = input(messages['choices'])
    return valid_operation(user_choice)

def valid_operation(operation):
    options = ['a', 's', 'm', 'd']
    operation = operation.lower()[0]

    if operation in options:
        return operation

    system('clear')
    print(messages['invalid_operation'])
    return get_operation_from_user()

def perform_operation_on_numbers(num1, num2, operation):
    system('clear')
    options = {
        "a": ['+', lambda a, b : a + b],
        "s": ['-', lambda a, b : a - b],
        "m": ['x', lambda a, b : a * b],
        "d": ['÷', lambda a, b : a / b],
    }

    return f'{num1} {options[operation][0]} {num2} = {options[operation][1](num1, num2)}'

def clear_console_print_inputs(num1, num2 = None):
    system('clear')
    inputs = [num1, num2]

    if inputs[1] is None:
        print(f'You previously entered: {num1}')
    else:
        inputs[0] = str(inputs[0])
        inputs[1] = str(inputs[1])
        numbers = ' and '.join(inputs)
        print(f'You previously entered: {numbers}')

def restart_calculator(message):
    response = input(message).lower()
    
    if response == 'y' or response == 'yes':
        return welcome_to_calculator()
    elif response == 'n' or response == 'no':
        return messages['end_calculator']
    else:
        return restart_calculator(messages['invalid_restart'])


def welcome_to_calculator(message = None):
    print(message) if message is not None else system('clear')

    called = 1
    input_number1 = int(get_number_from_user(called))
    clear_console_print_inputs(input_number1)

    called += 1
    input_number2 = int(get_number_from_user(called))
    clear_console_print_inputs(input_number1, input_number2)

    user_choice = get_operation_from_user()
    print(perform_operation_on_numbers(input_number1, input_number2, user_choice))
    return restart_calculator(messages['restart'])

print(welcome_to_calculator(messages['welcome']))