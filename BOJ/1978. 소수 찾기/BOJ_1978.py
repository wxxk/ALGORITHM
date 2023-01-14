import sys

sys.stdin = open("input.txt")

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
cnt = 0

for i in nums:
    if i == 1:
        continue
    else:
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            cnt += 1
print(cnt)
