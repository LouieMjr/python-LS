'''
inputs: string full of numbers
outputs: greatest product of 4 consec digits 

rules:
the argument will always have more than 4 digits
based on test cases, looks like you cant sort


algo:
declare a variable product set to 1
declare a variable tmp_product set to 1

iterate through string
    get a slice of the string from the current element + the next 3
    check if length of slice is actually 4
        if true, iterate through slice
            multiply tmp_product by int form of curr ele

        check if tmp product is greater than product
            if true, reassign product to be value of tmp_product

return product

'''

def greatest_product(digits):
    product = 1
    tmp = 1

    for i, ele in enumerate(digits):
        slice = digits[i:i+4]
        if len(slice) == 4:
            for num in slice:
                tmp *= int(num)

            if tmp > product:
                product = tmp
        tmp = 1

    return product

print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6
