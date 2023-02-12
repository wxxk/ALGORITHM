from collections import deque

# import sys

# sys.stdin = open("input.txt")
# input = sys.stdin.readline

n = int(input())
matrix = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    s, e = map(int, input().split())
    matrix[s].append(e)
    matrix[e].append(s)

queue = deque()
queue.append(1)
visited[1] = True

while queue:
    x = queue.popleft()
    for i in matrix[x]:
        if not visited[i]:
            result[i] = x
            queue.append(i)
            visited[i] = True

for i in range(2, n + 1):
    print(result[i])
