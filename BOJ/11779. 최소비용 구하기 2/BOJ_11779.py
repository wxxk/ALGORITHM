from heapq import heappush, heappop
import sys

# sys.stdin = open("input.txt")
INF = sys.maxsize
input = sys.stdin.readline

n = int(input())  # 도시의 개수
m = int(input())  # 버스의 개수
maps = [[] for _ in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    maps[a].append((b, c))

start, end = map(int, input().split())
visited = [INF] * (n + 1)

q = []
heappush(q, (0, start, [start]))
visited[start] = 0

while q:
    cost, node, load = heappop(q)
    if cost > visited[node]:
        continue

    if node == end:
        print(cost)
        print(len(load))
        print(*load)
        break

    for x, y in maps[node]:
        next_cost = cost + y
        next_load = load + [x]
        if visited[x] > next_cost:
            visited[x] = next_cost
            heappush(q, (next_cost, x, next_load))
