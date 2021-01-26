# Write a program that receives a list of numbers. Print only the even numbers from the list. Use filter()

def even_numbers(list_of_numbers):
    return list(filter(lambda x: x % 2 == 0, list_of_numbers))


line = [int(n) for n in input().split()]
print(even_numbers(line))
