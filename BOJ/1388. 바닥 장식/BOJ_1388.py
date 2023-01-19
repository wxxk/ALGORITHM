import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]
visited = [[False] * (M) for _ in range(N)]
cnt = 0
dx = [0, 1]
dy = [1, 0]

for i in range(N):
    for j in range(M):
        if matrix[i][j] == "-" and not visited[i][j]:
            cnt += 1
            visited[i][j] = True
            stack = []
            stack.append((i, j))

            while stack:
                a, b = stack.pop()

                nx = a + dx[0]
                ny = b + dy[0]

                if (
                    0 <= nx < N
                    and 0 <= ny < M
                    and matrix[nx][ny] == "-"
                    and not visited[nx][ny]
                ):
                    visited[nx][ny] = True
                    stack.append((nx, ny))

        if matrix[i][j] == "|" and not visited[i][j]:
            cnt += 1
            visited[i][j] = True
            stack = []
            stack.append((i, j))

            while stack:
                a, b = stack.pop()

                nx = a + dx[1]
                ny = b + dy[1]

                if (
                    0 <= nx < N
                    and 0 <= ny < M
                    and matrix[nx][ny] == "|"
                    and not visited[nx][ny]
                ):
                    visited[nx][ny] = True
                    stack.append((nx, ny))

print(cnt)
