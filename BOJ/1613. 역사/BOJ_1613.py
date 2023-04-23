import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

n, k = map(int, input().split())

matrix = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(k):
    b, a = map(int, input().split())
    b -= 1
    a -= 1
    matrix[b][a] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if matrix[i][k] and matrix[k][j]:
                matrix[i][j] = 1

s = int(input())
for _ in range(s):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if matrix[x][y] == 1:
        print(-1)
    elif matrix[y][x] == 1:
        print(1)
    elif matrix[x][y] == 0:
        print(0)
