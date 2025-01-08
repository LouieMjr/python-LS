# Write a function that takes a non-empty string argument and returns the middle character(s) of the string. If the string has an odd length, you should return exactly one character. If the string has an even length, you should return exactly two characters.

def center_of(string):
    length = len(string)
    if length % 2 == 0:
        center_left = (len(string) // 2) - 1
        return string[center_left:center_left + 2] # plus 2 here because stop index is not inclusive
    
    center_idx = (len(string) // 2)
    return string[center_idx]



print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True