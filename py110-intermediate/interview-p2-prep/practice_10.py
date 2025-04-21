# Create a function that takes a string of digits as an argument and returns the
# number of even-numbered substrings that can be formed. For example, in the
# case of '1432', the even-numbered substrings are '14', '1432', '4', '432',
# '32', and '2', for a total of 6 substrings.
#
# If a substring occurs more than once, you should count each occurrence as a
# separate substring.

'''
inputs: string of digits
outputs: number of even-numbered substrings that can be formed

if a substring occurs more than once, count each occurence as a separate substring


delcare a count variable set to 0

iterate through string starting index i at 0
    iterate through string starting index j at i + 1
        convert curr ele to int form
        check if curr number is even
            if true, increment count by 1

return count
'''

def even_substrings(digits):
    count = 0

    for i, digit in enumerate(digits):
        if int(digit) % 2 == 0:
            count += i + 1

    return count

    # for i in range(len(digits)):
    #     for j in range(i+1, len(digits)+1):
    #         slice = digits[i:j]
    #
    #         if int(slice) % 2 == 0:
    #             count += 1
    #
    # return count

print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)
