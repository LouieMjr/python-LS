'''
Write a function that takes a list of numbers and returns the sum of the sums
of each leading subsequence in that list. Examine the examples to see what we
mean. You may assume that the list always contains at least one number.
'''

'''
start with a total of 0
    1. starting with the first element
    2. slice up to element and append to list then sum the list
    3. add sum of list to total
    repeat steps 1 and 2,
    but for each iteration slice starting from first element to next element
    and so on. append to list and then sum the list
    repeat step 3

'''

def sum_of_sums(numbers):

    return sum([number
                for i in range(len(numbers))
                for number in numbers[:i + 1]
                ])

    # total_sum = 0
    # running_sum = 0
    #
    # for num in numbers:
    #     running_sum += num
    #     total_sum += running_sum
    #
    # return total_sum


print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True
