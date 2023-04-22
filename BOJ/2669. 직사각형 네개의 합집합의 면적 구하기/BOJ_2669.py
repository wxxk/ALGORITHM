import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline

matrix = [[0] * 101 for _ in range(101)]
ans = 0
for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            if not matrix[i][j]:
                matrix[i][j] = 1

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j]:
            ans += 1

print(ans)
