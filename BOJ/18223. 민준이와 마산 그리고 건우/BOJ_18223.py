from heapq import heappush, heappop
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(start):
    visited = [INF] * (v + 1)
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
    return visited


v, e, p = map(int, input().split())
maps = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    maps[a].append((b, c))
    maps[b].append((a, c))

v1 = dijkstra(1)
v2 = dijkstra(p)

# if v1[v] == v1[p] + v2[v]:
#     print("SAVE HIM")
# else:
#     print("GOOD BYE")

print("SAVE HIM" if v1[v] == v1[p] + v2[v] else "GOOD BYE")
