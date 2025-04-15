# Create a function that takes a string argument and returns a dict object in
# which the keys represent the lowercase letters in the string, and the values
# represent how often the corresponding letter occurs in the string.

'''
input: string
output: dict with letters as keys and freq count as values

only lowercase letters count

declare an empty dict
iterate through string
    check if curr char is an actual letter and its lowercase
        check if curr char does not exist in dict
            if true, store curr char as key and current value as one
        if it does exist already, increment that characters value by 1

return dict

'''

def count_letters(string):
    result = {}

    for char in string:
        if char.isalpha() and char.islower():
            result[char] = result.get(char, 0) + 1

    return result


expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})
