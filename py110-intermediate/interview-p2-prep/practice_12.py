'''
inputs: string
outputs: boolean

string has to contain every letter of the alphabet at least once to be considered a pangram

case insensitive

declare an empty set
iterate through lowercase version of string without puncuation
    check if set contains char and char is a letter
    if not, add char to set

if length of set is 26 return true
otherwise return false

'''
import re

def is_pangram(sentence):

    return len({char for char in sentence.lower() if char.isalpha()}) == 26
    # clean_text = re.sub(r'[^\w]', '', sentence)
    # seen = set(clean_text.lower())
    # return len(seen) == 26

    # seen = set()
    # sentence = sentence.lower()
    #
    # for char in sentence:
    #     if char.isalpha():
    #         seen.add(char)
    #
    return len(seen) >= 26

print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)
