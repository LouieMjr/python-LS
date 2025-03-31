# Write a function that takes a string and returns a dictionary containing the
# following three properties:
#
#     the percentage of characters in the string that are lowercase letters
#     the percentage of characters that are uppercase letters
#     the percentage of characters that are neither
#
# All three percentages should be returned as strings whose numeric values lie
# between "0.00" and "100.00", respectively. Each value should be rounded to two
# decimal points.
#
# You may assume that the string will always contain at least one character.

# input: string
# output: dictionary with three properties

# three properties include:
# percentage for chars in string that are lowercase
# percentage for chars in string that are uppercase
# percentage for chars in string that are neither

# format for percentages values should be between "0.00" and "100.00"
# represented as strings and rounded to two decimal points

# helper function
# function that takes in a number and length of input string, divides that
# number by the length of the input string and returns that value in string form

# main function
# takes in a string
# declare an empty dict
# declare 3 variables - each initialized to 0. One to count uppercase chars,
# lowercase chars and chars that are neither
#
# iterate through the string
## check if the character is upper or lower case or neither
### increment one of the variables depending on what the current character is
# after iterating
# make three calls to the helper function
# store the results as the value to the repsective key in the dictionary
# keys will be
# lowercase: result of lowercase func call * 100 - formated to two decimal places
# uppercase: result of uppercase func call * 100 - formated to two decimal places
# neither: result of neither func call * 100 - formated to two decimal places


def divide_and_stringify(count, length_of_str):
    return f'{(count / length_of_str) * 100:.2f}'

def letter_percentages(string):
    string_details = {}

    lowercase_count = 0
    uppercase_count = 0
    neither = 0

    for char in string:
        if char.islower():
            lowercase_count += 1
        elif char.isupper():
            uppercase_count += 1
        else:
            neither += 1

    string_details['lowercase'] = divide_and_stringify(lowercase_count,
                                                       len(string))
    string_details['uppercase'] = divide_and_stringify(uppercase_count,
                                                       len(string))
    string_details['neither'] = divide_and_stringify(neither, len(string))

    return string_details

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)
