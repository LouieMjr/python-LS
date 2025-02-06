from pprint import  pp, pprint
import random

'''
Consider the following nested dictionary:

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

Compute and display the total age of the family's male members. Try working out
the answer with a comprehension.

The result should be 444.
'''
munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

result = [value['age'] for value in munsters.values() 
                       if value['gender'] == 'male']

#print(sum(result))


'''
Given the following data structure, return a new list with the same structure,
but with the values in each sublist ordered in ascending order. Use a
comprehension if you can.

THEN

Given the following data structure, return a new list with the same structure,
but with the values in each sublist ordered in ascending order as strings (that
is, the numbers should be treated as strings). Use a comprehension if you can. 
'''

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
# [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]

# sorted_sublists = [sorted(sublist) for sublist in lst]
# print(sorted_sublists)


sorted_list_treated_as_strings = [sorted(sublist, key=str) for sublist in lst]
#print(sorted_list_treated_as_strings)

'''
Given the following data structure, write some code that defines a dictionary
where the key is the first item in each sublist, and the value is the second.
'''
lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

d = {sublist[0]: sublist[1] for sublist in lst}
# print(d)


'''
Given the following data structure, sort the list so that the sub-lists are
ordered based on the sum of the odd numbers that they contain. You shouldn't
mutate the original list.

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

Note that the first sublist has the odd numbers 1 and 7; the second sublist has
odd numbers 1, 5, and 3; and the third sublist has 1 and 3. Since (1 + 3) < (1
+ 7) < (1 + 5 + 3), the sorted list should look like this:

[[1, 8, 3], [1, 6, 7], [1, 5, 3]]
'''

def odd_total(sublist):
    odd_nums = [num for num in sublist if num % 2 != 0]
    return sum(odd_nums)

# print(odd_total([1, 6, 7]))

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

sorted = sorted(lst, key=odd_total)
#print(sorted)
#print(lst)


'''
Given the following data structure, return a new list identical in structure to
the original but, with each number incremented by 1. Do not modify the original
data structure. Use a comprehension.

'''

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

def add_one(dictionary):
    return {key: value + 1 for key, value in dictionary.items()}

# print(add_one({'a': 1}))

nlst = [add_one(obj) for obj in lst]
#print(nlst, lst, sep='\n')

new_lst = [{key: value + 1 for key, value in dictionary.items()}
                            for dictionary in lst]
#print(new_lst)

'''
Given the following data structure return a new list identical in structure to
the original, but containing only the numbers that are multiples of 3.

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

The returned list should look like this:
[[], [3, 12], [9], [15, 18]]
'''

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

nlist = [[num for num in sublist if num % 3 == 0]
              for sublist in lst]

# print(nlist, lst, sep='\n')

'''
Given the following data structure, write some code to return a list that
contains the colors of the fruits and the sizes of the vegetables. The sizes
should be uppercase, and the colors should be capitalized.

The return value should look like this:
[["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]
'''

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

def get_colors_and_sizes(dictionary):
    if dictionary['type'] == 'fruit':
        lst = dictionary['colors']
        return [word.capitalize() for word in lst]
    else:
        return dictionary['size'].upper()


n = [get_colors_and_sizes(subdict) for subdict in dict1.values()]
# pprint(n)


'''
Given the following data structure, write some code to return a list that
contains only the dictionaries where all the numbers are even.
'''

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]


def even_elements(lst):
    for num in lst:
        if num % 2 != 0:
            return False

    return True


def check_dict_values(item):
    for value in item.values():
        if even_elements(value) == False:
            return False

    return True

# print(check_dict_values({'b': [2, 4, 6], 'c': [3, 6], 'd': [4]}))

n = [dictionary for dictionary in lst if check_dict_values(dictionary) == True]
# pprint(n)

def all_even(dictionary):
    for value in dictionary.values():
        if not all([num % 2 == 0 for num in value]):
            return False

    return True

t = [dictionary for dictionary in lst if all_even(dictionary)]
# pprint(t)



'''
A UUID (Universally Unique Identifier) is a type of identifier often used to
uniquely identify items, even when some of those items were created on a
different server or by a different application. That is, without any
synchronization, two or more computer systems can create new items and label
them with a UUID with no significant risk of stepping on each other's toes. It
accomplishes this feat through massive randomization. The number of possible
UUID values is approximately 3.4 X 10E38, which is a huge number. The chance of
a conflict, a "collision", is vanishingly small with such a large number of
possible values.

Each UUID consists of 32 hexadecimal characters (the digits 0-9 and the letters
a-f) represented as a string. The value is typically broken into 5 sections in
an 8-4-4-4-12 pattern, e.g., 'f65c57f6-a6aa-17a8-faa1-a67f2dc9fa91'.

Note that our description of UUIDs is a simplified description of how UUIDs are
formed. There are several UUID versions, each with some non-random
characteristics in some of the bits. These different versions can play a part
in certain applications.

Write a function that takes no arguments and returns a string that contains a
UUID.

'''

def generate_UUID():
    hexadec_char = '0123456789abcdef'
    # UUID = [random.choice(hexadec_char) for _ in range(32) ]

    # for i in range(len(UUID)):
    #     if i in {8, 13, 18, 23}:
    #         UUID.insert(i, '-')


    UUID = [random.choice(hexadec_char) if i not in {8, 13, 18, 23} else
            '-' for i in range(36)]

    # print(len(UUID))
    return ''.join(UUID)

    # while(len(UUID) < 36):
    #     UUID += random.choice(hexadec_char)
    #     print(UUID)
    #
    #     if len(UUID) in {8, 13, 18, 23, 28}:
    #         UUID += '-'

    # return UUID


# print(generate_UUID())


'''
The following dictionary has list values that contains strings. Write some code
to create a list of every vowel (a, e, i, o, u) that appears in the contained
strings, then print it.
'''

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

def list_of_vowels(dictionary):
    vowels = 'aeiou'
    chars = [char for lst in dictionary.values()
                  for word in lst
                  for char in word if char in vowels]

    # vowel_lst = [[ele for ele in string if ele in vowels]
    #                     for string in lst]

    return chars

print(list_of_vowels(dict1))

# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']
