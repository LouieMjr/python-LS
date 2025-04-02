# Write a function that computes the difference between the square of the sum of
# the first count positive integers and the sum of the squares of the first count
# positive integers.

# inputs: number
# output: int -> sqaure of sum minus sum of squares

# get all positive numbers from input number to 1
# have two tallys going, sum and square sum
# iterate
# one that is calculating the sum of adding all the numbers together
# another that is doing the same thing but also getting the square of each
# number before they are added together
# add the end square the total of sum
# then return the results of subtracting sum from square sum


def sum_square_difference(num):
    sum_ = 0
    squared_sum = 0

    for number in range(1, num + 1):
        sum_ += number
        squared_sum += number ** 2

    return (sum_ ** 2) - squared_sum

print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True
