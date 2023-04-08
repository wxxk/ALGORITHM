import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())

graph = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

result = []
for i in range(n):
    count = 0
    for j in range(n):
        if not graph[i][j] and not graph[j][i]:
            count += 1
    result.append(count - 1)

print(*result)
