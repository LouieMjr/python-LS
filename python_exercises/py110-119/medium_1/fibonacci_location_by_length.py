import sys

sys.set_int_max_str_digits(50_000)

def find_fibonacci_index_by_length(length):
    prev, curr = 1, 1
    index = 2

    while len(str(curr)) < length:
        prev, curr = curr, prev + curr
        index += 1

    return index

    # for index in range(3, sys.maxsize):
    #     prev, curr = curr, prev + curr
    #     string_num = str(curr)
    #
    #     if len(string_num) == length:
    #         return index
    #
    # return curr


# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)
