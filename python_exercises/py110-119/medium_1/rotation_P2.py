# Write a function that rotates the last count digits of a number. To perform the rotation, move the first of the digits that you want to rotate to the end and shift the remaining digits to the left.

# inputs: number to be adjusted, number to adjust by - int
# output: adjusted number - int

# convert number into str form
# starting from the end of the string, move backwards however many places
# decided by the 2nd input number

# store element from index starting at the back of string
# slice up to that index but not including
# add to first slice, another slice starting from after that index to the end
# add stored element to the end of the sliced string
# return string in int form

def rotate_rightmost_digits(number, index):

    num_string = str(number)
    first_half = num_string[:-index]
    second_half = num_string[-index:]

    rotated_half = second_half[1:] + second_half[0]
    return int(first_half + rotated_half)


    if index == 1:
        return number
    string = str(number)
    length = len(string)

    add_to_end = string[-index]
    return int(string[:length - index] + string[-(index-1):] + add_to_end)


print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True
