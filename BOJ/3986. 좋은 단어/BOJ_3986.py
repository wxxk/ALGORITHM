import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
ans = 0

for i in range(n):
    word = input().strip()
    stack = []
    for j in word:
        if not stack:
            stack.append(j)
        else:
            if stack[-1] == j:
                stack.pop()
            else:
                stack.append(j)

    if not stack:
        ans += 1

print(ans)
