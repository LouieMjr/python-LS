'''
Write a program that solicits six (6) numbers from the user and prints a message that describes whether the sixth number appears among the first five.


input: 6 numbers from the user
output: strings stating whether 6th input number appears within in the first 5

rules:
prompt user 6 times for 6 numbers, dont need to convert inputs to actually
numbers
return out a message stating whether the 6th inputed number appears within the
first 5


Q:
what should happen if a number is not entered?

Data structure:
Could use a list to store each input number

Algo:
Declare an empty list
Declare a current variable initialized to 0

iterate 6 times:
    each time, prompt user for number, convert input to a number, store result
    inside current variable
    append only first 5 results to empty list

Check if the current variables value exists in the populated list
if it is, return a string saying it exists in the first 5 numbers
otherwise return a string saying it does not exist in the first 5 numbers 

'''
def search_for_last_input():
    numbers = []
    current = 0

    for i in range(1, 7):
        current = input(f'Enter the {i} number: ')
        if i < 6:
            numbers.append(current)

    message = f'{current} is in {','.join(numbers)}' if current in numbers else f'{current} is not in {','.join(numbers)}'
    return message

print(search_for_last_input())

