'''
Write a function that takes a string, doubles every consonant in the string,
and returns the result as a new string. The function should not double vowels
('a','e','i','o','u'), digits, punctuation, or whitespace.

You may assume that only ASCII characters will be included in the argument.
'''

def double_consonants(string):

    return ''.join([char * 2 if char.isalpha() and char not in 'aeiou' else char for char in string])

    # double_up = ''
    # for char in string:
    #     if not char.isalpha() or char in 'aeiou':
    #         double_up += char
    #     else:
    #         double_up += char * 2
    #
    # print(double_up)
    # return double_up



# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")
