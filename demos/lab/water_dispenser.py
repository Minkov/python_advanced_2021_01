from collections import deque

START_COMMAND = 'Start'
END_COMMAND = 'End'
REFILL_COMMAND = 'refill'

total_amount = int(input())

peoples_queue = deque()

while True:
    command = input()
    if command == START_COMMAND:
        break
    peoples_queue.append(command)

while True:
    command = input()
    if command == END_COMMAND:
        print(f'{total_amount} liters left')
        break
    if command.startswith(REFILL_COMMAND):
        command_params = command.split(' ')
        refill_liters = int(command_params[1])
        total_amount += refill_liters
    else:
        person = peoples_queue.popleft()
        person_liters = int(command)
        if person_liters <= total_amount:
            print(f'{person} got water')
            total_amount -= person_liters
        else:
            print(f'{person} must wait')
