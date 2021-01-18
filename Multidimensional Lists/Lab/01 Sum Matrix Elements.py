# # matrix = [
# [7, 1, 3, 3, 2, 1],
# [1, 3, 9, 8, 5, 6],
# [4, 6, 7, 9, 1, 0]
# ]

def matrix_input():
    (row, columns) = input().split(', ')
    matrix = []
    for r in range(int(row)):
        # matrix.append(list(map(int,input().split(', '))))
        matrix.append([int(el) for el in input().split(', ')])
    return matrix


#row, columns = input().split(', ')
matrix = matrix_input()

sum_of = 0

for i in range(len(matrix)):
    for c in range(len(matrix[i])):
        sum_of += matrix[i][c]

print(sum_of)
print(matrix)
