import sys

input = sys.stdin.readline

n, t = map(int, input().split())

dp = [[0 for _ in range(t + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    k, s = map(int, input().split())  # k = 예상공부 시간, s = 배점
    for j in range(1, t + 1):
        if k > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - k] + s)

print(dp[-1][-1])
