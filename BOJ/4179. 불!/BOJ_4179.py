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

flag = False
for i in range(r):
    for j in range(c):
        if matrix[i][j] == "F":
            queue.append((i, j))

for i in range(r):
    for j in range(c):
        if matrix[i][j] == "J":
            queue.append((i, j))
            visited[i][j] = 1

            if i == r - 1 or i == 0 or j == c or j == 0:
                print(visited[i][j])
                flag = True
                break
            else:
                break

while queue:
    x, y = queue.popleft()

    if flag == True:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c:
            if (
                "J" in matrix[x][y]
                and "F" not in matrix[nx][ny]
                and matrix[nx][ny] != "#"
            ):
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    matrix[nx][ny] = "J"

                    if nx == r - 1 or nx == 0 or ny == c - 1 or ny == 0:
                        print(visited[nx][ny])
                        flag = True
                        break
                    queue.append((nx, ny))
            if "F" in matrix[x][y]:
                if matrix[nx][ny] == "J" or matrix[nx][ny] == ".":
                    matrix[nx][ny] += "F"
                    queue.append((nx, ny))

if flag == False:
    print("IMPOSSIBLE")
