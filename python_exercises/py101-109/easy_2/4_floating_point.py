# Write a program that prompts the user for two positive numbers (floating-point), then prints the results of the following operations on those two numbers: addition, subtraction, product, quotient, floor quotient, remainder, and power. Do not worry about validating the input.

def results_of_operations():
    num_1 = float(input('Enter the first number: '))
    num_2 = float(input('Enter the second number: '))

    print(f'{num_1} + {num_2} = {num_1 + num_2}')
    print(f'{num_1} - {num_2} = {num_1 - num_2}')
    print(f'{num_1} * {num_2} = {num_1 * num_2}')
    print(f'{num_1} / {num_2} = {num_1 / num_2}')
    print(f'{num_1} // {num_2} = {num_1 // num_2}')
    print(f'{num_1} % {num_2} = {num_1 % num_2}')
    print(f'{num_1} ** {num_2} = {num_1 ** num_2}')

results_of_operations()