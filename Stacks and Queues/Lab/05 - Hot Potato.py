from collections import deque
kids = input().split(' ')
toss = int(input())

q = deque(kids)

counter = 0

while len(q) > 1:
    counter += 1
    counter_player = q.popleft()
    if counter == toss:
        print(f"Removed {counter_player}")
        counter = 0
    else:
        q.append(counter_player)
print(f"Last is {q.popleft()}")