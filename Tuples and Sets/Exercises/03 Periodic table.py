given_number = int(input())

unique_chemicals = set()

for _ in range(given_number):
    chemicals = input().split()
    unique_chemicals.update(chemicals)
    # for el in chemicals:
    #     unique_chemicals.add(el)


[print(el) for el in unique_chemicals]
