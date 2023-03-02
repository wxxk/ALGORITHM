from heapq import heappush, heappop
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
friend = list(map(int, input().split()))  # a, b, c 가 사는 위치
m = int(input())
maps = [[] for _ in range(n + 1)]
for _ in range(m):
    d, e, l = map(int, input().split())
    maps[d].append((e, l))
    maps[e].append((d, l))
visited = [INF] * (n + 1)
q = []

for i in friend:
    # 친구 집에서 각 지점의 최단거리를 구한다.
    heappush(q, (0, i))

while q:
    cost, node = heappop(q)

    for i, j in maps[node]:
        nx = cost + j

        if visited[i] > nx:
            visited[i] = nx
            heappush(q, (nx, i))

temp = 0
answer = 0

for i in range(1, len(visited)):
    if visited[i] > temp:
        temp = visited[i]
        answer = i

print(answer)
