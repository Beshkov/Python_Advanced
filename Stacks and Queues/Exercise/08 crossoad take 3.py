from collections import deque

green_light = int(input())
free_window = int(input())
safe = []
waiting_cars = deque()

command = input()
while not command == "END":

    if command != "green":
        waiting_cars.append(command)
    else:
        time = green_light + free_window
        while waiting_cars:
            crossing = waiting_cars.popleft()
            time -= len(crossing)
            safe.append(crossing)
            if time < 0:
                print("A crash happened!")
                print(f"{crossing} was hit at {crossing[time]}.")
                quit()
            if time - free_window <= 0:
                break
    command = input()
print(f"Everyone is safe.")
print(f"{len(safe)} total cars passed the crossroads.")