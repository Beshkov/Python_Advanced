def str_divider():
    return input().split(', ')

parking_lot = set()

for _ in range(int(input())):
    operation, car = str_divider()
    if operation == "IN":
        parking_lot.add(car)
    elif operation == "OUT":
        parking_lot.remove(car)

if len(parking_lot)>0:
    for car in parking_lot:
        print(car)
else:
    print("Parking Lot is Empty")