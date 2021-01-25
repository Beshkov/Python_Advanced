n_line = int(input())

petrol_pump = []    # 0 - 5
petrol_list = []    # 1, 10, 3, 11, 7
km_list = []        # 5, 3, 4, 20, 7


for ind in range(n_line):
    petrol, km = [int(el) for el in input().split()]
    petrol_pump.append(ind)
    petrol_list.append(petrol)
    km_list.append(km)

# km_max_index = km_list.index((max(km_list)))
# petrol_max_index = petrol_list.index(max(petrol_list))
#
# if max(km_list) > max(petrol_list) and km_max_index == petrol_max_index:
#     petrol_list.pop(petrol_max_index)
#     km_list.pop(km_max_index)
#

discarded_km = []
discarded_petrol = []

start_at = None

flag = False

while True:
    for i in range(len(petrol_pump), 0, -1):
        if petrol_list[-1] >= km_list[-1]:
            start_at = petrol_list.index(petrol_list[-1])
            flag = True
            break
        else:
            discarded_km.append(km_list.pop())
            discarded_petrol.append(petrol_list.pop())


    if flag:
        break

print(start_at)

""""
5
1 5
10 3
3 4
10 20
7 7
"""