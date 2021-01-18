def matrix_input():
    row = input()
    matrix = []
    for r in range(int(row)):
        # matrix.append(list(map(int,input().split(', '))))
        matrix.append([int(el) for el in input().split(' ')])
    return matrix


matrix = matrix_input()

primary_diagonal_sum = 0
secondary_diagonal_sum = 0

for i_row_col in range(len(matrix)):
    primary_diagonal_sum += matrix[i_row_col][i_row_col]

    secondary_diagonal_sum += matrix[i_row_col][len(matrix[i_row_col]) - 1 - i_row_col]

print(abs(primary_diagonal_sum - secondary_diagonal_sum))
