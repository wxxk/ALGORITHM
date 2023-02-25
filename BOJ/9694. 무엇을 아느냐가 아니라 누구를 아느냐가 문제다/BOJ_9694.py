from heapq import heappush, heappop
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize

t = int(input())

for i in range(1, t + 1):
    n, m = map(int, input().split())
    maps = [[] for _ in range(m)]
    visited = [INF] * m

    for _ in range(n):
        x, y, z = map(int, input().split())
        maps[x].append((y, z))
        maps[y].append((x, z))

    q = []
    heappush(q, (0, 0, [0]))
    visited[0] = 0

    print(f"Case #{i}:", end=" ")

    while q:
        cost, node, load = heappop(q)

        if node == m - 1:
            print(*load)
            break

        if cost > visited[node]:
            continue

        for N, C in maps[node]:
            next_cost = cost + C
            next_load = load + [N]

            if visited[N] > next_cost:
                visited[N] = next_cost
                heappush(q, (next_cost, N, next_load))

    else:
        print(-1)
