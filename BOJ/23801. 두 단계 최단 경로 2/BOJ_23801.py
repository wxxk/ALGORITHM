from heapq import heappush, heappop
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(start):
    visited = [INF for _ in range(n + 1)]
    visited[start] = 0
    q = []
    heappush(q, (0, start))

    while q:
        cost, node = heappop(q)

        if cost > visited[node]:
            continue

        for i, j in maps[node]:
            nc = cost + i

            if visited[j] > nc:
                visited[j] = nc
                heappush(q, (nc, j))
    return visited


n, m = map(int, input().split())
maps = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    maps[u].append((w, v))
    maps[v].append((w, u))
x, z = map(int, input().split())
p = int(input())
y = list(map(int, input().split()))

visited_x = dijkstra(x)  # 출발정점에서 p개의 중간 정점까지 최소거리 구하기
# p개의 중간 정점에서 z까지 각각의 거리를 구하면 다익스트라를 p번 사용하는 것이기 때문에 많은시간이 소요
# z에서 p로가는 다익스트라를 구하면 한번만 사용하면된다.
visited_y = dijkstra(z)

result = INF
for i in y:
    # p점에 대해 최솟값 찾기기
    result = min(visited_x[i] + visited_y[i], result)

print(-1 if result == INF else result)
