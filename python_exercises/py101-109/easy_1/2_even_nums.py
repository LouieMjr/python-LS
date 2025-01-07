#Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.

# Bonus Question: Can you solve the problem by iterating over just the odd numbers?

def print_even_nums(start, end):
    for i in range(start, end, 2):
        print(i)

print_even_nums(2, 101)