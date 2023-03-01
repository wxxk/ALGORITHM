from heapq import heappush, heappop
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize

n, m, k = map(int, input().split())
maps = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, c = map(int, input().split())
    maps[v].append((c, u))  # 면접지를 출발지로 두고 각 집의 거리로 구하기
k_list = list(map(int, input().split()))

q = []
visited = [INF] * (n + 1)

for i in k_list:
    visited[i] = 0
    heappush(q, (0, i))  # 다같이 돌려도 가까운 면접장으로 가게된다.

while q:
    cost, node = heappop(q)

    if cost > visited[node]:
        continue

    for i, j in maps[node]:
        next_cost = cost + i

        if visited[j] > next_cost:
            visited[j] = next_cost
            heappush(q, (next_cost, j))

result = 0
max_dis = 0

for i in range(1, len(visited)):
    if visited[i] > result:
        result = visited[i]
        num = i
print(num)
print(result)
