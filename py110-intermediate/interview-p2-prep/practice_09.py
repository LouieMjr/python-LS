'''
inputs: 2 strings
outputs: number of times the second string occurs in the first

overlapping strings dont count
meaning for another occurence to count it can use any elements of the first

2nd string argument is never empty

if 1st string arg is empty return 0

declare count variable set to 0
delcare len variable set to length of 2nd string

iterate through 1st string 
until we get to the len of first string minus len of 2nd string. Skip to every 3rd element
    get slice of 1st string starting from the first element to the len of 2nd element
    check if slice is equal to the 2nd string
        if true, increment count by 1

return count

'''

def count_substrings(string, substring):
    step = len(substring)
    substring_count = 0
    i = 0

    while i <= len(string) - step:
        curr_substring = string[i:i+step]

        if curr_substring == substring:
            substring_count += 1
            i += step
        else:
            i += 1

    return substring_count

print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)
