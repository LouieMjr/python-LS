# Write a function that takes a positive integer, n, as an argument and prints a right triangle whose sides each have n stars. The hypotenuse of the triangle (the diagonal side in the images below) should have one end at the lower-left of the triangle, and the other end at the upper-right.

def triangle(n):

    space = ' '
    star = '*'
    result = ''
    for i in range(0, n + 1):
        result += space * (n - i)
        result += star * i
        result += '\n'
    print(result)

triangle(5)
triangle(9)
