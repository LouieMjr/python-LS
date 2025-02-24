'''
Write a function that takes a list of strings and returns a list of the same
string values, but with all vowels (a, e, i, o, u) removed.
'''

def strip_vowels(string):
    vowels = 'aeiouAEIOU'

    no_vowels = [letter
                 for letter in string
                 if letter not in vowels
                ]

    return ''.join(no_vowels)

def remove_vowels(alphabet_lst):

    return [strip_vowels(string) for string in alphabet_lst]

    # result = []
    # for string in alphabet_lst:
    #     non_vowels = ''
    #     for letter in string:
    #         if letter not in 'aeiouAEIOU':
    #             non_vowels += letter
    #
    #     result.append(non_vowels)
    #
    # return result


# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True
