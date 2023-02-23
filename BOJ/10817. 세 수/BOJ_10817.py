import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

nums = list(map(int, input().split()))
nums.sort(reverse=True)

print(nums[1])
