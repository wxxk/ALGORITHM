import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
number = deque(enumerate(map(int, input().split()), start=1))
ans = []

while number:
    idx, num = number.popleft()
    ans.append(idx)

    if num > 0:
        number.rotate(-(num - 1))

    elif num < 0:
        number.rotate(-num)

print(*ans)
