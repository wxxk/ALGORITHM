from collections import deque
import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

M, N = map(int, input().split())
matrix = [list(map(int, input().strip().split())) for _ in range(N)]
queue = deque()

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            queue.append((i, j))

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 0:
            matrix[nx][ny] = matrix[x][y] + 1
            queue.append((nx, ny))

flag = False
day = 0
for a in range(N):
    for b in range(M):
        if matrix[a][b] == 0:
            flag = True
        day = max(day, matrix[a][b])

if flag:
    print(-1)
else:
    print(day - 1)
