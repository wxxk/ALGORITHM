from heapq import heappush, heappop
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(start, end, center):
    visited = [INF] * (n + 1)
    visited[start] = 0
    q = []
    heappush(q, (0, start))

    while q:
        cost, node = heappop(q)
        if cost > visited[node]:
            continue

        for i, j in maps[node]:  # i : 도시, j : 비용
            nc = cost + j
            if i != center:
                if visited[i] > nc:
                    visited[i] = nc
                    heappush(q, (nc, i))
    return visited[end]


n, m = map(int, input().split())
maps = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    maps[u].append((v, w))
x, y, z = map(int, input().split())

# 중간 정점을 거치는 경우
visited_1 = dijkstra(x, y, 0)
visited_2 = dijkstra(y, z, 0)

if visited_1 == INF or visited_2 == INF:
    result_1 = -1
else:
    result_1 = visited_1 + visited_2


# 바로 가는 경우(Y를 거치지 않고 가야함)
result_2 = dijkstra(x, z, y)

if result_2 == INF:
    result_2 = -1

print(result_1, result_2)
