'''
Modify the word_sizes function from the previous exercise to exclude
non-letters when determining word size. For instance, the word size of "it's"
is 3, not 4.

input: string
output: dictionary of word length occurences

rules:
only rule different from previous function is that puncuation does not count toward length

data stucture:
list
dictionary

Algo:
remove all non-alpha characters from string but keep spaces


'''

import re 
from letter_counterP1 import word_sizes as count_word_size

def word_sizes(string):
	# clean = re.sub(r'[^\w\s]', '', string) #includes underscores _
	clean = re.sub(r'[^a-zA-Z\s]', '', string) #removes _ unlike solution above
	print(clean)
	return count_word_size(clean)


# All of these examples should print True
string = 'Four_ score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!' 
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})
