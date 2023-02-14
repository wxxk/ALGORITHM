from heapq import heappush, heappop
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(start):
    q = []
    heappush(q, (0, start))
    visited[start] = 0

    while q:
        dis, now = heappop(q)

        if dis > visited[now]:
            continue

        for N, D in maps[now]:
            next_dis = dis + D

            if visited[N] > next_dis:
                visited[N] = next_dis
                heappush(q, (next_dis, N))


n, d = map(int, input().split())
maps = [[] for _ in range(d + 1)]
visited = [INF] * (d + 1)

# 거리 비용 1로 초기화
for i in range(d):
    maps[i].append((i + 1, 1))

for _ in range(n):
    s, e, dis = map(int, input().split())
    if e > d:
        continue
    maps[s].append((e, dis))

dijkstra(0)

print(visited[d])
