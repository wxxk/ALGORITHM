import sys
from collections import deque

# sys.stdin = open("input.txt")
input = sys.stdin.readline

m, n, h = map(int, input().split())
matrix = [[list(map(int, input().split())) for _ in range(n)] for i in range(h)]
visited = [[[False] * m for _ in range(n)] for _ in range(h)]

queue = deque()

dx = [-1, 1, 0, 0, 0, 0]  # 높이
dy = [0, 0, -1, 1, 0, 0]  # 세로
dz = [0, 0, 0, 0, -1, 1]  # 가로

for i in range(h):  # 높이
    for j in range(n):  # 세로
        for k in range(m):  # 가로
            if matrix[i][j][k] == 1:
                queue.append((i, j, k))
                visited[i][j][k] = 1
while queue:
    x, y, z = queue.popleft()

    for i in range(6):
        nx = x + dx[i]  # 높이
        ny = y + dy[i]  # 세로
        nz = z + dz[i]  # 가로

        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
            if matrix[nx][ny][nz] == 0 and not visited[nx][ny][nz]:
                visited[nx][ny][nz] = True
                matrix[nx][ny][nz] = matrix[x][y][z] + 1
                queue.append((nx, ny, nz))

flag = False
result = 0

for i in range(h):
    for j in range(n):
        for k in range(m):
            if matrix[i][j][k] == 0:
                flag = True
            elif matrix[i][j][k] > result:
                result = matrix[i][j][k]
# if flag:
#     print(-1)
# else:
#     print(result - 1)

print(result - 1 if not flag else -1)
