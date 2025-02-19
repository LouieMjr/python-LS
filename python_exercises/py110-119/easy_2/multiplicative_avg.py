'''
Write a function that takes a list of positive integers as input, multiplies
all of the integers together, divides the result by the number of entries in
the list, and returns the result as a string with the value rounded to three
decimal places.
'''
'''
Algo:
declare a total varaible, set to 1
iterate through the list
    multiply each element by total and store result

divide total by the length of the list
return result with value rounded to three decimal places - could use round or
format method in combo with f string

'''
def multiplicative_average(numbers):
    total = 1
    for number in numbers:
        total *= number

    total = total / len(numbers)

    return f'{total:.3f}'


# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")
