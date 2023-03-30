import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().strip().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if matrix[i][k] and matrix[k][j]:
                matrix[i][j] = 1

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()
