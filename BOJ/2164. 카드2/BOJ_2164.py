from collections import deque
import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
nums = deque()

for i in range(1, n + 1):
    nums.append(i)

while len(nums) > 1:
    nums.popleft()
    nums.append(nums.popleft())

print(nums[0])
