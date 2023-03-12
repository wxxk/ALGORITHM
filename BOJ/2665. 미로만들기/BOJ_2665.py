from heapq import heappush, heappop
import sys

# sys.stdin = open("input.txt")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
matrix = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0] * (n) for _ in range(n)]

q = []
heappush(q, (0, 0, 0))
visited[0][0] = 1

while q:
    cost, x, y = heappop(q)

    if x == n - 1 and y == n - 1:
        print(cost)
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            visited[nx][ny] = 1
            if matrix[nx][ny]:
                heappush(q, (cost, nx, ny))
            else:
                heappush(q, (cost + 1, nx, ny))
