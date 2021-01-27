"""
Create a function called age_assignment that receives different number of names
and then different number of key-value pairs.
The key will be a single letter (first letter of a name), and the value a number (age).
For each name, find its first letter in the key-value pairs and assign the age to the person's name.
At the end return a dictionary with all the names and ages as shown in the example.
Submit only the function in the judge system.
"""

def age_assignment(*args, **kwargs):
    people_and_ages = {}

    for person in args:
        people_and_ages[person] = kwargs[person[0]]

    return people_and_ages

print(age_assignment("Peter", "George", G=26, P=19))