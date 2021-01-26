"""
Write a function called concatenate() that receives some strings, concatenates them and returns the result
"""

def concatenate(*args):
    temp = ''
    for arg in args:
        temp += arg
    return temp

print(concatenate("Soft", "Uni", "Is", "Great", "!"))