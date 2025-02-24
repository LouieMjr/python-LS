'''
Given two lists of integers of the same length, return a new list where each
element is the product of the corresponding elements from the two lists.
'''

def multiply_items(lst1, lst2):
    return [a * b for a, b in zip(lst1, lst2)]

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True
