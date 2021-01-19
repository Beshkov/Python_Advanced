def matrix_input(row):
    matrix = []
    for r in range(int(row)):
        # matrix.append(list(map(int,input().split(', '))))
        matrix.append(input().split(' '))
    return matrix


def box(matrix, row, col):
    aa = matrix[row][col]
    ab = matrix[row][col + 1]
    ba = matrix[row + 1][col]
    bb = matrix[row + 1][col + 1]
    if aa == ab and aa == ba and aa == bb:
        return True
    return False


row, col = input().split()

matrix = matrix_input(row)

counter = 0

for current_row in range(int(row) - 1):
    for current_col in range(int(col) - 1):
        if box(matrix, current_row, current_col):
            counter += 1

print(counter)