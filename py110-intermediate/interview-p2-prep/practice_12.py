'''
inputs: string
outputs: boolean

string has to contain every letter of the alphabet at least once to be considered a pangram

rules:
ignore numbers and punctuation
case insensitive

Algo:

declare a variable named alphabet, set to a list of each letter as an element in the alphabet

iterate through the lowercase input string
    check if curr char is a letter
    AND check if current character exists in the alphabet list
        if true, remove current character from the alphabet list


return results of if length of the list is equal to 0

'''

def is_pangram(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = list(alphabet)

    for char in string.lower():
        if char.isalpha() and char in alphabet:
            alphabet.remove(char)

    return len(alphabet) == 0

    # return len({char for char in sentence.lower() if char.isalpha()}) == 26

print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)
