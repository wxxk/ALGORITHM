import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]

for i in range(1, k + 1):
    im, ti = map(int, input().split())

    for j in range(1, n + 1):
        if ti > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - ti] + im)

print(dp[-1][-1])
