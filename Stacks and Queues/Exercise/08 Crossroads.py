from collections import deque


def crossing(a_list, time):
    temp = ''
    for el in a_list:
        temp += el
        time -= 1
        if time == -1:
            crash(a_list, el)
            exit()
    return (False, time)


def crash(a_list, el):
    print("A crash happened!")
    print(f"{''.join(a_list)} was hit at {el}.")
    return True


green_light_duration = int(input())
free_window = int(input())

lane = deque()

time_to_crash = green_light_duration + free_window
crashed = False
safely_passed_cars_counter = 0

command = input()

while not command == 'END':

    if command == 'green':
        time_to_crash = green_light_duration + free_window
    else:
        car = command
        if time_to_crash - free_window >= 0:
            lane.append(car)
            crossing_car = deque([el for el in lane.popleft()])
            crashed, time_to_crash = crossing(crossing_car, time_to_crash)
            safely_passed_cars_counter += 1
        if crashed:
            break

    command = input()

if not crashed:
    print(f"Everyone is safe.\n{safely_passed_cars_counter} total cars passed the crossroads.")
