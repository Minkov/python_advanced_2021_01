from collections import deque

END_COMMAND = 'End'
PAID_COMMAND = 'Paid'

names_queue = deque()

while True:
    command = input()
    if command == END_COMMAND:
        print(f'{len(names_queue)} people remaining.')
        break
    elif command == PAID_COMMAND:
        while names_queue:
            print(names_queue.popleft())
    else:
        names_queue.append(command)
