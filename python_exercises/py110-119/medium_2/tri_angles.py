# A triangle is classified as follows:
#
#     Right: One angle is a right angle (exactly 90 degrees).
#     Acute: All three angles are less than 90 degrees.
#     Obtuse: One angle is greater than 90 degrees.
#
# To be a valid triangle, the sum of the angles must be exactly 180 degrees, and
# every angle must be greater than 0. If either of these conditions is not
# satisfied, the triangle is invalid.
#
# Write a function that takes the three angles of a triangle as arguments and
# returns one of the following four strings representing the triangle's
# classification: 'right', 'acute', 'obtuse', or 'invalid'.
#
# You may assume that all angles have integer values, so you do not have to
# worry about floating point errors. You may also assume that the arguments are
# in degrees.

# input: 3 integers, representing degrees of a triangle
# output: returns a string representing the triangles classification

# to be a valid triangle the sum of the angles must be exactly 180 degrees and
# every angle must be greater than 0. 

# high level:
# make sure to check all input numbers are greater than 0 and that all three numbers
# added together equal 180 degrees, if not, return an invalid string

# otherwise
# check if one of the numbers is greater than 90, if true, return obtuse
# else if one of the numbers is equal to 90, if true, return right
# else if none of greater than or equal to 90, return acute


def triangle(s1, s2, s3):

    angles = [s1, s2, s3]

    if 0 in angles or sum(angles) != 180:
        return 'invalid'

    if any(angle > 90 for angle in angles):
        return 'obtuse'

    if 90 in angles:
        return 'right'

    return 'acute'

print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True
