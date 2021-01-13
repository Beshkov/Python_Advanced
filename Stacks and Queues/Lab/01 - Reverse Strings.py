read_str = input()

stack = []

reversed_str = ""

for el in read_str:
    stack.append(el)

while stack:
    reversed_str += stack.pop()

print(reversed_str)