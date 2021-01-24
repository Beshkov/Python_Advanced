box_with_cloths = [int(cloth) for cloth in input().split()]

rack_capacity = int(input())

rack_counter = 1

summed_capacity = rack_capacity

for _ in range(len(box_with_cloths)):
    cloth = box_with_cloths.pop()
    if summed_capacity >= cloth:
        summed_capacity -= cloth
    else:
        rack_counter += 1
        summed_capacity = rack_capacity
        summed_capacity -= cloth

print(rack_counter)
a = 5