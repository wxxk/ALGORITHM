from heapq import heappush, heappop
import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(start):
    global visited
    q = []
    visited = [INF] * (n + 1)
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


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    maps = [[] for _ in range(n + 1)]
    for i in range(m):
        a, b, c = map(int, input().split())
        maps[a].append((b, c))
        maps[b].append((a, c))
    k = int(input())
    friend = list(map(int, input().split()))
    result = [0] * (n + 1)

    for i in friend:
        dijkstra(i)
        for j in range(len(visited)):
            result[j] += visited[j]

    for i in range(1, n + 1):
        if result[i] == min(result):
            print(i)
            break
