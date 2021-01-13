from collections import deque
queue = deque()


while True:
    read_str = input()

    if read_str == "End":
        break
    elif read_str == "Paid":
        while queue:
            print(queue.popleft())
    else:
        queue.append(read_str)

print(f"{len(queue)} people remaining.")