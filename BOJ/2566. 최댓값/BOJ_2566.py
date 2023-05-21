import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

n, m = 9, 9
matrix = [list(map(int, input().split())) for _ in range(n)]

max_num = -1
x, y = 0, 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] > max_num:
            max_num = matrix[i][j]
            x, y = i, j

print(max_num)
print(x + 1, y + 1)
