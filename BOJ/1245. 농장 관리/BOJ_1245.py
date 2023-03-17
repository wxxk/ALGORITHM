from collections import deque
import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    global flag

    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if matrix[x][y] < matrix[nx][ny]:
                    flag = False
                if matrix[nx][ny] == matrix[x][y] and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * (m + 1) for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] > 0 and not visited[i][j]:
            flag = True
            bfs(i, j)

            if flag:
                cnt += 1

print(cnt)
