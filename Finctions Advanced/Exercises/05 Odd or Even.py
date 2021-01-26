"""
You will receive a command and a list of numbers:
If the command is "Odd": Print the sum of the Odd numbers multiplied by the length of the initial list.
If the command is "Even": Print the sum of the Even numbers multiplied by the length of the initial list.

"""
def sum_even_odd(command,some_list):
    if command == 'Odd':
        return sum([x for x in some_list if x % 2 != 0])*len(some_list)
    return sum([x for x in some_list if x % 2 == 0])*len(some_list)

command = input()
some_list = [int(x) for x in input().split()]

print(sum_even_odd(command,some_list))