from collections import deque
import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    s = input().strip()

    left = deque()
    right = deque()

    for i in s:
        if i == "<":
            if left:
                right.appendleft(left.pop())

        elif i == ">":
            if right:
                left.append(right.popleft())

        elif i == "-":
            if left:
                left.pop()

        else:
            left.append(i)

    print("".join(left + right))
