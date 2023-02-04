from heapq import heappop, heappush
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().split())
k = int(input()) - 1
maps = [[] for _ in range(v)]
visited = [INF] * v

for i in range(e):
    u, v, w = map(int, input().split())
    maps[u - 1].append([v - 1, w])

queue = []
heappush(queue, [0, k])
visited[k] = 0

while queue:
    cost, x = heappop(queue)

    if cost > visited[x]:
        continue

    for i, j in maps[x]:
        next_cost = cost + j

        if visited[i] > next_cost:
            visited[i] = next_cost
            heappush(queue, [next_cost, i])

for ans in visited:
    if ans == INF:
        print("INF")
    else:
        print(ans)
