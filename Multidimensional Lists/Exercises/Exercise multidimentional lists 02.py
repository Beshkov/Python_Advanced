def take_input():
    r, c = [int(x) for x in input().split()]
    matrix = [[el for el in input().split()] for _ in range(r)]
    return matrix

def find_square(matrix):
    number_of_occurrences = 0
    if len(matrix) == 1:
        return 1

    for row in range(len(matrix)-1):
        for column in range(len(matrix[row])-1):
            if matrix[row][column] == matrix[row][column+1] == matrix[row+1][column] == matrix[row+1][column+1]:
                number_of_occurrences += 1
    return number_of_occurrences

matrix = take_input()
print(find_square(matrix))