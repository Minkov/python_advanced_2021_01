def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


def input_to_list_until_command(end_command):
    lines = []
    while True:
        command = input()
        if command == end_command:
            break
        lines.append(command)

    return lines


def is_vip_guest(guest):
    return guest[0].isdigit()


def separate_into_vip_and_regular(guests):
    vip_guests = []
    regular_guests = []
    for guest in guests:
        if is_vip_guest(guest):
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


#
# reservations = [
#     '7IK9Yo0h',
#     '9NoBUajQ',
#     'Ce8vwPmE',
#     'SVQXQCbc',
#     'tSzE5t0p',
# ]
#
reservations = [
    'fc1oZCE0',
    'UgffRkOn',
    'm8rfQBvl',
    '7ugX7bm0',
    '9CQBGUeJ',
    '2FQZT3uC',
]
#
# guest_arrived = [
#     '9NoBUajQ',
#     'Ce8vwPmE',
#     'SVQXQCbc',
# ]

guests_arrived = [
    '2FQZT3uC',
    '9CQBGUeJ',
    'fc1oZCE0',
]

# for guest in guest_arrived:
#     reservations.remove(guest)

guests_count = int(input())
reservations = input_to_list(guests_count)
guests_arrived = input_to_list_until_command('END')
guests_not_arrived = set(reservations).difference(guests_arrived)
print_result(guests_not_arrived)

# guests_not_arrived = set()
# for guest in reservations:
#     if guest not in guest_arrived:
#         guests_not_arrived.add(guest)
