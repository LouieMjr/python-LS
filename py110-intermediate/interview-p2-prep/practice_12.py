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
    clean_text = re.sub(r'[^\w]', '', sentence)
    print(clean_text)
    seen = set(clean_text.lower())
    print(seen)

    # seen = set()
    # sentence = sentence.lower()
    #
    # for char in ''.join(sentence.split()):
    #     if char not in seen and char.isalpha():
    #         seen.add(char)
    #
    return True if len(seen) >= 26 else False

print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)
