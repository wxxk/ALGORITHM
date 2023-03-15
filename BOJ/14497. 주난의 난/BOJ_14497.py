from heapq import heappush, heappop
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize


def bfs(x, y):
    q = []
    heappush(q, (1, x, y))
    visited[x][y] = 1

    while q:
        cost, x, y = heappop(q)
        if cost > visited[x][y]:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == "0" and visited[nx][ny] > cost:
                    heappush(q, (cost, nx, ny))
                    visited[nx][ny] = cost
                elif matrix[nx][ny] == "1" and visited[nx][ny] > cost + 1:
                    heappush(q, (cost + 1, nx, ny))
                    visited[nx][ny] = cost + 1
                elif matrix[nx][ny] == "#":
                    return cost


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
matrix = [list(map(str, input().strip())) for _ in range(n)]
visited = [[INF] * m for _ in range(n)]

print(bfs(x1 - 1, y1 - 1))
