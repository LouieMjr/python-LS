'''
In the previous exercise, you developed a function that converts simple numeric
strings to integers. In this exercise, you're going to extend that function to
work with signed numbers.

Write a function that takes a string of digits and returns the appropriate
number as an integer. The string may have a leading + or - sign; if the first
character is a +, your function should return a positive number; if it is a -,
your function should return a negative number. If there is no sign, return a
positive number.

You may assume the string will always contain a valid number.

You may not use any of the standard conversion functions available in Python,
such as int. You may, however, use the string_to_integer function from the
previous exercise.


Algo:

check if first element starts with + or -
if element is -, 
returning negative results of invoking string_to_int func with sliced off first
element

if element is + 
return results of invoking func with sliced off first element 

otherwise
return results of invoking func with input string

'''

from string_to_number import string_to_integer

def string_to_signed_integer(num_string):
    sign = num_string[0]
    match sign:
        case '-':
            return -string_to_integer(num_string[1:])
        case '+':
            return string_to_integer(num_string[1:])
        case _:
            return string_to_integer(num_string)


print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True
