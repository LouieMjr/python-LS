# Write a program that asks the user to enter an integer greater than 0, then asks whether the user wants to determine the sum or the product of all numbers between 1 and the entered integer, inclusive.


# Please enter an integer greater than 0: 5
# Enter "s" to compute the sum, or "p" to compute the product. s

# The sum of the integers between 1 and 5 is 15.

# Please enter an integer greater than 0: 6
# Enter "s" to compute the sum, or "p" to compute the product. p

# The product of the integers between 1 and 6 is 720.
from math import prod

multiply = lambda n: prod(range(1, n + 1))
add = lambda n: sum(range(0, n + 1))

def display_sum_or_product():
    num = int(input('Enter an integer greater than 0: '))
    response = input('Enter "s" to compute the Sum or "p" to compute the product: ')
    
    if response == 'p':
        total = multiply(num)
    if response == 's':
        total = add(num)
    
    print(total)

display_sum_or_product()