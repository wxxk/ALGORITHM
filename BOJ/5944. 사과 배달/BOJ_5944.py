from heapq import heappush, heappop
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(start, visited):
    q = []
    heappush(q, (0, start))
    visited[start] = 0

    while q:
        dis, node = heappop(q)

        for i, j in maps[node]:
            next_dis = dis + j

            if visited[i] > next_dis:
                visited[i] = next_dis
                heappush(q, (next_dis, i))
    return visited


c, p, pb, pa1, pa2 = map(int, input().split())

maps = [[] for _ in range(p + 1)]
visited_1 = [INF] * (p + 1)
visited_2 = [INF] * (p + 1)
visited_3 = [INF] * (p + 1)

for _ in range(c):
    s, e, dis = map(int, input().split())
    maps[s].append((e, dis))
    maps[e].append((s, dis))

dijkstra(pb, visited_1)
dijkstra(pa1, visited_2)
dijkstra(pa2, visited_3)

print(min(visited_1[pa1] + visited_2[pa2], visited_1[pa2] + visited_3[pa1]))
