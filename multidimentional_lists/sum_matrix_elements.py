def read_matrix(is_test=False):
    if is_test:
        return [
            [7, 1, 3, 3, 2, 1],
            [1, 3, 9, 8, 5, 6],
            [4, 6, 7, 9, 1, 0],
        ]
    else:
        (rows_count, columns_count) = map(int, input().split(', '))
        matrix = []
        for row_index in range(rows_count):
            # row = list(map(int, input().split(', ')))
            row = [int(x) for x in input().split(', ')]
            matrix.append(row)

        return matrix
        # Don't do this:
        # return [list(map(int, input().split(', '))) for _ in range(rows_count)]


matrix = read_matrix()

matrix_sum = 0

for r in range(len(matrix)):
    row = matrix[r]
    for c in range(len(row)):
        matrix_sum += row[c]
    # matrix_sum += sum(row)

print(matrix_sum)
print(matrix)
