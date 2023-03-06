# '('는 스택에 넣는다.
# ')'는 두가지 경우로 나뉜다.
# ')' 이전에 문자가 '('라면 레이저다. 따라서 현재 stack에 쌓인 개수 만큼 더해준다.
# ')' 이전에 문자가 ')'라면 쇠막대기 끝이다. 따라서 하나가 올때마다 하나씩만 추가해주면 된다.

import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

data = list(input())
stack = []
result = 0

for i in range(len(data)):
    if data[i] == "(":
        stack.append("(")
    elif data[i] == ")":
        if data[i - 1] == "(":
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1

print(result)
