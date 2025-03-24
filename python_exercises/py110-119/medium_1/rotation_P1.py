# Write a function that rotates a list by moving the first element to the end of
# the list. Do not modify the original list; return a new list instead.
#
# If the input is an empty list, return an empty list. 
# If the input is not a list, return None.
#
# Review the test cases below, then implement the solution accordingly.

# All of these examples should print True

# inputs: list
# outputs: new list with first element removed from the front and added to the
# end

# if input is anything other than a populated list: return none

# check if input is not a list: if true, return None
# check if input is has no length: if true, return empty list

# create a shallow copy of the list
# pop first element from shallow list, store popped element
# append popped element to end of shallow list
# return shallow copy of list

def rotate_list(lst):
    if not isinstance(lst, list):
        return None
    if len(lst) == 0:
        return []

    return lst[1:] + [lst[0]]
    # list_copy = lst.copy()
    # first = list_copy.pop(0)
    # list_copy.append(first)
    # return list_copy


print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])
