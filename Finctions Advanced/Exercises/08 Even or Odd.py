"""
Create a function called even_odd that can receive different amount of numbers and a command at the end.
The command can be "even" or "odd".
Filter the numbers depending on the command and return them in a list.
Submit only the function in the judge system.
"""

def even_odd(*args):
    numbers = args[0:-1]
    if args[-1] == 'even':
        return list(filter(lambda x: x % 2 == 0, numbers))
    return [n for n in numbers if n % 2 != 0]

print(even_odd(1, 2, 3, 4, 5, 6, "even"))