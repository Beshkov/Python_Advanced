from collections import deque

price_of_bullet = int(input())
gun_barrel_size = int(input()) #capacity
bullets = [int(bullet) for bullet in input().split()]  # back to front <-
locks = deque([int(lock) for lock in input().split()])  # front to back ->
value_of_intelligence = int(input())
capacity = gun_barrel_size
spend_on_bullets = len(bullets)

while bullets:


    if bullets.pop() <= locks[0]:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")

    capacity -= 1
    if capacity == 0:
        if not bullets:
            break
        else:
            print("Reloading!")
            capacity = gun_barrel_size
    if not locks:
        break
if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    money_spend_on_bullets = (spend_on_bullets-len(bullets))*price_of_bullet
    print(f"{len(bullets)} bullets left. Earned ${value_of_intelligence - money_spend_on_bullets:.0f}")