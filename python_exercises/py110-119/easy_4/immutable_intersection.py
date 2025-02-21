'''
Transform two lists into frozen sets and find their common elements.
'''

def intersection(a, b):
    return frozenset(a) & frozenset(b)

list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True
