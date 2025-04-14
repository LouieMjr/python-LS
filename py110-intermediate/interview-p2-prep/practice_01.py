# Create a function that takes a list of numbers as an argument. For each
# number, determine how many numbers in the list are smaller than it, and place
# the answer in a list. Return the resulting list.
#
# When counting numbers, only count unique values. That is, if a number occurs
# multiple times in the list, it should only be counted once.

'''
input: list of numbers
output: list of numbers

can only count unique numbers, meaning,
if there is a duplicate number thats smaller only count 1 of them


declare a count variable, set to 0
declare a empty set
declare a empty list

iterate through list starting with first element
    iterate again, j starting at 0
        check if j element not in set
            if not, add current j element to set
            check if list at i, is greater than j element
                if true, increment count

    add count to output list
    reset set
    reste count
return output list
'''

def smaller_numbers_than_current(lst):
    count = 0
    seen = set()
    output = []

    for number in lst:
        for num in lst:
            if num not in seen:
                seen.add(num)
                if number > num:
                    count += 1

        output.append(count)
        count = 0
        seen.clear()

    return output


print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)
