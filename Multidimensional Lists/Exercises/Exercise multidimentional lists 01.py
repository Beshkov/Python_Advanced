def take_input():
    n = int(input())
    matrix = [[int(el) for el in input().split()] for _ in range(n)]
    return matrix


def left_diagonal(matrix):
    left_sum = 0

    for row_index in range(len(matrix)):
        left_sum += matrix[row_index][row_index]
    return left_sum


def right_diagonal(matrix):
    right_sum = sum([matrix[len(matrix) - i_row - 1][i_row - len(matrix)] for i_row in range(len(matrix))])
    return right_sum


matrix = take_input()
left = left_diagonal(matrix)
right = right_diagonal(matrix)

print(abs(left-right))