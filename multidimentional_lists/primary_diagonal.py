def read_matrix(is_test=False):
    if is_test:
        return [
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, -12],
        ]
    else:
        size = int(input())
        matrix = []
        for row_index in range(size):
            row = [int(x) for x in input().split(' ')]
            matrix.append(row)

        return matrix


def get_sum_of_primary_diagonal(matrix):
    diagonal_sum = 0
    for i in range(len(matrix)):
        diagonal_sum += matrix[i][i]
    return diagonal_sum


def get_sum_below_primary_diagonal_1(matrix):
    the_sum = 0
    size = len(matrix)
    for r in range(size):
        for c in range(size):
            if c <= r:  # including main diagonal
                # if c < r:  # excluding main diagonal
                the_sum += matrix[r][c]
    return the_sum


def get_sum_below_primary_diagonal_2(matrix):
    the_sum = 0
    size = len(matrix)
    for r in range(size):
        for c in range(size):
            if r < c:  # including main diagonal
                # if r <= c:  # excluding main diagonal
                break

            the_sum += matrix[r][c]
    return the_sum


def get_sum_below_primary_diagonal_3(matrix):
    the_sum = 0
    size = len(matrix)
    for r in range(size):
        for c in range(r + 1):  # including main diagonal
            # for c in range(r): # excluding main diagonal
            the_sum += matrix[r][c]
    return the_sum


def get_sum_above_primary_diagonal(matrix):
    the_sum = 0
    size = len(matrix)
    for r in range(size):
        for c in range(r, size):  # including main diagonal
            # for c in range(r+1, size): # excluding main diagonal
            the_sum += matrix[r][c]
    return the_sum


def get_sum_of_secondary_diagonal(matrix):
    diagonal_sum = 0
    size = len(matrix)
    for i in range(size):
        diagonal_sum += matrix[i][size - i - 1]
    return diagonal_sum


print(get_sum_of_primary_diagonal(read_matrix()))
# print(get_sum_below_primary_diagonal_1(read_matrix(is_test=True)))
# print(get_sum_below_primary_diagonal_2(read_matrix(is_test=True)))
# print(get_sum_below_primary_diagonal_3(read_matrix(is_test=True)))
# print(get_sum_above_primary_diagonal(read_matrix(is_test=True)))
# print(get_sum_of_secondary_diagonal(read_matrix(is_test=True)))
