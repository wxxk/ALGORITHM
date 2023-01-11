import sys
from pprint import pprint

sys.stdin = open("input.txt")
input = sys.stdin.readline

n = 30

dp = [[0, 1, 1], [0, 1, 1]]

for i in range(3, n + 1):
    dp[0].append(dp[0][i - 1] + dp[0][i - 2])
    dp[1].append(dp[0][i] % 12)
print(dp)
