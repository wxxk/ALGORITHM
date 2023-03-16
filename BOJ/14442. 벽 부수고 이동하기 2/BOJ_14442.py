from collections import deque
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m, k = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[-1 for _ in range(m)] for _ in range(n)] for _ in range(k + 1)]

visited[0][0][0] = 0
q = deque()
q.append((0, 0, 0))

while q:
    z, x, y = q.popleft()
    if x == n - 1 and y == m - 1:
        print(visited[z][x][y] + 1)
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if matrix[nx][ny] == 1 and z < k and visited[z + 1][nx][ny] == -1:
                visited[z + 1][nx][ny] = visited[z][x][y] + 1
                q.append((z + 1, nx, ny))
            elif matrix[nx][ny] == 0 and visited[z][nx][ny] == -1:
                visited[z][nx][ny] = visited[z][x][y] + 1
                q.append((z, nx, ny))
else:
    print(-1)
