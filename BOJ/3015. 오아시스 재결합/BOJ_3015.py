"""
stack에 (height, cnt) 쌍으로
pop해서 나온 요소의 cnt만큼 ++

"""

import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
num = [int(input()) for _ in range(n)]
stack = []
ans = 0

for i in num:
    # 스택의 끝 값보다 키가 크면
    while stack and stack[-1][0] < i:
        ans += stack.pop()[1]

    # 스택이 비어있다면 append
    if not stack:
        stack.append((i, 1))
        continue

    # 스택의 끝값의 키와 같다면
    if stack[-1][0] == i:
        cnt = stack.pop()[1]
        ans += cnt

        if stack:
            ans += 1
        stack.append((i, cnt + 1))

    else:
        stack.append((i, 1))
        ans += 1


print(ans)
