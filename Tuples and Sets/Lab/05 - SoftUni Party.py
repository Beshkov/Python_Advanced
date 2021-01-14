def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())
    return lines

def input_to_list_until_command(end_command):
    line = []
    while True:
        command = input()
        if command == end_command:
            break
        line.append(command)

    return line

def find_vip(guest):
    return guest[0].isdigit()


def separate_into_vip_and_regular(guests):
    vip_guests = []
    regular_guests = []
    for guest in guests:
        if find_vip(guest):
            vip_guests.append(guest)
        else:
            regular_guests.append(guest)
    return (sorted(vip_guests), sorted(regular_guests))


def print_result(guests):
    print(len(guests))
    (vip_guests, regular_guests) = separate_into_vip_and_regular(guests)

    for guest in vip_guests:
        print(guest)

    for guest in regular_guests:
        print(guest)


number = int(input())

expected_guests = input_to_list(number)

guests = input_to_list_until_command("END")

guest_missing = set(expected_guests).difference(guests)


print_result(guest_missing)
