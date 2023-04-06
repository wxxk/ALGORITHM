import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
graph = [[INF] * (n) for _ in range(n)]

result = []

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    else:
        graph[a - 1][b - 1] = 1
        graph[b - 1][a - 1] = 1

for i in range(n):
    graph[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(n):
    mv = 0
    for j in range(n):
        mv = max(mv, graph[i][j])
    result.append(mv)

print(min(result), result.count(min(result)))

for i in range(len(result)):
    if result[i] == min(result):
        print(i + 1, end=" ")
