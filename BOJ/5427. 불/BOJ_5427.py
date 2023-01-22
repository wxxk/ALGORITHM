from collections import deque
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline


t = int(input())

for _ in range(t):
    w, h = map(int, input().split())
    matrix = [list(input().strip()) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    queue = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    flag = False

    for i in range(h):
        for j in range(w):
            if matrix[i][j] == "*":
                queue.append((i, j))

    for i in range(h):
        for j in range(w):
            if matrix[i][j] == "@":
                queue.append((i, j))
                visited[i][j] = 1

                if i == h - 1 or i == 0 or j == w - 1 or j == 0:
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

            if 0 <= nx < h and 0 <= ny < w:
                if (
                    "@" in matrix[x][y]
                    and "*" not in matrix[nx][ny]
                    and matrix[nx][ny] != "#"
                ):
                    if visited[nx][ny] == 0:
                        matrix[nx][ny] = "@"
                        visited[nx][ny] = visited[x][y] + 1
                        if nx == h - 1 or nx == 0 or ny == w - 1 or ny == 0:
                            print(visited[nx][ny])
                            flag = True
                            break
                        queue.append((nx, ny))

                if "*" in matrix[x][y]:
                    if matrix[nx][ny] == "@" or matrix[nx][ny] == ".":
                        matrix[nx][ny] += "*"
                        queue.append((nx, ny))
    if flag == False:
        print("IMPOSSIBLE")
