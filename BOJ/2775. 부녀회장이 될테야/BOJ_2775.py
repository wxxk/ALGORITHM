import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

dp = [[0] * 15 for _ in range(15)]

for i in range(15):
    dp[0][i] = i

for i in range(1, 15):
    for j in range(1, 15):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

t = int(input())

for _ in range(t):
    n = int(input())
    k = int(input())
    print(dp[n][k])
