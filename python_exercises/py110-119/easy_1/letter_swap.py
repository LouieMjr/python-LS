'''
Given a string of words separated by spaces, write a function that swaps the
first and last letters of every word.

You may assume that every word contains at least one letter, and that the
string will always contain at least one word. You may also assume that each
string contains nothing but words and spaces, and that there are no leading,
trailing, or repeated spaces.

input: string of words
output: string of words with first and last letters of every word swapped

rules:
every word containts at least one letter
strings contain only words and spaces
there are no leading, trailing or repeated spaces

Data structure:
possibly turn string into list of words

Algo:
if len of string is 1, return string
split string into list of words separated by spaces
iterate through list
for each word, swap first element with last element

join back to a string

'''

def swap(string):
    if len(string) == 1:
        return string
    words = string.split(' ')

    for i, word in enumerate(words):
        current_word = list(word)
        current_word[0], current_word[-1] = current_word[-1], current_word[0]

        word = ''.join(current_word)
        words[i] = word

    return ' '.join(words)


print(swap('Oh what a wonderful day it is') == "hO thaw a londerfuw yad ti si") # True 
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
