import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m, k = map(int, input().split())
matrix = [[0] * (m) for _ in range(n)]
visited = [[False] * (m * 1) for _ in range(n)]
max_cnt = 0
# print(visited)

for _ in range(k):
    r, c = map(int, input().split())
    matrix[r - 1][c - 1] = 1

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            cnt = 0
            visited[i][j] = True
            stack = []
            stack.append((i, j))

            while stack:
                cnt += 1
                a, b = stack.pop()

                for k in range(4):
                    nx = a + dx[k]
                    ny = b + dy[k]

                    if (
                        0 <= nx < n
                        and 0 <= ny < m
                        and matrix[nx][ny] == 1
                        and not visited[nx][ny]
                    ):
                        visited[nx][ny] = 1
                        stack.append((nx, ny))
            max_cnt = max(max_cnt, cnt)

print(max_cnt)
