n_queries = int(input())

stack = []

for _ in range(n_queries):
    command_rl = input()

    if command_rl[0] == '1':
        element = command_rl.split()[1]
        stack.append(int(element))

    elif command_rl[0] == '2':
        if stack:
            stack.pop()
    elif command_rl[0] == '3':
        if stack:
            print(max(stack))
    elif command_rl[0] == '4':
        if stack:
            print(min(stack))

print(', '.join([str(stack.pop()) for _ in range(len(stack))]))