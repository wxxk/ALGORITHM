from heapq import heappush, heappop
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(x):
    q = []
    heappush(q, (0, x))
    visited[x] = 0

    while q:
        dis, node = heappop(q)

        for i in maps[node]:  # i[0]:노드 / i[1]:비용
            next_dis = dis + i[1]

            if visited[i[0]] > next_dis:
                visited[i[0]] = next_dis
                heappush(q, (next_dis, i[0]))


n, m, k, x = map(int, input().split())
maps = [[] for _ in range(n + 1)]
visited = [INF] * (n + 1)
result = []

for _ in range(m):
    start, end = map(int, input().split())
    maps[start].append((end, 1))

dijkstra(x)

for i in range(1, len(visited)):
    if visited[i] == k:
        result.append(i)

if not result:
    print(-1)
else:
    for j in result:
        print(j)
