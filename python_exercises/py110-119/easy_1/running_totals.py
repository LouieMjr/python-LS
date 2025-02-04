'''
Write a function that takes a list of numbers and returns a list with the same
number of elements, but with each element's value being the running total from
the original list.

input: list of numbers
output: list of numbers with each value being a running total from the original
list

rules:
first element stays the same
start with first element as a total and add the next value in the list
return out a new list

test cases answer any questions I have

Data structure:
list

Algo:
declare an empty list
declare a total variable set to the first element of the list
append this value to the empty list

iterate through list, start at 2nd element of the list
    add and assign current element of list to current total
    append total to new list

return new list

'''

def running_total(numbers):
    if numbers == []: return []
    totals = []
    total = 0

    for num in numbers:
        total += num
        totals.append(total)

    return totals



print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20]) == [14, 25, 32, 47, 67]) # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True
