'''
Write a function that takes a list as an argument and returns a list that
contains two elements, both of which are lists. Put the first half of the
original list elements in the first element of the return value and put the
second half in the second element. If the original list contains an odd number
of elements, place the middle element in the first half list.

'''
'''
input: one list
output: nested list with two lists, one list will contain first half of input
list, other list will contain second half of input list.

rules:
- split contents of list into two separate lists
- if input list contains odd number of elements, add the middle elements to the 
  first list
- if list contains 1 element, that element goes to first list and none in the
  second list
- if list is empty, return two nested empty lists

Algo:
get mid point of list by dividing length of list by 2
check if input list has even or odd amount of elements
if even
    turn middle into an int and reassign middle
if odd
    use math.ceil on mid point and reassign what the current mid point is

slice list up to mid point and store in a list
slice list from mid point to end of list and store in a list
return a list with both lists nested
'''
# import math

def halvsies(numbers):
    # middle = len(numbers) / 2
    # odd_length = len(numbers) % 2 == 1

    # middle = math.ceil(middle) if odd_length else int(middle)

    middle = (len(numbers) + 1) // 2
    return [numbers[:middle], numbers[middle:]]

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])

