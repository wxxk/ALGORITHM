import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
tri = []

for _ in range(n):
    tri.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(0, i + 1):
        if j == 0:
            tri[i][0] += tri[i - 1][0]
        elif i == j:
            tri[i][j] += tri[i - 1][j - 1]
        else:
            tri[i][j] += max(tri[i - 1][j - 1], tri[i - 1][j])

print(max(tri[n - 1]))
