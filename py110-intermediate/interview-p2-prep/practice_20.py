'''
Implement a function that calculates the sum of numbers inside of a string.

You can expect that the string will include only positive numbers.
'''
'''
inputs: string
outputs: sum of numbers within string


rules:
string will include only positive numbers

Algo:
declare a variable digit, set to an empty string
declare a varaible result, set to an empty list

iterate through input string
    check if current element is a digit
        if true, add character to digit string

    check if curr element is not a digit 
    OR the current char is equal to the last element in the string

        if true, append digit string in int form to list
        reassign digit to empty string



return sum of list of numbers

'''

def sum_of_numbers(string):
    digit = ''
    result = []

    for i, char in enumerate(string):
        if char.isdigit():
            digit += char

        if not char.isdigit():

            if digit:
                digit = int(digit)
                result.append(digit)
                digit = ''
        else:
            digit = int(digit)
            if digit:
                result.append(digit)
            digit = ''

    print(result)
    return sum(result)

# print(sum_of_numbers("L12aun3ch Sch3oo451") == 469)

