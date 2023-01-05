import sys

sys.stdin = open("input.txt")

n = int(input())
nums = [0] * 301
for i in range(n):
    nums[i] = int(input())

dp = [0] * 301
dp[0] = nums[0]
dp[1] = nums[0] + nums[1]
dp[2] = max(nums[0] + nums[2], nums[1] + nums[2])

for i in range(3, n):
    dp[i] = max(dp[i - 3] + nums[i - 1] + nums[i], dp[i - 2] + nums[i])
    print(dp[i - 3] + nums[i - 1] + nums[i], dp[i - 2] + nums[i])

print(dp[n - 1])
