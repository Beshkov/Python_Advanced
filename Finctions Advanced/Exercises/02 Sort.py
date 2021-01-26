# Write a program that prints a sorted list of numbers in ascending order. Use sorted()

def sort_function(list_of_numbers):
    return sorted(list_of_numbers)


line = [int(n) for n in input().split()]
print(sort_function(line))