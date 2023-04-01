import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize
n, m = map(int, input().split())
matrix = [[INF] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    matrix[a][b] = 1
    matrix[b][a] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = 0
            else:
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

result = []
for i in matrix:
    result.append(sum(i))
print(result.index(min(result)) + 1)
