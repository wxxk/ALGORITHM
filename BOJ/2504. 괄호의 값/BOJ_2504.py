import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

back = list(input())
stack = []
temp = 1
answer = 0

for i in range(len(back)):
    if back[i] == "(":
        stack.append(back[i])
        temp *= 2

    elif back[i] == "[":
        stack.append(back[i])
        temp *= 3

    elif back[i] == ")":
        if not stack or stack[-1] != "(":
            answer = 0
            break
        if back[i - 1] == "(":
            answer += temp
        stack.pop()
        temp //= 2

    elif back[i] == "]":
        if not stack or stack[-1] != "[":
            answer = 0
            break
        if back[i - 1] == "[":
            answer += temp

        stack.pop()
        temp //= 3

if stack:
    print(0)
else:
    print(answer)
