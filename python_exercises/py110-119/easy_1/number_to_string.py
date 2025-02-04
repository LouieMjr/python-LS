'''
In the previous two exercises, you developed functions that convert simple
numeric strings to signed integers. In this exercise and the next, you're going
to reverse those functions.

Write a function that converts a non-negative integer value (e.g., 0, 1, 2, 3,
and so on) to the string representation of that integer.

You may not use any of the standard conversion functions available in Python,
such as str. Your function should do this the old-fashioned way and construct
the string by analyzing and manipulating the number.


input: numbe
output: string representation of input number

Data structure:
dictionary
variable to store a string

Algo:
Declare a dictionary, keys will be numbers 0-9, values will be their string
equivalent
declare an empty string

check if input num is between 9999 and 1000
- step 1: use divmod on current num and pass in 1000 as divisor
- step 2: pass in first ele of tuple to obj and store results inside string
- step 3: store second ele of tuple to be passed in as next current number to
  recursive call and return
check if input num is between 999 and 100
- repeat steps 1-3
check if input num is between 99 and 0
- repeat steps 1-2
- return string

'''
def integer_to_string(number):

    num_strings = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    result = ''
    while number > 0:
        number, remainder = divmod(number, 10)
        result = num_strings[remainder] + result

    return result or '0'

    # if number == 0:
    #     return '0'
    # int_to_numstr = {
    #     0 : '0',
    #     1 : '1',
    #     2 : '2',
    #     3 : '3',
    #     4 : '4',
    #     5 : '5',
    #     6 : '6',
    #     7 : '7',
    #     8 : '8',
    #     9 : '9',
    # }
    #
    #
    # if number < 9999 and number >= 1000:
    #     quotient, remainder = divmod(number, 1000)
    #     num_string += int_to_numstr[quotient]
    #     if remainder == 0:
    #         num_string += '000' 
    #         return num_string
    #     return integer_to_string(remainder, num_string)
    #
    # if number < 999 and number >= 100:
    #     quotient, remainder = divmod(number, 100)
    #     num_string += int_to_numstr[quotient]
    #     if remainder == 0:
    #         num_string += '00'
    #         return num_string
    #     return integer_to_string(remainder, num_string)
    #
    # if number < 99 and number >= 0:
    #     quotient, remainder = divmod(number, 10)
    #     num_string += int_to_numstr[quotient]
    #     num_string += int_to_numstr[remainder]
    #     return num_string



print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True
