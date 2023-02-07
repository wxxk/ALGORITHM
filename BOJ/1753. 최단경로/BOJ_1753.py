from heapq import heappop, heappush
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().split())
k = int(input()) - 1
maps = [[] for _ in range(v)]
visited = [INF] * v

# 인접리스트에 에지 정보 저장
for i in range(e):
    u, v, w = map(int, input().split())
    maps[u - 1].append([v - 1, w])

# 다익스트라 함수 구현
# 출발노드를 우선순위 큐에 넣고 시작
queue = []
heappush(queue, [0, k])
visited[k] = 0


while queue:  # 큐가 빌 때까지
    cost, x = heappop(queue)

    if cost > visited[x]:
        continue

    for i, j in maps[x]:
        # 현재 선택 노드 최단거리 + 비용
        next_cost = cost + j

        # 현재 노드를 방문 전 / 현재 선택 노드 최단거리 + 비용 < 타깃 노드의 최단 거리
        if visited[i] > next_cost:
            # 타깃 노드 최단 거리 업데이트
            visited[i] = next_cost
            # 우선순위 큐에 타깃 노드 추가
            heappush(queue, [next_cost, i])

for ans in visited:
    if ans == INF:
        print("INF")
    else:
        print(ans)
