number = int(input())

list_of_names = set()

for _ in range(number):
    list_of_names.add(input())


for name in list_of_names:
    print(name)