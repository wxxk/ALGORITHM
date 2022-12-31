import sys

sys.stdin = open("input.txt")

n = int(input())
result = []

for i in range(n):
    num = int(input())
    if num:
        result.append(num)
    else:
        result.pop()

print(sum(result))
