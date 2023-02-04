from heapq import heappop, heappush
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())
matrix = [[] for _ in range(n)]
visited = [INF] * (n)

for i in range(m):
    # 단방향 그래프
    start, end, cost = map(int, input().split())
    matrix[start - 1].append([end - 1, cost])

# 출발, 도착
x, y = map(int, input().split())

queue = []
heappush(queue, [0, x - 1])
visited[x - 1] = 0

while queue:
    cost, x = heappop(queue)

    # 이미 찍힌비용이 더 적은 비용일떄
    if cost > visited[x]:
        continue

    for i in matrix[x]:
        # 다음 비용 계산
        next_cost = cost + i[1]

        if visited[i[0]] > next_cost:
            visited[i[0]] = next_cost
            heappush(queue, [next_cost, i[0]])

print(visited[y - 1])
