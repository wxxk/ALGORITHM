import sys

sys.stdin.readline

n = int(input())
num = [int(input()) for _ in range(n)]
stack = []
ans = 0

for i in range(len(num)):
    while stack and stack[-1] <= num[i]:
        stack.pop()
    ans += len(stack)
    stack.append(num[i])
print(ans)
