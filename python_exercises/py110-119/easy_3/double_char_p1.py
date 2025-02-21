'''
Write a function that takes a string, doubles every character in the string,
then returns the result as a new string.
''' 

'''
Algo:
declare a function that takes in a single character
 takes that character and repreats it twice 
 returns this double char

declare a function that takes in a string
iterates through the string
passes each element to the callback
stores the result to a variable

return updated string after loop is finished

'''

def double(char):
    return char + char

def repeater(string):
    return ''.join([char * 2 for char in string])
    # doubled_char = ''
    # for char in string:
    #     doubled_char += double(char)
    #
    # return doubled_char

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True

