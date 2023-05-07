import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    matrix[a][b] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = 0

            elif matrix[i][k] and matrix[k][j]:
                matrix[i][j] = 1

answer = 0
for i in range(n):
    max_num = 0
    min_num = 0
    for j in range(n):
        max_num += matrix[i][j]
        min_num += matrix[j][i]

    if max_num >= (n / 2) or min_num >= (n / 2):
        answer += 1

print(answer)
