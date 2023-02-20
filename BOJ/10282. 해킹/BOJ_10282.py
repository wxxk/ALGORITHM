from heapq import heappush, heappop
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize

t = int(input())
for _ in range(t):
    n, d, c = map(int, input().split())
    maps = [[] for _ in range(n + 1)]
    visited = [INF] * (n + 1)
    for i in range(d):
        a, b, s = map(int, input().split())
        maps[b].append((a, s))

    q = []
    heappush(q, (0, c))
    visited[c] = 0

    while q:
        cost, node = heappop(q)

        if cost > visited[node]:
            continue

        for i, j in maps[node]:
            next_cost = cost + j

            if visited[i] > next_cost:
                visited[i] = next_cost
                heappush(q, (next_cost, i))
    cnt = 0
    result = 0
    for i in visited:
        if i != INF:
            cnt += 1
            result = max(result, i)
    print(cnt, result)
