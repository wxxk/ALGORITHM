import sys

sys.stdin = open("input.txt")

input = sys.stdin.readline

T = int(input())

for t in range(T):
    dp = [0, 1, 2, 4]
    n = int(input())

    for i in range(4, n + 1):
        dp.append(dp[i - 3] + dp[i - 2] + dp[i - 1])

    print(dp[n])
