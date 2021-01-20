import sys
row, columns = [int(x) for x in input().split()]

matrix = []
for _ in range(row):
    matrix.append([int(el) for el in input().split()])

max_sum = -sys.maxsize
keeping_list = []
size = 3


def max_sum_range(matrix, str_row, str_col, size):
    sum_of_range = 0
    some_helping_list = []
    for row in range(str_row, str_row + size):
        elements = []
        for col in range(str_col, str_col + size):
            sum_of_range += matrix[row][col]
            elements.append(matrix[row][col])
        some_helping_list.append(elements)
    return sum_of_range, some_helping_list


for el_row in range(row - size + 1):
    for el_col in range(columns - size + 1):
        current_max, list_of_el = max_sum_range(matrix, el_row, el_col, size)
        if max_sum < current_max:
            max_sum = current_max
            keeping_list = [x for x in list_of_el]

print(f"Sum = {max_sum}")
for mini_list in keeping_list:
    mini_list = [str(item) for item in mini_list]
    print(" ".join(mini_list))