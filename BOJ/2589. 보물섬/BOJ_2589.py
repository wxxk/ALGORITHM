from collections import deque
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
matrix = [list(input().strip()) for _ in range(n)]

# 첫 번째 BFS : 가장 먼 거리에 있는 육지 찾기
def bfs(x, y):
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = True
    max_distance = 0

    while q:
        x, y, distance = q.popleft()
        max_distance = max(distance, max_distance)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if matrix[nx][ny] == "L":
                    q.append((nx, ny, distance + 1))
                    visited[nx][ny] = True
    return max_distance


# 모든 육지에서 BFS를 수행하여 가장 긴 거리를 찾는다
result = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == "L":
            visited = [[False] * m for _ in range(n)]
            result = max(result, bfs(i, j))

print(result)
