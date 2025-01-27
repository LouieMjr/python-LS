"""
PROBLEM:

Given a string, write a function `change_me` which returns the same
string but with all the words in it that are palindromes uppercased.

"""
# split string into array of words
# declare an empty string
# iterate through array
# invoke palindrome func,
    # if true, uppercase curr string, & add it to empty string
    # else, add curr string it to empty string


# inputs string
# check if 1st element is not equal to last element
# if true, return false
# else return substring

def is_palindrome(strr):
    if len(strr) <= 1:
        return True
    if strr[0] != strr[-1]:
        return False
    return is_palindrome(strr[1:-1])


def change_me(string):
    list_of_words = string.split()
    newstr = ''
    for ele in list_of_words:
        if(is_palindrome(ele)):
            newstr += ele.upper()
        else:
            newstr += ele
        newstr += ' '

    return newstr

# Comments show expected return values
# print(change_me("We will meet at noon"))       # "We will meet at NOON"
# print(change_me("No palindromes here"))       # "No palindromes here"
# print(change_me(""))                           # ""
# print(change_me("I LOVE mom and dad equally")) # "I LOVE MOM and DAD equally"


"""
PROBLEM:

Given a string, write a function `palindrome_substrings` which returns
all the palindromic substrings of the string that are 2 or more characters
long. Palindrome detection
should be case-sensitive.
"""
# input: string
# output: list of strings that are 2 or more characters long 
# ex:
# a palindrome is a word spelled the same in reverse
# based on test cases, its case sensitive
# return empty list if no palindromes exist
# 
#
# algorithm:
# declare an empty list
# iterate through string
# start j at i + 1
# inner loop, length of string minus i
# start slice at what i is currently, end slice at j
# pass slice into palindrome function, if true,
# append substring to list
# return list


def palindrome_substrings(string):
    subs = []
    for i in range(len(string) - 1):
        j = i + 2
        while j <=len(string) - i:
            slice = string[i:j]
            if is_palindrome(slice):
                subs.append(slice)
            j += 1
    return subs


# Test cases:
# Comments show expected return values
# print(palindrome_substrings("abcddcbA"))   # ["bcddcb", "cddc", "dd"]
# palindrome_substrings("palindrome") # []
# palindrome_substrings("")           # []
# palindrome_substrings("repaper")    # ['repaper', 'epape', 'pap']
# palindrome_substrings("supercalifragilisticexpialidocious") # ["ili"]

def sum_even_number_row(row_number):
    rows = []
    start_integer = 2
 
    for row_length in range(1, row_number + 1):
        row = create_row(start_integer, row_length)
        rows.append(row)
        start_integer = rows[-1][-1] + 2

    return rows


def create_row(start_int, row_length):
    row = []
    current_int = start_int

    while len(row) < row_length:
        row.append(current_int)
        current_int += 2

    return row


# print(sum_even_number_row(3)) # 30




""" Write a program that, given the number of available blocks, calculates the
number of blocks left over after building the tallest possible valid structure.

inputs:  unknown number of building blocks 
outputs: a number, for left over blocks after building tallest possible
structure

requirements:
- structure is built in layers using blocks
- blocks are cubes
- the top layer is a single block
- a block in an upper layer must be supported by four blocks in a lower layer
- a block in a lower layer can support more than one block in an upper layer
- no gaps between blocks
- 
- questions:
- What does it mean when it says a block in an upper layer must be supported by
  four blocks in a lower layer? Where does the upper block, need to be placed
  on the 4 lower blocks?
-
-
-
- test cases:
print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True

- Notes about test cases:
- seems like you cant have extra blocks in a lower layer. Each block in an
  upper layer must be supported by 4 blocks in a lower layer, no more, no less
- Any blocks left over are extra blocks
- 
- Data Structures you could use:
- a counter variable or nested arrays to represent the a valid structure
-
- Algorithm:
- input: is a number used to build as big of a valid structure as possible
- each layer of the strucure seems to be as big as a number squared

- SET a counter to 1
- SET a count to 0, to count left-over blocks

- iterate WHILE input number is positive
- STARTING from counter, multiply itself and subtract from the current state of input number
- STORE the results of the subtraction

- IF current state of input number is negative, return left-over blocks
  variable
- else, input number is still positive, this means you have enough blocks to build
  the current layer, increment counter by 1, move on to try and build the next layer in
"""



def calculate_leftover_blocks(blocks):
    if blocks == 0: return 0

    remaining_blocks = blocks
    current_layer = 1
    blocks_needed_for_layer = current_layer

    while remaining_blocks >= blocks_needed_for_layer:
        remaining_blocks -= blocks_needed_for_layer
        current_layer += 1
        blocks_needed_for_layer = current_layer ** 2


    return remaining_blocks



# print(calculate_leftover_blocks(0) == 0)  # True
# print(calculate_leftover_blocks(1) == 0)  # True
# print(calculate_leftover_blocks(2) == 1)  # True
# print(calculate_leftover_blocks(4) == 3)  # True
# print(calculate_leftover_blocks(5) == 0)  # True
# print(calculate_leftover_blocks(6) == 1)  # True
# print(calculate_leftover_blocks(14) == 0) # True





'''

# Sort Strings by Most Adjacent Consonants

Given a list of strings, sort the list based on the highest number of adjacent
consonants a string contains and return the sorted list. If two strings contain
the same highest number of adjacent consonants, they should retain their
original order in relation to each other. Consonants are considered adjacent if
they are next to each other in the same word or if there is a space between two
consonants in adjacent words.



input: list of strings
output: sorted list based on highest number of adjacent consonants a string
contains, if two strings contain the same amount, retain their order

rules:
- list is sorted starting with the highest number of adjacent consonants a string
contains first
- if two strings contain the same amount of consonants, retain their order
- consonants are considered adjacent if they are next to each other in the same
  word OR if there is a space between two consonants in adjacent words


- strings may contain more than one word



my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
['xxxx', 'xxxb', 'xxxa']

- new implicit rules after looking at test cases:

- strings may contain single or multiple words
- strings may not be empty
- strings may have no adjacent consonants
- strings should be sorted in descending orders
- case is not relevant
- if a string just has a single consonant, that does not affect the sort order
  in comparison to strings with no consonants.


DATA STRUCTURE TO USE:
- we have to return a list of strings
- Potentially use a dictionary to count the number of adjacent consonants in
  each string


Algorithm:

Take list of strings as input
SET a count variable to 0
SET a dict to empty
iterate through list
    use helper function
    helper function takes in string as input
        iterate through string
            check if current character is not a vowel
            if true, increment count variable
            otherwise, reset count to 0

        if count variable is 1, reset count to 0
        return count

    store current string as key, and count as value
'''

def count_max_adjacent_consonants(string):
    tmp_count = 0
    max_count = 0
    vowels = 'aeiou'
    string = string.replace(" ", "")

    for char in string:
        if char not in vowels:
            tmp_count += 1
            if tmp_count > 1:
                max_count = max(max_count, tmp_count)
        else:
            # if tmp_count > 1 and tmp_count > max_count:
                # max_count = tmp_count
            tmp_count = 0

    # if tmp_count > max_count:
        # max_count = tmp_count

    return max_count

print(count_max_adjacent_consonants('dddaa'))       # 3
print(count_max_adjacent_consonants('ccaa'))        # 2
print(count_max_adjacent_consonants('baa'))         # 0
print(count_max_adjacent_consonants('aa'))          # 0
print(count_max_adjacent_consonants('rstafgdjeccccccc')) # 4

def sort_by_consonant_count(lst_of_strings):
    count = count_max_adjacent_consonants
    lst_of_strings.sort(key=count, reverse=True)
    return lst_of_strings



my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']
#
my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']
#
my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']
#
my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']
#
my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']






































































"""
We're receiving a set of messages in code. The messages are sets of text strings, like:
"alakwnwenvocxzZjsf"
Write a method to decode these strings into numbers. The decoded number should be the number of lowercase characters between the first two uppercase characters. If there aren't two uppercase characters, the number should be 0.


input: a list of strings, could be an empty list
output: returning a list

explicit:
-working with strings
-need to decode any string character that is between 2 uppercase characters
- if there arent 2 uppercase char, then there is nothing decode, return 0 in this case

implicit:
return 0 for empty string
return an empty list, if an empty list is given

Data structure:
start with empty list, will add numbers depending on string input

Algo:
declare an empty list
iterate through the input array




helper function
initialize count varible to 0
initialize a boolean to false
initialize a string with capitalized alphabet
iterate through the string
    check if the current element exists inside capitalized alphabet 
    AND next element is lowercased
        


Test cases:
print(decode(['ZoL', 'heLlo', 'XX']) == [1, 0, 0])
print(decode(['foUrsCoreAnd', 'seven', '']) == [2, 0, 0])
print(decode(['lucYintheskyWith', 'dIaMonDs']) == [8, 1])
print(decode([]) == [])
"""

"""
victor

'''
Inputs: list of messages (strings)
Outputs: list of numbers

requirements:
    - each number is the number of lowercase characters between the first two uppercase characters
    - if there aren't 2 uppercase characters, the number should be zero

a list of messages can be any length
a message can be any length

helper function to calculate the number for each message
    - loop through each character of the message
    - initialize two index variables (indexes of the two uppercase characters) to None
    - if the character is upper, reassign the first index variable to that index
    - if the character is upper, reassign the second index variable to that index
    - break the loop after second index variable has been reassigned
    - after looping through the message, check to see if either of the index variables are None
    - if either of the index variables are None, then return 0
    - if both index variables have been reinitialized, then we use string slicing
    - to grab the substring between both indexes
    - get the lnegth of that substring and return that

in the main function, loop through each of the input lists elements. then run the helper function 
on each message
'''

def decode(messages):
    return [decode_message(message) for message in messages]

def decode_message(message):
    first_index = None
    second_index = None

    for idx, char in enumerate(message):
        if char.isupper() and first_index is None:
            first_index = idx
        elif char.isupper() and second_index is None:
            second_index = idx
            break
        
    if None in [first_index, second_index]:
        return 0
        
    real_message = message[first_index + 1: second_index]

    return len(real_message)

print(decode(['ZoL', 'heLlo', 'XX']) == [1, 0, 0])
print(decode(['foUrsCoreAnd', 'seven', '']) == [2, 0, 0])
print(decode(['lucYintheskyWith', 'dIaMonDs']) == [8, 1])
print(decode([]) == [])
"""

"""
ostap
## Understanding
# Input: list of strings
# Output: list of integers. Each integer represents a number of lowercase letters
#   in-between first two uppercase letters in each string

# Explicit reqs
# - If there are no 2 uppercase letters, number should be 0

# Implicit reqs
# - If string is empty, number should be 0
# - If input list is empty. output should alse be an empty list

## Data Structure
# List for numbers

## Algorithm
# Create empty list decoded_messages
# Iterate over each string in input list
#   Set first_uppercase to False
#   Set lowercase_counter to 0
#   Iterate over each char in string
#       If char is uppercase:
#           If no first_uppercase:
#               set first_uppercase to True
#           else:
#               append lowercase_counter to decoded_messages
#               break inner loop
#       else:
#           counter += 1
# Return decoded_messages
"""
#
