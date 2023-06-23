import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

a, b = [], []

n, m = map(int, input().split())

for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

for i in range(n):
    row = list(map(int, input().split()))
    b.append(row)

for i in range(n):
    for j in range(m):
        print(a[i][j] + b[i][j], end=" ")
    print()
