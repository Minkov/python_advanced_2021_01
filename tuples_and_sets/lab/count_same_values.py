values = map(float, input().split(' '))

values_counts = {}
for value in values:
    if value not in values_counts:
        values_counts[value] = 0
    values_counts[value] += 1

for (value, count) in values_counts.items():
    print(f'{value} - {count} times')
