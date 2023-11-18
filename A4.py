def is_safe(board, row, col, n):
    # Check if there is a Queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a Queen in the left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a Queen in the right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row, n):
    if row == n:
        # All Queens are placed, print the board
        for i in range(n):
            print(board[i])
        print()
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            # Place Queen and move to the next row
            board[row][col] = 1
            solve_n_queens(board, row + 1, n)
            # Backtrack: remove the Queen if the current placement does not lead to a solution
            board[row][col] = 0

# Example: Solve 4-Queens problem with the first Queen placed in the first row and second column
n = 4
board = [[0] * n for _ in range(n)]
board[0][1] = 1  # Placing the first Queen
solve_n_queens(board, 1, n)
