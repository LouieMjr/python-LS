'''
inputs: nonempty string
outupts: tuble consisting of shortest possible substring and how many times it occurs

input string will only contain lowercase alphabetic letters

declare an empty string
iterate through input string
    add curr letter to empty string
    store results of dividing len of input string by len of new string
    store results of multiplying new string by results of division
    if results are equal to input string
        return tuple with substring and 

'''

def repeated_substring(string):
    substring = ''

    for char in string:
        substring += char
        multiplier = len(string) // len(substring)
        result = substring * multiplier
        if result == string:
            return (substring, multiplier)



print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))

