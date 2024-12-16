'''
Rewrite your code from the previous exercise to use a ternary expression.

The code provided below randomly initializes random_number to either 0 or 1 each time it is executed.

Write an if statement that prints Yes! if random_number is 1, and No. if random_number is 0.
'''

import random
random_number = random.randint(0, 1)

print('yes' if random_number else 'no')

# if random_number:
#   print('Yes!')
# else:
#   print('No!')