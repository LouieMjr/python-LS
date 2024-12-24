# a function that takes two lists of numbers and returns the result of merging the lists. The elements of the first list should become the elements at the even indexes of the returned list, while the elements of the second list should become the elements at the odd indexes.


# function takes in 2 arrays
## declare an empty array
## declare two variables, i, j both set to 0
## iterate while at least one variable is less than the length of an array
#### if curr index(i) is less than the len of the first array
####### push curr element to empty array
####### increment i by 1
#### if curr index(j) is less than the len of the second array
####### push curr element to empty array
####### increment j by 1
## return merged array

def merge(array1, array2):
    MERGED = []
    i, j = 0, 0

    while i < len(array1) or j < len(array2):
        if i < len(array1):
            MERGED.append(array1[i])
            i += 1
        if j < len(array2):
            MERGED.append(array2[j])
            j += 1
        
    return MERGED

                
print(merge([1, 2, 3], [4, 5, 6, 8, 9])) # => [1, 4, 2, 5, 3, 6]