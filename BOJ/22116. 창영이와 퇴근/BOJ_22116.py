from heapq import heappush, heappop
import sys

# sys.stdin = open("input.txt")
INF = sys.maxsize

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[INF] * (n) for _ in range(n)]
q = []
heappush(q, (0, 0, 0))
while q:
    cost, x, y = heappop(q)
    if visited[x][y] != INF:
        continue
    if x == n - 1 and y == n - 1:
        print(cost)
        break
    visited[x][y] = cost
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] != INF:
                continue
            heappush(q, (max(abs(matrix[x][y] - matrix[nx][ny]), cost), nx, ny))
