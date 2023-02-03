from heapq import heappush, heappop
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(n)]
visited = [[INF] * m for _ in range(n)]
start = []
heappush(start, (matrix[0][0], 0, 0))
visited[0][0] = matrix[0][0]

while start:
    cost, x, y = heappop(start)

    if x == n - 1 and y == m - 1:
        print(visited[x][y])

    if cost > visited[x][y]:
        continue

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            next_cost = cost + matrix[nx][ny]
            if visited[nx][ny] > next_cost:
                visited[nx][ny] = next_cost
                heappush(start, (next_cost, nx, ny))
