'''
Write a function that takes a string argument and returns a list of substrings
of that string. Each substring should begin with the first letter of the word,
and the list should be ordered from shortest to longest.
'''

'''
inputs: string
output: list of substrings from input

rules:
each substring should begin with the first letter of input string

Data structure:
list

Algo:
declare an empty list
iterate through len of string

        starting with the first index, add slice of string and push just that
        slice to list
        increase index, then push larger slice to list, so on and so forth
'''

def leading_substrings(string):
    return [string[:i] for i in range(1, len(string) + 1)]


# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])
