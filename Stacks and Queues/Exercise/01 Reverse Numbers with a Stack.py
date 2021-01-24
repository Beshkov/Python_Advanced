read_numbers = input().split()

stack = []

for number in read_numbers:
    stack.append(int(number))

for el in range(len(stack)):
    print(stack.pop(), end=" ")