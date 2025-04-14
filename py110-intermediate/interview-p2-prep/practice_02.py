# Create a function that takes a list of integers as an argument. The function
# should return the minimum sum of 5 consecutive numbers in the list. If the
# list contains fewer than 5 elements, the function should return None.

'''
input: list of ints
output: minimum sum of 5 consecutive numbers in the list OR none if list is less
than 5 numbers

return none if len of list is less than 5

iterate through the range of len of list - 5
for each number
    iterate from that number to the next 5 in the list
    adding up the total of each number
    append total to output list

return min of output list


'''

def minimum_sum(lst):
    if len(lst) < 5:
        return None

    curr_min = float('inf')

    for i in range(len(lst) - 4):
        curr_sum = sum(lst[i:i + 5])

        if curr_sum < curr_min:
            curr_min = curr_sum

    return curr_min


    # output = []
    #
    # for i in range(len(lst) - 4):
    #     total = 0
    #     for j in range(i, i + 5):
    #         total += lst[j]
    #
    #     output.append(total)
    #
    # return min(output)

print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)
