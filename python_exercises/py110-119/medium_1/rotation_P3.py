# Take the number 735291 and rotate it by one digit to the left, getting 352917.
# Next, keep the first digit fixed in place and rotate the remaining digits to
# get 329175. Keep the first two digits fixed in place and rotate again to get
# 321759. Keep the first three digits fixed in place and rotate again to get
# 321597. Finally, keep the first four digits fixed in place and rotate the final
# two digits to get 321579. The resulting number is called the maximum rotation
# of the original number.

# Write a function that takes an integer as an argument and returns the
# maximum rotation of that integer. You can (and probably should) use the
# rotate_rightmost_digits function from the previous exercise.

# inputs: number
# outputs: rotated number

# pattern based on test cases seems to be to continue to take a number and put
# that number at the end of the current number - two less than the length of
# the number.
# START with the first number - remove and put that at the end
# NEXT, KEEP current first number in place and move the following number to the
# end
# CONTINUE to increment, so that on the next iteration you keep the next two
# numbers in place, then the next three numbers in place and so on until you
# have kept a total of two less than the length of the number in place

# Algo
# import right_most_digits func
# check if number is an int, if true,
# iterate while index is less than or equal to length of string - 2
# Loop steps
# # pass in number and length - current index to import function
# # this function will take in a number and convert it to a string and will
# # rotate the numbers based on the current index (count) passed in
# # assign the results of the function to a variable and repeat Loop steps
# return result converted back to int form after loop is finished

from rotation_P2 import rotate_rightmost_digits

def max_rotation(number):
    # number_digits = len(str(number))
    # for count in range(number_digits, 1, -1):
    #     print(count)
    #     number = rotate_rightmost_digits(number, count)
    #
    # return number

    if not isinstance(number, int):
        return "Not an int"

    length = len(str(number))
    rotated_number = number
    count = 0

    while count <= length - 2:
        rotated_number = rotate_rightmost_digits(rotated_number,
                                                 length - count)
        count += 1

    return rotated_number

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True
