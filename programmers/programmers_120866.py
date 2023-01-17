board = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0],
]
n = len(board)
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]
stack = []
cnt = 0

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            stack.append((i, j))

for x, y in stack:
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            board[nx][ny] = 1

for a in range(n):
    for b in range(n):
        if board[a][b] == 0:
            cnt += 1
print(cnt)
