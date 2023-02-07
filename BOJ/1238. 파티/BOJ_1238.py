from heapq import heappush, heappop
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize

n, m, k = map(int, input().split())
maps = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    maps[a].append((b, c))

result = [[]]
answer = []

for i in range(1, n + 1):  # 각 마을에 1명씩 살고있다 => 마을마다 거리
    visited = [INF] * (n + 1)
    visited[i] = 0
    pq = []
    heappush(pq, (0, i))

    while pq:
        dis, node = heappop(pq)

        if dis > visited[node]:
            continue

        for nnode, ndis in maps[node]:
            sdis = ndis + dis
            if visited[nnode] > sdis:
                visited[nnode] = sdis
                heappush(pq, (sdis, nnode))

    result.append(visited)  # 각 마을마다 최단 거리 저장

# print(result)
for i in range(1, n + 1):
    # 가는 거리 + 돌아오는 거리
    answer.append(result[i][k] + result[k][i])

print(max(answer))
