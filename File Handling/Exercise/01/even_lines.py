import re

with open('text.txt', 'r') as file:
    content = file.readlines()

pattern = '[?!.,-]'
for i in range(len(content)):
    if i % 2 == 0:
        line_to_print = re.sub(pattern,'@',content[i])
        print(*[el for el in line_to_print.split()][::-1])