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
    # 1. 시작점 ~ 첫 VIP석 사이 일반석의 갯수
    # 2. VIP석과 VIP석 사이 일반석 갯수
    end = vip[i]
    answer *= dp[end - start - 1]
    start = end

# 3. 마지막 VIP석과 마지막점 사이 일반석의 갯수
answer *= dp[n-start]
print(answer)