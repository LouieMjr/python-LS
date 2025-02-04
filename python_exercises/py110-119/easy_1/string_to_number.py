'''
Write a function that takes a string of digits and returns the appropriate
number as an integer. You may not use any of the standard conversion functions
available in Python, such as int. Your function should calculate the result by
using the characters in the string.

For now, do not worry about leading + or - signs, nor should you worry about
invalid characters; assume all characters are numeric.

input: string of digits
output: returns the numbered string in integer form

rules:
cannot use any conversion functions, such as int
do not worry about leading + or - signs or any non digit characters

only numbers will be used in the string

Data strucure:
possibly a dictionary
variable to store growing number

Algo:
    create a dictionary of numbers in string form as key and the int
    equivalent as the value
    declare a variable, called str_to_num, to store a growing number, initialized to 0
    declare a variable, called multiplier, initiailzed to 1 - this number will be multipled by 10 on each iteration

    iterate through a reversed version of the string
        multiply, multiplier with value of current element passed into obj as key
        increase and update str_to_num with result above
        multiply, multiplier by 10


    return str_to_num

'''

def string_to_integer(num_str):
    str_to_num = 0
    multiplier = 1

    base10_values = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }

    for ele in num_str[::-1]:
        product = base10_values[ele] * multiplier
        str_to_num += product
        multiplier *= 10

    return str_to_num


print(string_to_integer("4321") == 4321)  # True 
print(string_to_integer("570") == 570)    # True

def hexadecimal_to_integer(num_str):
    str_to_num = 0
    power = 0
    base_16 = 16

    base16_values = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    }

    for ele in num_str[::-1].upper():
        product = base16_values[ele] * (base_16 ** power)
        str_to_num += product
        power += 1

    return str_to_num

print(hexadecimal_to_integer('4D9f') == 19871)  # True
