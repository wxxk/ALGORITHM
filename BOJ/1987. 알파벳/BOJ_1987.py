import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    visited.add(matrix[x][y])
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if matrix[nx][ny] not in visited:
                dfs(nx, ny, cnt + 1)
    visited.remove(matrix[x][y])


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
r, c = map(int, input().split())
matrix = [list(input()) for _ in range(r)]
visited = set()
ans = 0

dfs(0, 0, 1)
print(ans)
