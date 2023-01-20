from collections import deque
import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
matrix = [list(input().strip()) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
B_po = 0
W_po = 0

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            queue = deque()
            queue.append((i, j))
            cnt = 1

            while queue:
                a, b = queue.popleft()

                for k in range(4):
                    nx = a + dx[k]
                    ny = b + dy[k]

                    if (
                        0 <= nx < m
                        and 0 <= ny < n
                        and matrix[nx][ny] == matrix[i][j]
                        and not visited[nx][ny]
                    ):
                        cnt += 1
                        visited[nx][ny] = True
                        queue.append((nx, ny))

            if matrix[i][j] == "W":
                W_po += cnt**2
            else:
                B_po += cnt**2

print(W_po, B_po)
