# Write a function that takes one integer argument and returns True when the number's absolute value is odd, False otherwise.

# def is_odd(n):
    # return True if n % 2 != 0 else False

is_odd = lambda n: abs(n) % 2 == 1
print(is_odd(-1))