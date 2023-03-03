from heapq import heappush, heappop
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize


def dij(start):
    visited = [INF] * (v + 1)
    visited[start] = 0
    q = []
    heappush(q, (0, start))

    while q:
        cost, node = heappop(q)

        if cost > visited[node]:
            continue

        for i, j in maps[node]:
            nx = cost + j

            if visited[i] > nx:
                visited[i] = nx
                heappush(q, (nx, i))
    return visited


n, v, e = map(int, input().split())
a, b = map(int, input().split())
h = list(map(int, input().split()))
maps = [[] for _ in range(v + 1)]
for _ in range(e):
    x, y, z = map(int, input().split())
    maps[x].append((y, z))
    maps[y].append((x, z))

visited_a = dij(a)
visited_b = dij(b)
answer = 0

for i in h:
    dist_a = visited_a[i]
    dist_b = visited_b[i]

    if dist_a == INF:
        answer -= 1
    else:
        answer += dist_a

    if dist_b == INF:
        answer -= 1
    else:
        answer += dist_b


print(answer)
