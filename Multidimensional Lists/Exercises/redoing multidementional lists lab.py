# matrix = []
# for i in range(3):
#     matrix.append([])
#     for j in range( 2):
#         matrix[i].append(0)
# matrix = [ [ 0 for j in range(2)] for i in range(3)]
# print(matrix)


# rows, columns = (int(f) for f in input().split(', '))
# matrix = []
#
# # for i in range(rows):
# #     matrix.append([int(x) for x in input().split(', ')])
#
# matrix_2 = [[int(x) for x in input().split(', ')] for _ in range(rows)]
#
# # both works nice!
# matrix_sum = sum([sum(i)for i in matrix_2])
#
# print(matrix_sum)
# print(matrix_2)


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# for row in range(len(matrix)):
#     for col in range(len(matrix[row])):
#         print(matrix[row][col], end=" ")
#     print()

# [print(num) for num in [j for j in matrix]]

# rows, columns = tuple(map(int, input().split(', ')))
#
# matrix = [[int(col) for col in input().split()] for row in range(rows)]
#
# result = []
#
# for columns_index in range(columns):
#     columns_sum = 0
#     for row_index in range(rows):
#         columns_sum += matrix[row_index][columns_index]
#     result.append(columns_sum)
#
# [print(x) for x in result]

"""Task 3"""
# #
# rows = int(input())
#
# matrix = [[int(number) for number in input().split()]for _ in range(rows)]
# added = 0
# for row in range(rows):
#     for col in range(rows):
#         if row == col:
#             added += matrix[row][col]
#
# print(added)
""" My answer is not wrong! BUT """
#
# size = int(input())
# matrix = [[0] * size for row in range(0, size)]
#
# for x in range(0,size):
#     line = list(map(int,input().split()))
#     for y in range(0, size):
#         matrix[x][y] = line[y]
#
# sum_diagonal = sum(matrix[size - i - 1][size - i - 1] for i in range(size))
# print(sum_diagonal)


""" task 4 """

# size = int(input())
# matrix = [[x for x in input()] for _ in range(size)]
# looking_for = input()
# coordinates = None
#
# def is_symbol_in_matrix(matrix, symbol):
#
#     for r in range(len(matrix)):
#         for c in range(len(matrix)):
#             if matrix[r][c] == looking_for:
#                 coordinates = r, c
#                 return coordinates
#     return f"{looking_for} does not occur in the matrix"
#
#
# print(is_symbol_in_matrix(matrix,looking_for))

""" Task 5 """

row, col = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(', ')] for _ in range(row)]


def get_sum_of_submatrix(matrix, row_index, column_index, size):
    the_sum = 0
    for r in range(row_index, row_index + size):
        for c in range(column_index, column_index + size):
            the_sum += matrix[r][c]
    return the_sum

def get_best_submatrix_sum(matrix,submatrix_size):

    best_row_index = 0
    best_column_index = 0
    # best_sum = matrix[best_row_index][best_column_index] + matrix[best_row_index+1][best_column_index] + \
    #            matrix[best_row_index][best_column_index+1] + matrix[best_row_index+1][best_column_index+1]

    best_sum = get_sum_of_submatrix(matrix, 0, 0, 2)

    for row_index in range(len(matrix) - submatrix_size + 1):
        for col_index in range(len(matrix[row_index]) - submatrix_size + 1):
            current_sum = get_sum_of_submatrix(matrix, row_index, col_index, submatrix_size)
            if best_sum < current_sum:
                best_sum = current_sum
                best_row_index = row_index
                best_column_index = col_index
    return (best_row_index, best_column_index)

def print_result(coordinates, size):
    row_index, col_index = coordinates
    for r in range(row_index, row_index + size):
        row = []
        for c in range(col_index, col_index + size):
            row.append(matrix[r][c])
        print(' '.join(str(x) for x in row))
    print(get_sum_of_submatrix(matrix,row_index,col_index,size))

submatrix_size = 2
print()
print_result(get_best_submatrix_sum(matrix,submatrix_size),submatrix_size)