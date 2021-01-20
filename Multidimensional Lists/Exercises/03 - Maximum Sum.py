dict_of_range_and_sum = {}

def matrix_maker(row):
    matrix = []
    for r in range(row):
        # matrix.append(list(map(int,input().split(', '))))
        matrix.append([int(el) for el in input().split(' ')])
    return matrix


def max_sum_range(matrix, el_row, el_col):
    # row_1 = sum(matrix[el_row][:el_col+3])
    # row_2 = sum(matrix[el_row + 1][:el_col+3])
    # row_3 = sum(matrix[el_row + 2][:el_col+3])
    # summed_matrix = 0
    # max_summed_matrix = 0
    # summed_matrix = row_1 + row_2 + row_3
    # if summed_matrix > max_summed_matrix:
    #     max_summed_matrix = summed_matrix
    # return max_summed_matrix

    sum_of_range = 0
    some_helping_list = []
    row_help_list = 0
    for row in range(el_row, el_row + 3):
        some_helping_list.append([])
        for col in range(el_col, el_col + 3):
            sum_of_range += matrix[row][col]
            some_helping_list[row_help_list].append(matrix[row][col])
        row_help_list += 1
    dict_of_range_and_sum[sum_of_range] = some_helping_list

    return sum_of_range

row, columns = tuple(map(int, input().split()))
matrix = matrix_maker(row)
max_sum = 0
for el_row in range(row - 2):
    for el_col in range(columns - 2):
        current_max = max_sum_range(matrix, el_row, el_col)

        if max_sum < current_max:
            max_sum = current_max

print(f"Sum = {max_sum}")
for mini_list in dict_of_range_and_sum[max_sum]:

    print(" ".join([str(x) for x in mini_list]))