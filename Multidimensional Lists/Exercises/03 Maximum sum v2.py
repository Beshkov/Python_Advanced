def matrix_maker(row):
    matrix = []
    for _ in range(row):
        # matrix.append(list(map(int,input().split(', '))))
        matrix.append([int(el) for el in input().split()])
    return matrix


rows, columns = input().split()
rows = int(rows)
columns = int(columns)
current_sum = 0
max_sum = 0
size = 3

row = None
column = None

matrix = matrix_maker(rows)

for r in range(rows - size + 1):
    for c in range(columns - size + 1):
        current_sum = matrix[r][c] + matrix[r][c + 1] + matrix[r][c + 2] \
                      + matrix[r + 1][c] + matrix[r + 1][c + 1] + matrix[r + 1][c + 2] \
                      + matrix[r + 2][c] + matrix[r + 2][c + 1] + + matrix[r + 2][c + 2]

        if current_sum > max_sum:
            max_sum = current_sum
            row = r
            column = c

print(f"Sum = {max_sum}")
for i in range(3):
    for j in range(3):
        print(matrix[row+i][column+j], end=" ")
    print()

# print(f"{matrix[row][column]} {matrix[row][column + 1]} {matrix[row][column + 2]}")
# print(f"{matrix[row + 1][column]} {matrix[row + 1][column + 1]} {matrix[row + 1][column + 2]}")
# print(f"{matrix[row + 2][column]} {matrix[row + 2][column + 1]} {matrix[row + 2][column + 2]}")
