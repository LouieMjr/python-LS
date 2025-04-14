# Create a function that takes a list of integers as an argument and returns a
# tuple of two numbers that are closest together in value. If there are multiple
# pairs that are equally close, return the pair that occurs first in the list.

'''
input: list of ints
output: tuple of two numbers that are closest together in value

if there are multiple pairs that are equally close return the pair that occurs
first in the list

want to grab a slice of the first two numbers, get the difference and store that
number
then I want to slide, the slice by 1 and get the difference of those two numbers
and store the difference between that and repeat

declare a variable difference, set to inf
delcare an empty list

iterate through the list, starting at index 1
    store the difference between the current element and the element before
    current
    check if current difference is less than difference
    if true, append to the list, tuple of current element and element before it


return last element of list

'''

def closest_numbers(lst):
    difference = float('inf')
    # differences = []
    closest = None

    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            curr_diff = abs(lst[i] - lst[j])

            if curr_diff < difference:
                difference = curr_diff
                # differences.append((lst[i], lst[j]))
                closest = (lst[i], lst[j])

    # return differences[-1]
    return closest

print(closest_numbers([10, 5, 3, 8, 6, 2]))  # should be (5, 6)
print(closest_numbers([1, 3, 5, 7, 9, 11]))  # should be (1, 3)
print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))
