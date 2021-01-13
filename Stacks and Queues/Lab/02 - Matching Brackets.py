read_str = input()

stack  = []

for el in range(len(read_str)):
    if read_str[el] == '(':
        stack.append(el)
    elif read_str[el] == ')':
        print(read_str[stack.pop():el+1])