ll = [1, 2, 3, 4, 5]

matrix = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
]

print(matrix)
print(matrix[1][2])

rows_count = 3
columns_count = 2

# matrix = []
# for row_index in range(rows_count):
#     row = []
#     for column_index in range(columns_count):
#         row.append(0)
#     matrix.append(row)
#
# print(matrix)

matrix = [[0] * columns_count for _ in range(rows_count)]
print(matrix)
