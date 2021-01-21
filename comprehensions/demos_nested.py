matrix = [
    [1, 2, 3],
    [4, 5, 6],
]

flat = [x for row in matrix for x in row]
print(flat)
