number_of_inputs = int(input())
uniques_names = {input() for _ in range(number_of_inputs)}
[print(unique_name) for unique_name in uniques_names]