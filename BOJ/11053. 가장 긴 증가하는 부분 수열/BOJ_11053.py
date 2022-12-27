import sys
import bisect

sys.stdin = open("input.txt")

n = int(input())
a = list(map(int, input().split()))
result = []

for i in a:
    if result:
        if i > result[-1]:
            result.append(i)
        else:
            idx = bisect.bisect_left(result, i)
            result[idx] = i
    else:
        result.append(i)

print(len(result))
