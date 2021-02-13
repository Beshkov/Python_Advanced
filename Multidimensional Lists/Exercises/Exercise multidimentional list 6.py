KNIGHT_SYMBOL = 'K'
EMPTY_SYMBOL = '0'

n = int(input())
matrix = [[el for el in input()] for _ in range(n)]
# n = 3
# matrix = [
#     ['K', 'K', "K"],
#     ['K', 'K', 'K'],
#     ['K', 'K', 'K'],
#
# ]
knight_movements = [
    (-2, -1),
    (-2, +1),
    (-1, -2),
    (-1, +2),
    (+1, -2),
    (+1, +2),
    (+2, +1),
    (+2, -1),


]


def is_valid(row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


def calculate_kills(matrix, row, column, knight_movements):
    kills = 0

    for r, c in knight_movements:
        potential_row = row + r
        potential_column = column + c
        if is_valid(potential_row, potential_column, n):
            if matrix[potential_row][potential_column] == KNIGHT_SYMBOL:
                kills += 1

    return kills


removed_counter = 0

while True:
    max_kills = 0
    killer_index = []

    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == KNIGHT_SYMBOL:
                kills = calculate_kills(matrix, row, col, knight_movements)
                if max_kills < kills:
                    max_kills = kills
                    killer_index = [row, col]

    if killer_index:
        matrix[killer_index[0]][killer_index[1]] = EMPTY_SYMBOL
        removed_counter += 1

    else:
        break

print(removed_counter)
