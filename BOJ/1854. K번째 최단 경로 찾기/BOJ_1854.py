from heapq import heappush, heappop
import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize

n, m, k = map(int, input().split())  # 노드, 엣지, k번째 최단경로
maps = [[] for _ in range(n + 1)]  # 그래프 정보 저장 인접 리스트
visited = [[INF] * (k) for _ in range(n + 1)]  # 방문 리스트

# 인접리스트에 에지 정보 저장
for _ in range(m):
    a, b, c = map(int, input().split())
    maps[a].append((b, c))

pq = [(0, 1)]  # 가중치, 목표 노드
visited[1][0] = 0

while pq:
    cost, node = heappop(pq)  # 거리, 노드 데이터 가져오기

    for nNode, nCost in maps[node]:  # 현재 노드에서 연결된 에지 탐색
        sCost = cost + nCost  # 새로운 총 거리 = 현재 노드의 거리 + 에지 가중치
        if visited[nNode][k - 1] > sCost:  # 새로운 노드의 k번째 거리 > 새로운 총 거리
            visited[nNode][k - 1] = sCost  # k번째 최단 거리를 변경
            visited[nNode].sort()  # 거리 순으로 정렬
            heappush(pq, [sCost, nNode])  # 우선순위 큐에 새로운 데이터 추가

for i in range(1, n + 1):
    if visited[i][k - 1] == INF:
        print(-1)
    else:
        print(visited[i][k - 1])
