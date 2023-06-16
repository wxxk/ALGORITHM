import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
num = [int(input()) for _ in range(n)]
cnt = 0
stack = []
for i in num:
    while stack and stack[-1] < i:
        stack.pop()

    stack.append(i)

print(cnt)
