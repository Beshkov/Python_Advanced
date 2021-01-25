from collections import deque

n_line = int(input())

stations = deque()

# pumps = []    # 0 - 5
# petrol_list = deque([])   # 1, 10, 3, 11, 7
# km_list = deque([])      # 5, 3, 4, 20, 7
#
#
# for ind in range(n_line):
#     petrol, km = (int(el) for el in input().split())
#     pumps.append(ind)
#     petrol_list.append(petrol)
#     km_list.append(km)

for _ in range(n_line):
    stations.append(tuple(int(x) for x in input().split()))

for big_circle in range(n_line):
    is_valid = True
    tank = 0
    for small_circle in range(n_line):
        tank += (stations[small_circle][0] - stations[small_circle][1])

        if tank < 0:
            is_valid = False
            stations.append(stations.popleft())
            break


    if is_valid:
        print(big_circle)
        break