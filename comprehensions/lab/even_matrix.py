def strs_to_ints(strs):
    return [int(x) for x in strs]


def read_matrix():
    rows_counts = int(input())
    return [strs_to_ints(input().split(', ')) for _ in range(rows_counts)]


def is_even(x):
    return x % 2 == 0


def get_even(values):
    return [x for x in values if is_even(x)]


def get_even_matrix(matrix):
    return [get_even(row) for row in matrix]


def print_result(matrix):
    print(matrix)


matrix = read_matrix()
even_matrix = get_even_matrix(matrix)
print_result(even_matrix)
