# Write a function that takes a list of lists that represents a 3x3 matrix and
# returns the transpose of the matrix. You should implement the function on your
# own, without using any external libraries.
#
# Take care not to modify the original matrix -- your function must produce a
# new matrix and leave the input matrix list unchanged.

# 0 1, 0 2 --- 1 2
#  5    8       2
# 1 0, 2 0 --- 2 1
#  4    3       9

def transpose(matrix):

    transposed = []
    for _ in range(len(matrix)):
        transposed.append([])

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            transposed[col].append(matrix[row][col])

    return transposed

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]


new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True
