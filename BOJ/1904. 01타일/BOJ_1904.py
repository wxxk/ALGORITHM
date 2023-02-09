"""
n = 1 : 1(1)
n = 2 : 00 11(2)
n = 3 : 001 100 111(3)
n = 4 : 0000 0011 1001 1100 1111(5)
"""

import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
dp = [0] * 1000001

# dp[0] = 1
dp[1] = 1
dp[2] = 2

# for i in range(3, n+1):
#     dp[i] = dp[i-2] + dp[i-1]
# print(dp[n]%15746)

for i in range(3, n + 1):
    dp[i] = (dp[i - 2] + dp[i - 1]) % 15746

print(dp[n])
