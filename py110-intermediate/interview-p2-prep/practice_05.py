# Create a function that takes a string argument and returns the character that
# occurs most often in the string. If there are multiple characters with the
# same greatest frequency, return the one that appears first in the string. When
# counting characters, consider uppercase and lowercase versions to be the same.

'''
input: string
output: element of character that appears most in input string

if multiple characters have the same greatest frequency, return the one that appeard first
case insensitive

convert string to all lowercase characters
declare a max variable, set to 0
declare an index variable set to 0

iterate through string
    store count of current character
    check if count is greater than max
    if yes, 
        reassign max to current count
        store current index of character

return string at index

'''

def most_common_char(string):
    lowercase_string = string.lower()

    counts = {}
    max_count = 0
    result = None

    for char in lowercase_string:
        counts[char] = counts.get(char, 0) + 1

    for char in lowercase_string:
        if counts[char] > max_count:
            max_count = counts[char]
            result = char

    return result

print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')
