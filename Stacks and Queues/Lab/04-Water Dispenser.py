from collections import deque

liters = int(input())

queue = deque()

while True:
    command = input()

    if command == 'Start':
        break

    queue.append(command)

while queue:
    line = input()

    if command == 'End':
        break

    if line.split()[0] == 'refill':
        refill = line.split()[1]
        liters += int(refill)


    elif int(line) > liters:
        print(f"{queue.popleft()} must wait")

    else:
        print(f"{queue.popleft()} got water")
        liters -= int(line)

print(f"{liters} liters left")
