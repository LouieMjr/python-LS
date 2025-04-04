
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


    # row = 0
    # col = 0
    # count = 1
    #
    # transposed = [row[:] for row in matrix]
    #
    # while row < len(transposed) - 1:
    #     x = row
    #     y = col
    #
    #     for _ in range(len(transposed[row]) - count):
    #         y += 1
    #         transposed[x][y], transposed[y][x] = transposed[y][x], transposed[x][y]
    #
    #     row += 1
    #     col += 1
    #     count += 1
    #
    # return transposed

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]


new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True
