from collections import deque
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    com = input()
    n = int(input())
    arr = deque(input().strip()[1:-1].split(","))

    if n == 0:
        arr = []

    flag = 0

    for i in com:
        if i == "R":
            flag += 1
        elif i == "D":
            if not arr:
                print("error")
                flag = True
                break
            else:
                if flag % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()

    else:
        if flag % 2 == 0:
            print("[" + ",".join(arr) + "]")
        else:
            arr.reverse()
            print("[" + ",".join(arr) + "]")
