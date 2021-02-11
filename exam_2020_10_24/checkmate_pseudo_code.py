board = []

# 1. From every cell O(N^3)
for row_index in range(len(board)):
    for column_index in range(len(board[row_index])):
        if board[row_index][column_index] == 'Q':
            # run algorithm from position (row_index, column_index)
            pass

# 2. O(max(N^2, N*queens_count))
queens = []
## O(N^2)
for row_index in range(len(board)):
    for column_index in range(len(board[row_index])):
        if board[row_index][column_index] == 'Q':
            queens.append((row_index, column_index))

## O(N*queens_count)
for queen in queens:
    # run algorithm from position queen
    pass

# 100 000 000op ~ 1s

# 3. Start from the King O(N^2)