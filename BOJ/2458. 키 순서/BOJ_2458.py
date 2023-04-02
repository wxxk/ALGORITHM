import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    matrix[a][b] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if matrix[i][k] and matrix[k][j]:
                matrix[i][j] = 1

result = 0
for i in range(n):
    temp = 0
    for j in range(n):
        temp += matrix[i][j] + matrix[j][i]
    if temp == (n - 1):
        result += 1
print(result)
