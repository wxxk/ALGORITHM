import sys
from collections import deque

# sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
m = int(input())

matrix = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

q = deque()
q.append((1, 0))
visited[1] = 1
cnt = 0

while q:
    cur, dis = q.popleft()
    if dis <= 2:
        cnt += 1

    for i in matrix[cur]:
        if not visited[i]:
            visited[i] = 1
            q.append((i, dis + 1))

print(cnt - 1)
