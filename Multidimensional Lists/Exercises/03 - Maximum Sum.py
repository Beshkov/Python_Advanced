def matrix_maker(row):
    matrix = []
    for r in range(row):
        # matrix.append(list(map(int,input().split(', '))))
        matrix.append([int(el) for el in input().split(' ')])
    return matrix


def max_sum_range(matrix, el_row, el_col):
    row_1 = sum(matrix[el_row][:el_col+3])
    row_2 = sum(matrix[el_row + 1][:el_col+3])
    row_3 = sum(matrix[el_row + 2][:el_col+3])
    summed_matrix = 0
    max_summed_matrix = 0
    summed_matrix = row_1 + row_2 + row_3
    if summed_matrix > max_summed_matrix:
        max_summed_matrix = summed_matrix
    return max_summed_matrix


row, columns = tuple(map(int, input().split()))
matrix = matrix_maker(row)

for el_row in range(row - 2):
    for el_col in range(columns - 2):
        current_max = max_sum_range(matrix, el_row, el_col)
        max_sum = 0
        if max_sum < current_max:
            max_sum = current_max

