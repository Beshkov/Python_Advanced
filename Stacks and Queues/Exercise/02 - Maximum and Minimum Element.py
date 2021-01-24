from sys import maxsize
n_queries = int(input())

stack = []


def push(numb, stack):
    stack.append(int(numb))
    return stack

def deleter(stack):
    if len(stack) > 0:
        stack.pop()
    return stack

def wl_max(stack):
    max = - maxsize
    for el in stack:
        if max < el:
            max = el
    print(max)

def wl_min(stack):
    minx = maxsize
    for el in stack:
        if minx > el:
            minx = el
    print(minx)

for _ in range(n_queries):
    command_rl = input()

    if command_rl[0] == '1':
        element = command_rl.split()[1]
        stack = push(element, stack)
    elif command_rl[0] == '2':
        stack = deleter(stack)
    elif command_rl[0] == '3':
        wl_max(stack)
    elif command_rl[0] == '4':
        wl_min(stack)

print(', '.join([str(stack.pop()) for _ in range(len(stack))]))
