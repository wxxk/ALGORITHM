import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

for i in range(1, n):
    nums[i] = max(nums[i], nums[i] + nums[i - 1])

print(max(nums))
