# A triangle is classified as follows:
#
#     Equilateral: All three sides have the same length.
#     Isosceles: Two sides have the same length, while the third is different.
#     Scalene: All three sides have different lengths.
#
# To be a valid triangle, the sum of the lengths of the two shortest sides must
# be greater than the length of the longest side, and every side must have a
# length greater than 0. If either of these conditions is not satisfied, the
# triangle is invalid.
#
# Write a function that takes the lengths of the three sides of a triangle as
# arguments and returns one of the following four strings representing the
# triangle's classification: 'equilateral', 'isosceles', 'scalene', or
# 'invalid'.

# input: 3 numbers representing the length of each side of a triangle
# output: the type of triangle is is or whether its a valid triangle or not

# to be a valid triangle, sum of the length of the two shortest sides need to be
# greater than the length of the longest side, and every side should be greater
# than 0.
# if the two shorter sides total is equal to the longer side but not greater
# than its invalid

# store sides in a list
# sort the list, lowest to largest
# check if 0 is in the list, if true, return string invalid
# store, first and second element of the list into two variables and add them
# together
# check if total is greater than the last element of the array, if true,
### convert list to a set.
### check length of set:
### if length is 1: return 'equilateral'
### if length is 2: return 'isosceles'
### if length is 3: return 'scalene'
# else return invalid


def triangle(s1, s2, s3):
    triangle_sides = [s1, s2, s3]
    triangle_sides.sort()

    s1, s2, s3 = triangle_sides

    if s1 > 0 and s1 + s2 > s3:
        length = len(set(triangle_sides))

        if length == 1:
            return 'equilateral'
        elif length == 2:
            return 'isosceles'
        else:
            return 'scalene'

    else:
        return 'invalid'

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True
