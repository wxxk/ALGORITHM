from heapq import heappush, heappop
import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline
INF = sys.maxsize


def dijk(start):
    dist[start] = 0
    q = []
    heappush(q, (0, start))

    while q:
        cost, now = heappop(q)

        if dist[now] < cost:
            continue

        for time, node in graph[now]:
            next_cost = cost + time

            if dist[node] > next_cost:
                dist[node] = next_cost
                heappush(q, (next_cost, node))

    return dist


n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dist = [INF] * (n + 1)

for _ in range(m):
    a, b, t = map(int, input().split())

    graph[a].append((t, b))
    graph[b].append((t, a))

dijk(x)

answer = 0

for i in range(1, n + 1):
    answer = max(answer, dist[i])

print(answer * 2)
