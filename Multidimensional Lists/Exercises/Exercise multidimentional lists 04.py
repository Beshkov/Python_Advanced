r, c = tuple(int(el) for el in input().split())
matrix = [[el for el in input().split()] for _ in range(r)]


def is_valid(command, matrix):
    if not command.split()[0] == 'swap' or not len(command.split()) == 5:
        print('Invalid input!')
        return
    row_one, col_one, row_two, col_two = [int(x) for x in command.split()[1:]]
    if not (row_one < len(matrix) and row_two < len(matrix)) or not (
            col_one < len(matrix[0]) and col_two < len(matrix[0])):
        print('Invalid input!')
        return

    return (row_one, col_one, row_two, col_two)


def swap(command, matrix):
    if is_valid(command, matrix):
        r_1, c_1, r_2, c_2 = is_valid(command, matrix)
        matrix[r_1][c_1], matrix[r_2][c_2] = matrix[r_2][c_2], matrix[r_1][c_1]
        [print(" ".join(map(str, num))) for num in [submatrix for submatrix in matrix]]


command = input()

while not command == "END":
    swap(command, matrix)

    command = input()



# def check_if_index_is_valid(index_row,index_col, rows, cols):
#     if 0 <= index_row < rows and 0<= index_col < cols:
#         return True
#     return False
#
# def check_if_command_is_valid(command,coordinates, rows, cols):
#     if len(coordinates) == 4 and command == "swap":
#         for index in range(0,len(coordinates), 2):
#             if not check_if_index_is_valid(coordinates[index], coordinates[index+1], rows,cols):
#                 print('Invalid input!')
#                 return False
#         return True
#
# def print_matrix(matrix):
#     for row_index in range(len(matrix)):
#         for col_index in range(0,len(matrix[row_index])):
#             print(matrix[row_index][col_index], end=' ')
#         print()
#
#
# def init_matrix(rows):
#
#     matrix = []
#     for _ in range(rows):
#         matrix.append([el for el in input().split()])
#     return matrix
#
# rows, cols = [int(el) for el in input().split()]
# matrix = init_matrix(rows)
# data = input()
#
# while not data == "END":
#
#     splitted_data = data.split()
#     try:
#         command = splitted_data[0]
#         coordinates = [int(el) for el in splitted_data[1:]]
#     except:
#         print("Invalid input")
#     if check_if_command_is_valid(command,coordinates, rows, cols):
#         temp = matrix[coordinates[0]][coordinates[1]]
#         matrix[coordinates[0]][coordinates[1]] = matrix[coordinates[2]][coordinates[3]]
#         matrix[coordinates[2]][coordinates[3]] = temp
#         print_matrix(matrix)
#
#     data = input()
