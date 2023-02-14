from heapq import heappop, heappush
import sys

# sys.stdin = open("input.txt")
INF = sys.maxsize


def dijkstra(start):
    q = []
    heappush(q, (0, start))
    visited[start] = 0

    while q:
        cost, now = heappop(q)

        if cost > visited[now]:
            continue

        for N, C in maps[now]:
            next_cost = cost + C

            if visited[N] > next_cost:
                visited[N] = next_cost
                heappush(q, (next_cost, N))


n, m = map(int, input().split())
maps = [[] for _ in range(n + 1)]
visited = [INF] * (n + 1)

for _ in range(m):
    s, e, cost = map(int, input().split())
    maps[s].append((e, cost))
    maps[e].append((s, cost))

dijkstra(1)
print(visited[-1])
