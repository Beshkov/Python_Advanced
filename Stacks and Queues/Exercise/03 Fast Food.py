quantity_of_the_food = int(input())

queue_of_orders =[int(el) for el in input().split()]

print(max(queue_of_orders))

for order in range(len(queue_of_orders)):
    if queue_of_orders[0] > quantity_of_the_food:
        break
    else:
        quantity_of_the_food -= int(queue_of_orders.pop(0))


if not queue_of_orders:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(map(str,queue_of_orders))}")