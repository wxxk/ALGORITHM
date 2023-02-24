from heapq import heappush, heappop
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
ward = list(map(int, input().split()))
maps = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    maps[a].append((b, c))
    maps[b].append((a, c))
visited = [INF] * (n)
ward[-1] = 0
visited[0] = 0
q = []
heappush(q, (0, 0))

while q:
    cost, node = heappop(q)

    if cost > visited[node]:
        continue

    for i, j in maps[node]:
        next_cost = cost + j

        if visited[i] > next_cost and ward[i] == 0:
            visited[i] = next_cost
            heappush(q, (next_cost, i))

print(visited[-1] if visited[-1] < INF else -1)
