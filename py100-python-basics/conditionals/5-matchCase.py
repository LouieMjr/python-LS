animal = 'horse'

match animal:
    case 'duck':
        print('quack')
    case 'squirrel':
        print('nook nook')
    case 'horse':
        print('neigh')
    case 'bird':
        print('tweet tweet')
    case _:
        print('*cricket*')

'''
Since the value of animal is horse, neigh is printed.

neigh

The match-case statement, added in Python 3.10, provides a way to perform pattern matching. This feature can be considered an advanced form of traditional conditional statements.

Here's a breakdown:

The match keyword initiates the pattern matching block by evaluating the target expression (the value that immediately follows the match keyword).
Python then sequentially assesses each case pattern.
Upon finding a matching pattern, the corresponding code block is executed.
If none of the patterns align with the target value and there's an _ (underscore) case, this acts as a catch-all, executing its block.
One notable characteristic of the match-case construct is that once a pattern is satisfied and its block is executed, the flow exits the match structure. This ensures that only one block of code is executed per match.
In this example:

The value of animal is evaluated using the match keyword.
Python sequentially inspects the patterns specified in each case.
When the value 'horse' is matched, it leads to the execution of print('neigh').
Post-execution, the flow moves out of the match block, ensuring a singular matching case gets executed.
'''