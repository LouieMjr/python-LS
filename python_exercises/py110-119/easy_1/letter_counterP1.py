'''
Write a function that takes a string consisting of zero or more space-separated
words and returns a dictionary that shows the number of words of different
sizes.

Words consist of any sequence of non-space characters.


input: string
output: dictionary that shows the number of words of different sizes

rules:
input could be an empty string or space separated words
words consist o any sequence of non-space characters

based on test cases, seems like any puncuation is considered part of a word

data stucture:
store each word thats separated by a space into a list
dictionary

Algo:
split string into list of words separated by a space
declare an empty dict
iterate through list
    for each word, store length of string as the key and how many occurences of this
    length as the value

return dict

'''

def word_sizes(string):
    if not string: 
        return {}

    occurences_of_word_length =  {}
    list_of_words = string.split()
    obj = occurences_of_word_length

    for word in list_of_words:
        obj[len(word)] = obj.get(len(word), 0) + 1 

    return occurences_of_word_length


# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!' 
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall' 
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?" 
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})
