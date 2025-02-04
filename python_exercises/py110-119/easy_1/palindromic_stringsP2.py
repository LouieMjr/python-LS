'''
Write another function that returns True if the string passed as an argument is
a palindrome, or False otherwise. This time, however, your function should be
case-insensitive, and should ignore all non-alphanumeric characters. If you
wish, you may simplify things by calling the is_palindrome function you wrote
in the previous exercise.

input: string
output: boolean

remove any nonalphanumeric character from string
call original is palindrome function on new string 
Either upper or lower case string

'''

from palindromic_stringsP1 import is_palindrome
import re

def is_real_palindrome(string):
    clean = re.sub(r'\W', '', string).casefold()
    return is_palindrome(clean)


print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True
