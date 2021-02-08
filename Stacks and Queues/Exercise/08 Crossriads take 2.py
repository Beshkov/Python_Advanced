from collections import deque

green_light_duration = int(input())
free_window = int(input())
current_time = green_light_duration + free_window
command = input()
safe = 0
flag = True
while not command == "END":

    if command == "green":
        current_time = green_light_duration + free_window
    else:
        if (current_time - free_window) > 0:
            lane = deque([el for el in command])
            car = lane.copy()
            passing = ""
            for letter_index in range(len(car)):
                passing += car.popleft()
                current_time -= 1
                if current_time <= 0:
                    print("A crash happened!")
                    print(f"{''.join(lane)} was hit at {lane[letter_index+1]}.")
                    flag = False
                    break
            safe += 1
    if not flag:
        break
    command = input()

if flag:
    print(f"Everyone is safe.")
    print(f"{safe} total cars passed the crossroads.")