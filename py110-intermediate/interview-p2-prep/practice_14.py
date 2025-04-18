'''
inputs: number
outputs: number

if an arugment is negative return 0
return the sum of all the multiples of 7 and 11
if theres a multiple of both 7 and 11 count it only once

if input is less than or equal to 0, return 0

iterate through a range up to the input number
for each number in the range
    if the current number is a multiple of 7 or a multiple of 11
        add the number to the total

return the sum of the toal

'''

def seven_eleven(number):
    if number < 0:
        return 0

    loop = range(number)

    return sum(num for num in loop if num % 7 == 0 or num % 11 == 0)


print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)
