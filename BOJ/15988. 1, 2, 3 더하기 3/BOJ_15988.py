import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

t = int(input())
dp = [0, 1, 2, 4]
for _ in range(t):
    n = int(input())

    if n <= 3:
        print(dp[n])
    else:
        for i in range(len(dp), n + 1):
            dp.append((dp[i - 3] + dp[i - 2] + dp[i - 1]) % 1000000009)
        print(dp[n])
