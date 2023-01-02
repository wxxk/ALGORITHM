import sys
sys.stdin = open('input.txt')

import heapq

n = int(input())
nums = []
cnt = 0
count =0

for i in range(n):
    x, y = map(int, input().split())    
    heapq.heappush(nums, (y, x))

while nums:
    a, b = heapq.heappop(nums)
    if b >= cnt:
        cnt = a
        count +=1

print(count)
