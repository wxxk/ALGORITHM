from heapq import heappop, heappush
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(start):
    q = []
    heappush(q, (0, start))
    visited[start] = 0

    while q:
        cost, node = heappop(q)

        for i, j in maps[node]:
            next_cost = cost + j

            if visited[i] > next_cost:
                visited[i] = next_cost
                heappush(q, (next_cost, i))


n, m = map(int, input().split())
maps = [[] for _ in range(n + 1)]
visited = [INF] * (n + 1)
for i in range(m):
    a, b, c = map(int, input().split())
    maps[a].append((b, c))
    maps[b].append((a, c))
s, t = map(int, input().split())

dijkstra(s)

print(visited[t])
