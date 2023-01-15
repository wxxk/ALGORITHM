import sys
from collections import deque

sys.stdin = open("input.txt")
input = sys.stdin.readline


def bfs(a, b):
    queue = deque()
    queue.append((a, b))

    visited[a][b] = True

    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = 1
                    cnt += 1
                    queue.append((nx, ny))

    return cnt


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
count = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            count.append(bfs(i, j))

count.sort()

print(len(count))
for i in count:
    print(i)
