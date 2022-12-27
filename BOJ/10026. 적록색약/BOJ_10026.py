import sys

sys.stdin = open("input.txt")

from collections import deque

n = int(input())
matrix = [list(input()) for _ in range(n)]
visited_1 = [[False] * n for _ in range(n)]
visited_2 = [[False] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt_1 = 0
cnt_2 = 0

for i in range(n):
    for j in range(n):
        if not visited_1[i][j]:
            q = deque()
            q.append((i, j))
            visited_1[i][j] = True

            while q:
                a, b = q.popleft()

                for k in range(4):
                    nx = a + dx[k]
                    ny = b + dy[k]

                    if 0 <= nx < n and 0 <= ny < n and not visited_1[nx][ny]:
                        if matrix[i][j] == "R" or matrix[i][j] == "G":
                            if matrix[nx][ny] == "R" or matrix[nx][ny] == "G":
                                q.append((nx, ny))
                                visited_1[nx][ny] = True
                        if matrix[i][j] == "B" and matrix[nx][ny] == "B":
                            q.append((nx, ny))
                            visited_1[nx][ny] = True
            cnt_1 += 1

        if not visited_2[i][j]:
            q = deque()
            q.append((i, j))
            visited_2[i][j] = True

            while q:
                a, b = q.popleft()
                for k in range(4):
                    nx = a + dx[k]
                    ny = b + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and not visited_2[nx][ny]:
                        if matrix[i][j] == matrix[nx][ny]:
                            q.append((nx, ny))
                            visited_2[nx][ny] = True
            cnt_2 += 1

print(cnt_2, cnt_1)
