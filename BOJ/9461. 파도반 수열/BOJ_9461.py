import sys

sys.stdin = open("input.txt")

t = int(input())

for i in range(t):
    n = int(input())
    dp = [0] * 101

    # dp[1], dp[2], dp[3], dp[4], dp[5] = 1, 1, 1, 2, 2

    # dp[6] = dp[3] + dp[5]
    # dp[7] = dp[2] + dp[6]
    # dp[8] = dp[1] + dp[7]

    # for j in range(8, n + 1):
    #     dp[j] = dp[j - 5] + dp[j - 1]

    for i in range(1, 4):
        dp[i] = 1

    for j in range(4, n + 1):
        dp[j] = dp[j - 3] + dp[j - 2]

    print(dp[n])
