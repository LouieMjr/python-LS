# Create a function that takes two strings as arguments and returns True if some
# portion of the characters in the first string can be rearranged to match the
# characters in the second. Otherwise, the function should return False.
#
# You may assume that both string arguments only contain lowercase alphabetic
# characters. Neither string will be empty.

'''
inputs: 2 strings
outputs: boolean

2 string inputs, neither will be empty
both will only contain lowercase alphabetic characters

string 1 has to at least be the same length or greather than string 2



iterate through string 1
    check if curr char exists in string2
    if yes append char

return length of string 1 equal to length of string 2

'''

def unscramble(string1, string2):
    occurences = {}

    for char in string2:
        occurences[char] = occurences.get(char, 0) + 1

    for char in string1:
        if char in occurences:
            occurences[char] -= 1

    return all(count <= 0 for count in occurences.values())
    return not any(occurences.values())


print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)
