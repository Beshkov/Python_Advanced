# Write a program that prints the min and max values from a list and the sum of all the numbers in the list. Use min(), max() and sum()

def min_value(list_of_numbers):
    print(f"The minimum number is {min(list_of_numbers)}")

def max_value(list_of_numbers):
    print(f"The maximum number is {max(list_of_numbers)}")

def sum_value(list_of_numbers):
    print(f"The sum number is: {sum(list_of_numbers)}")

def min_max_sum(list_of_numbers):
    min_value(list_of_numbers)
    max_value(list_of_numbers)
    sum_value(list_of_numbers)

line = [int(n) for n in input().split()]

min_max_sum(line)