# import sys
# sys.stdin = open('input.txt')

n = int(input())
m = int(input())
vip = [int(input()) for _ in range(m)]

dp = [0] * (41)
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = dp[i-2] + dp[i-1]

answer = 1
start = 0

for i in range(m):
    end = vip[i]
    answer *= dp[end - start - 1]
    # print(start, end-1)
    start = end

# print(n, start)
answer *= dp[n-start]
print(answer)