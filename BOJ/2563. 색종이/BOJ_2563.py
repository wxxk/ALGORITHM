import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())

matrix = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(n):
    y, x = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            if matrix[i][j]:
                continue
            matrix[i][j] = 1

sum_n = 0
for i in matrix:
    sum_n += sum(i)

print(sum_n)
