'''
Modify the function from the previous exercise so it ignores non-alphabetic
characters when determining whether it should uppercase or lowercase each
letter. The non-alphabetic characters should still be included in the return
value; they just don't count when toggling the desired case.
'''

def staggered_case(string):
    result = ''
    upper = True

    for char in string:
        if char.isalpha():
            result += char.upper() if upper else char.lower()
            upper = not upper
        else:
            result += char

    return result

    # staggered = ''
    # i = 0
    #
    # for character in string:
    #     if i % 2 == 0 and character.isalpha():
    #         staggered += character.upper()
    #         i += 1
    #     elif i % 2 == 1 and character.isalpha():
    #         staggered += character.lower()
    #         i += 1
    #     else:
    #         staggered += character
    #
    # return staggered

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True
