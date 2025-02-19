'''
Write a function that takes two lists as arguments and returns a set that
contains the union of the values from the two lists. You may assume that both
arguments will always be lists.
'''

def union(lst1, lst2):
    # a = set(lst1)
    # b = set(lst2)
    # return a | b
    return set(tuple(lst1 + lst2))

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True
