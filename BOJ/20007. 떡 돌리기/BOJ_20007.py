from heapq import heappush, heappop
import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize

n, m, x, y = map(int, input().split())
maps = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    maps[a].append((b, c))
    maps[b].append((a, c))
visited = [INF] * (n)
visited[y] = 0
q = []
heappush(q, (0, y))

while q:
    cost, node = heappop(q)

    for i, j in maps[node]:
        nc = cost + j

        if visited[i] > nc:
            visited[i] = nc
            heappush(q, (nc, i))

for i in range(n):
    if visited[i] > (x / 2):
        print(-1)
        break
else:
    visited.sort()
    cnt = 0
    result = 1
    for i in range(n):
        if cnt + visited[i] > (x / 2):
            result += 1
            cnt = visited[i]
        else:
            cnt += visited[i]
    print(result)
