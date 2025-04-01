# A featured number (something unique to this exercise) is an odd number that is
# a multiple of 7, with all of its digits occurring exactly once each. For
# example, 49 is a featured number, but 98 is not (it is not odd), 97 is not (it
# is not a multiple of 7), and 133 is not (the digit 3 appears twice).
#
# Write a function that takes an integer as an argument and returns the next
# featured number greater than the integer. Issue an error message if there is
# no next featured number.
#
#NOTE#: The largest possible featured number is 9876543201.


# input: integer
# output: first number that is greater than input that meets criteria

# featured number requirements:
## an odd number
## multiple of 7
## each digit in the number only occurs once

# algo:
# helper function-2, takes in number and input number
# check if remainder of number divided by 2 is 1
# if true,
# check if number is greater than input number
# if true, return number
# else return false

# helper function-1, takes in multiplier
# multiples 7 by multiplier
# return result

# main function, take in default parameter, multiplier, set to 1
# store result of helper function-1
# increment multiplier
# turn result into string form and get length using len method
# pass string form into set and get length of set using len method
# if lengths are equal
## return result of inovking helper function-2


def odd_multiple_of_7(number):
    number += 1
    while number % 2 == 0 or number % 7 != 0:
        number += 1

    return number

def unique_numbers(feat_num):
    str_num = str(feat_num)
    return len(str_num) == len(set(str_num))

def next_featured(num):
    featured_number = odd_multiple_of_7(num)

    while featured_number <= 9876543201:
        if unique_numbers(featured_number):
            return featured_number

        featured_number += 14

    return "There is no possible number that fulfills those requirements."

print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True
