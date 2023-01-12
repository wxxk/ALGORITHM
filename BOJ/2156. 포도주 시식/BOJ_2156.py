import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
arr = [0]

for i in range(n):
    arr.append(int(input()))

dp = [0]
dp.append(arr[1])

if n > 1:
    dp.append(arr[1] + arr[2])

for i in range(3, n + 1):
    dp.append(max(dp[i - 1], dp[i - 3] + arr[i - 1] + arr[i], dp[i - 2] + arr[i]))

print(dp)
