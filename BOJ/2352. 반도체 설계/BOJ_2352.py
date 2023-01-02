import sys
sys.stdin = open('input.txt')
from bisect import bisect_left

n = int(input())
nums = list(map(int, input().split()))
result = []

for i in nums:
    if result:
        if result[-1] < i:
            result.append(i)
        else:
            idx = bisect_left(result, i)
            result[idx] = i

    else:
        result.append(i)

print(len(result))