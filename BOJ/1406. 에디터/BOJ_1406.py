import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

stack_1 = list(map(str, input().strip()))
stack_2 = []
m = int(input())
n = len(stack_1)

for i in range(m):
    x = input().strip()

    if x[0] == "P":
        stack_1.append(x[2])

    elif x[0] == "L" and stack_1:
        stack_2.append(stack_1.pop())

    elif x[0] == "D" and stack_2:
        stack_1.append(stack_2.pop())

    elif x[0] == "B" and stack_1:
        stack_1.pop()

print("".join(stack_1 + list(reversed(stack_2))))
