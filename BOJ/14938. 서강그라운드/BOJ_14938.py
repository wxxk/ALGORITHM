import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline
INF = sys.maxsize

n, m, r = map(int, input().rstrip().split())
items = list(map(int, input().rstrip().split()))
graph = [[INF] * n for _ in range(n)]

for _ in range(r):
    a, b, l = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = l
    graph[b][a] = l

for i in range(n):
    graph[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

item = 0
for i in range(n):
    temp = 0
    for j in range(n):
        if graph[i][j] <= m:
            temp += items[j]
    item = max(item, temp)

print(item)
