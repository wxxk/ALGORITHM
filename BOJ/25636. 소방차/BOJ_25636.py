from heapq import heappop, heappush
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
w = list(map(int, input().split()))
m = int(input())

matrix = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    matrix[a].append((c, b))
    matrix[b].append((c, a))
s, t = map(int, input().split())
s -= 1
t -= 1

visited = [INF] * n
water = [0] * n
visited[s] = 0
water[s] = w[s]  # 시작지점의 물 충전

hq = []
heappush(hq, (0, s))  # 거리, 시작지점

while hq:
    cur_dist, cur_node = heappop(hq)

    # 현재 거리가 방문리스트의 현재 거리보다 크다면
    # 최소 거리가 아니기 때문에 무시
    if cur_dist > visited[cur_node]:
        continue

    for next_cost, next_node in matrix[cur_node]:
        next_dist = next_cost + cur_dist
        if visited[next_node] > next_dist:
            visited[next_node] = next_dist
            water[next_node] = (
                w[next_node] + water[cur_node]
            )  # 다음 노드에서 충전한 물과 현재까지 충전한 물을 저장
            heappush(hq, (next_dist, next_node))

        elif next_dist == visited[next_node]:  # 거리가 같을 경우
            # 현재까지 충전한 물과 다음 노드에서 충전한 물의 합 중 큰 값 저장
            water[next_node] = max(water[next_node], w[next_node] + water[cur_node])

if visited[t] == INF:
    print(-1)
else:
    print(visited[t], water[t])
