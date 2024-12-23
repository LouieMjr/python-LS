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
        print(messages['invalid'])
        return get_number_from_user(called)

def get_operation_from_user():
    print(messages['operation'])
    operation = input(messages['choices'])
    print(operation)



def welcome_to_calculator():
    print(messages['welcome'])
    called = 1
    num1 = get_number_from_user(called)
    called += 1
    num2 = get_number_from_user(called)
    operation = get_operation_from_user()

welcome_to_calculator()
