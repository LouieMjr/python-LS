'''
Write a function that takes an integer argument and returns a list containing
all integers between 1 and the argument (inclusive), in ascending order.

You may assume that the argument will always be a positive integer.

'''

def sequence(limit):
    return list(range(1, limit + 1))
    # return [i for i in range(1, limit + 1)]

print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True
