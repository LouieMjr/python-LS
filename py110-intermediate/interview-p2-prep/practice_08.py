'''
inputs: non empty string
outputs: count of consecutive vowels/length of longest vowel substring


declare a variable count set to 0
declare a tmp counter set to 0
declare a variable toggle set to false
represent vowels in a tuple

iterate through string
    check if the curr char is in the vowels
        if yes, set toggle to true
        increment the tmp counter by 1

    if the curr char is not a vowel
        set toggle to false
        check if tmp counter is greater than count
            if yes, reassign count to tmp counter
            set tmp counter to 0

return count

'''

def longest_vowel_substring(string):
    vowel_count = 0
    tmp_count = 0
    toggle = False

    for char in string:
        if char in ('aeiou'):
            tmp_count += 1

        if char not in ('aeiou') or char == string[-1]:
            if tmp_count > vowel_count:
                vowel_count = tmp_count
            tmp_count = 0

    return vowel_count

print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)
