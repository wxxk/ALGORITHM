import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

word = input()
stack = []
res = ""
for i in word:
    if i.isalpha():
        res += i
    elif i == "(":
        stack.append(i)

    elif i == "*" or i == "/":
        while stack and (stack[-1] == "*" or stack[-1] == "/"):
            res += stack.pop()
        stack.append(i)

    # 덧셈이나 뺄셈이나 모두 내보내기
    elif i == "+" or i == "-":
        while stack and stack[-1] != "(":
            res += stack.pop()
        stack.append(i)

    elif i == ")":
        while stack and stack[-1] != "(":
            res += stack.pop()
        stack.pop()

while stack:
    res += stack.pop()
print(res)
