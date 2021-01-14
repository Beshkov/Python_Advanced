n = tuple(map(float, input().split(' ')))

count_values = {}

for el in n:
    if el not in count_values:

        count_values[el] = 0

    count_values[el] +=1

for value, count in count_values.items():

    print(f"{value} - {count} times")