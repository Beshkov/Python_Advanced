from collections import deque

rows, cols = [ int( el ) for el in input().split()]
# rows, cols = [ int( el ) for el in '5 6'.split()]


def make_matrix(rows, cols):
    return [[0 for c in range(cols)]for _ in range(rows)]

matrix = make_matrix(rows,cols)

snake = input()
# snake = 'SoftUni'
snake = deque(l for l in snake)


for row in range(len(matrix)):
    if row % 2 == 0:
        for col in range(len(matrix[row])):
            temp = snake.popleft()
            matrix[row][col] = temp
            snake.append(temp)
    else:
        for col in range(cols, 0, -1):
            temp = snake.popleft()
            matrix[row][col-1] = temp
            snake.append(temp)

for row in matrix:
    print("".join(map(str,row)))
