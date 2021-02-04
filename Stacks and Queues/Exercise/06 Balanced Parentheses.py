s = []

brackets = {'{': '}', '[': ']', '(': ')' }

rd_line = input()
result = ''
for el in rd_line:
    if el in ('{', '[', '('):
        s.append(el)
    elif el in ('}', ']', ')'):
        if len(s)<1:
            result = 'NO'
            break
        else:
            if brackets[s.pop()] == el:
                result = 'YES'

            else:
                result = 'NO'
                break

print(result)