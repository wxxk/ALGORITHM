from collections import deque
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    numbers = deque(list(map(int, input().split())))
    cnt = 0

    while True:
        max_num = max(numbers)
        front = numbers.popleft()
        m -= 1

        if max_num == front:
            cnt += 1
            if m < 0:
                print(cnt)
                break
        else:
            numbers.append(front)
            if m < 0:
                m = len(numbers) - 1
