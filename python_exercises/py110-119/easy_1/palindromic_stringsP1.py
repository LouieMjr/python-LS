'''
Write a function that returns True if the string passed as an argument is a
palindrome, False otherwise. A palindrome reads the same forwards and
backwards. For this problem, the case matters and all characters matter.


input: string
output: boolean

rules:
a palindrome is a string that reads the same forwards and backwards
case and all characters matter, meaning and uppercase or a space char, will
cause the string to not be a palindrome
return true if its a palidrome, return false otherwise

Data structure:
no real use of any data structures that are needed

Algo:
Check if the length of the string is less than or equal to 1, if true, return
true
Check if the first element of the string is not equal to the last element of
the string, if true, return false
return a recursive call with both ends of the string sliced off


'''
def is_palindrome(string):
    # return string == string[::-1]
    if len(string) <= 1: 
        return True
    if string[0] != string[-1]:
        return False

    return is_palindrome(string[1:-1])

# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)
