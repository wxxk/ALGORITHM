import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
power = list(map(int, input().split()))
hello = list(map(int, input().split()))

p = [0] + power
h = [0] + hello

dp = [[0 for _ in range(101)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, 101):
        a = p[i]
        b = h[i]
        if a > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - a] + b)

print(dp[n][99])
