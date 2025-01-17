"""
PROBLEM:

Given a string, write a function `change_me` which returns the same
string but with all the words in it that are palindromes uppercased.

"""
# split string into array of words
# declare an empty string
# iterate through array
# invoke palindrome func,
    # if true, uppercase curr string, & add it to empty string
    # else, add curr string it to empty string


# inputs string
# check if 1st element is not equal to last element
# if true, return false
# else return substring

def is_palindrome(strr):
    if len(strr) <= 1:
        return True
    if strr[0] != strr[-1]:
        return False
    return is_palindrome(strr[1:-1])


def change_me(string):
    array_of_words = string.split()
    newstr = ''
    for ele in array_of_words:
        if(is_palindrome(ele)):
            newstr += ele.upper()
        else:
            newstr += ele
        newstr += ' '
    
    return newstr


# Comments show expected return values
print(change_me("We will meet at noon"))       # "We will meet at NOON"
print(change_me("No palindromes here"))       # "No palindromes here"
print(change_me(""))                           # ""
print(change_me("I LOVE mom and dad equally")) # "I LOVE MOM and DAD equally"