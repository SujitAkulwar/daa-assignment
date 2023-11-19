n = 4
board = [[ 0 for i in range(n)] for i in range(n)]

def safe(r, c):
    for i in range(r):
        if board[i][c] == 1:
            return False
    for i, j in zip(range(r, -1, -1), range(c, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(r, -1, -1), range(c, n)):
        if board[i][j] == 1:
            return False
    return True

def solve(r, c):
    if r == n:
        return [row[:] for row in board]  # Return a copy of the board

    for c in range(n):
        if safe(r, c):
            board[r][c] = 1
            result = solve(r + 1, c)
            if result:  # Check if a solution is found
                return result
            board[r][c] = 0

solution = solve(0, 0)
if solution:
    for i in range(n):
      print(board[i])
else:
    print("No solution found.")