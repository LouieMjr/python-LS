'''
In the previous exercise, you developed a function that converts non-negative
numbers to strings. In this exercise, you're going to extend that function by
adding the ability to represent negative numbers as well.

Write a function that takes an integer and converts it to a string
representation.

You may not use any of the standard conversion functions available in Python,
such as str. You may, however, use integer_to_string from the previous
exercise.


Algo:
check if the input number is greater than 0
return plus sign concated with return value of integer_to_string

check if the input number is equal 0
return integer_to_string

otherwise
return minus sign concated with return value of integer_to_string but passing
in absolute value of number to function

'''
from number_to_string import integer_to_string

def signed_integer_to_string(number):

    if number > 0:
        return '+' + integer_to_string(number)
    elif number == 0:
        return integer_to_string(number)
    else:
        return '-' + integer_to_string(abs(number))
        # could pass in -number instead of abs(number)


print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True
