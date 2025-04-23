'''
inputs: string 
output: count of distinct case insens alphabetic characters and numeric digits that occur more than once 


rules: 
Input string will contain only alphanumeric characters
a string without any duplicates will return 0
dont need to consider any elements that appear only once

DS:
dict


algo:
lowercase entire string
declare an empty dict to store the occurences of an element

iterate through the string
    add current element as a key and add 1 each time the element is found in the string, as the value

get current values of dict
for each value in dict values greater than 1, add 1 to the count variable

return count
'''

def distinct_multiples(string):
    frequency = {}

    for char in string.lower():
        frequency[char] = frequency.get(char, 0) + 1

    return sum(1 for value in frequency.values() if value > 1)


print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5
