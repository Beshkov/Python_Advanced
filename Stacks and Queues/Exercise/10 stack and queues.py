"""
You will be given a sequence of integers – each indicating a cup's capacity.
After that you will be given another sequence of integers – a bottle with water in it.
Your job is to try to fill up all the cups.
Filling is done by picking exactly one bottle at a time.
You must start picking from the last received bottle and start filling from the first entered cup.
If the current bottle has N water, you give the first entered cup N water and reduce its integer value by N.
When a cup's integer value reaches 0 or less, it gets removed.
It is possible that the current cup's value is greater than the current bottle's value.
In that case you pick bottles until you reduce the cup's integer value to 0 or less.
If a bottle's value is greater or equal to the cup's current value,
you fill up the cup and the remaining water becomes wasted.
You should keep track of the wasted litters of water and print it at the end of the program.
If you have managed to fill up all the cups,
print the remaining water bottles, from the last entered – to the first,
otherwise you must print the remaining cups, by order of entrance – from the first entered – to the last.

"""
from collections import deque

cup_capacity = deque(map(int, input().split()))  # queue

filled_bottles = [int(x) for x in input().split()]  # stack

waster_liters = []

current_cup = 0
no_bottles_left = False
while cup_capacity:
    current_cup = cup_capacity.popleft()

    while filled_bottles:
        current_cup -= filled_bottles.pop()

        if current_cup <= 0:
            waster_liters.append(current_cup)
            break
    if not filled_bottles:
        no_bottles_left = True
        break

if no_bottles_left:
    print(f'Cups: {" ".join(map(str,cup_capacity))}')
else:
    print(f'Bottles: {" ".join(map(str,filled_bottles))}')
print(f'Wasted litters of water: {abs(sum(waster_liters))}')