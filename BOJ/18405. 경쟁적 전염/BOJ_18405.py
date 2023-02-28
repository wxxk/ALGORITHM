from collections import deque
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
visited = [[0] * n for _ in range(n)]
q = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] != 0:
            q.append((matrix[i][j], i, j, 0))

q.sort()
q = deque(q)

while q:
    virus, a, b, t = q.popleft()
    visited[a][b] = 1
    if t == s:
        break
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            matrix[nx][ny] = virus
            visited[nx][ny] = 1
            q.append((virus, nx, ny, t + 1))


print(matrix[x - 1][y - 1])
