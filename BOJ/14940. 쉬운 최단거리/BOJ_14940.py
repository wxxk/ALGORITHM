from collections import deque
import sys

# sys.stdin = open("input.txt")

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# n 세로 / m 가로
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
queue = deque()

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            queue.append((i, j))
            visited[i][j] = 0

            while queue:
                x, y = queue.popleft()

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < n and 0 <= ny < m:
                        if visited[nx][ny] == -1 and matrix[nx][ny] == 1:
                            visited[nx][ny] = visited[x][y] + 1
                            queue.append((nx, ny))
        elif matrix[i][j] == 0:
            visited[i][j] = 0

for i in visited:
    print(*i)
