"""
Somewhere in the future, there is a robotics factory. The current project is assembly line robots.
Each robot has a processing time, the time it needs to process a product.
When a robot is free it should take a product for processing and log his name, product and processing start time.
Each robot processes a product coming from the assembly line.
A product is coming from the line each second (so the first product should appear at [start time + 1 second]).
If a product passes the line and there is not a free robot to take it, it should be queued at the end of the line again.
The robots are standing on the line in the order of their appearance.
"""

"""
ROB-15;SS2-10;NX8000-3
8:00:00
detail
glass
wood
apple
End

"""

from collections import deque
from datetime import datetime, timedelta



robot_info = [x for x in input().split(';')]
starting_time = datetime.strptime(input(), '%H:%M:%S')

products = deque()
robots =[]
available_robots = deque()

for el in robot_info:
    robot = {}
    name, time = el.split('-')
    robot['name'] = name
    robot['time'] = int(time)
    robot['available_at'] = starting_time + timedelta(seconds=int(time))
    robots.append(robot)
    available_robots.append(robot)

product = input()
while not product == 'End':
    products.append(product)
    product = input()

current_time = starting_time + timedelta(seconds=1)

while len(products) > 0:
    current_product = products.popleft()

    if available_robots:
        current_robot = available_robots.popleft()
        current_robot['available_at'] = current_time + timedelta(seconds=current_robot['time'])
        robot = [el for el in robots if el ==  current_robot][0]
        robot['available_at'] = current_time + timedelta(seconds=current_robot['time'])
        print(f'{current_robot["name"]} - {current_product} [{current_time.strftime("%H:%M:%S")}]')
    else:
        for r in robots:
            if current_time >= r['available_at']:
                available_robots.append(r)
        if not available_robots:
            products.append(current_product)
        else:
            current_robot = available_robots.popleft()
            current_robot['available_at'] = current_time + timedelta(seconds=current_robot['time'])
            robot = [el for el in robots if el == current_robot][0]
            robot['available_at'] = current_time + timedelta(seconds=current_robot['time'])
            print(f'{current_robot["name"]} - {current_product} [{current_time.strftime("%H:%M:%S")}]')
    current_time = current_time + timedelta(seconds=1)

