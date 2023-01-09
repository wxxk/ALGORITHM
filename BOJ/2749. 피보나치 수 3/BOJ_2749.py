import sys

sys.stdin = open("input.txt")

n = int(input())

mod = 1000000
fibo = 15 * mod // 10

dp = [0] * fibo
dp[1] = 1

for i in range(2, fibo):
    dp[i] = (dp[i - 1] + dp[i - 2]) % mod

print(dp[n % fibo])
