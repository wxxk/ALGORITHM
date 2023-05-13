from heapq import heappop, heappush
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())  # 감방의 수
e = int(input())  # 출구 번호
t = int(input())  # 카운트 타운
m = int(input())  # 감옥에 있는 연결 수

matrix = [[] for _ in range(n)]
visited = [INF] * (n)
cnt = 0

for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    matrix[a].append((b, c))

visited[e] = 0
q = []
heappush(q, (e, 0))

while q:
    node, dis = heappop(q)

    if dis > visited[node]:
        continue

    for n, d in matrix[node]:
        nd = dis + d
        if visited[n] > nd:
            visited[n] = nd
            heappush(q, (n, nd))


for v in visited:
    if 0 <= v <= t:
        cnt += 1

print(cnt)
