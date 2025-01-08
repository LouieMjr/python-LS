# Using the multiply function from the "Multiplying Two Numbers" exercise, write a function that computes the square of its argument (the square is the result of multiplying a number by itself).




def multiply(num1, num2):
    return num1 * num2

square = lambda n: multiply(n, n)

# def square(number):
#     return multiply(number, number)

print(square(5) == 25)   # True
print(square(-8) == 64)  # True

# Further Exploration
# Suppose we want to generalize this function to a "power to the n" type function: cubed, to the 4th power, to the 5th, etc. How would we go about doing so while still using the multiply function?

def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result = multiply(result, base)

    return result

print(power(5, 3))