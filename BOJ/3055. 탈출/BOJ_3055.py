from collections import deque
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

r, c = map(int, input().split())
matrix = [list(input().strip()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
queue = deque()

for i in range(r):
    for j in range(c):
        if matrix[i][j] == "*":
            queue.append((i, j))

for i in range(r):
    for j in range(c):
        if matrix[i][j] == "S":
            queue.append((i, j))

flag = False
while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c:
            if (
                "S" in matrix[x][y]
                and "*" not in matrix[nx][ny]
                and matrix[nx][ny] != "X"
            ):
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    if matrix[nx][ny] == "D":
                        print(visited[nx][ny])
                        flag = True
                        break
                    matrix[nx][ny] = "S"
                    queue.append((nx, ny))

            if "*" in matrix[x][y]:
                if matrix[nx][ny] == "." or matrix[nx][ny] == "S":
                    matrix[nx][ny] += "*"
                    queue.append((nx, ny))
if not flag:
    print("KAKTUS")
