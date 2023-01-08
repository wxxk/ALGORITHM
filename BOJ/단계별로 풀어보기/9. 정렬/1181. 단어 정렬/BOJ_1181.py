import sys

sys.stdin = open("input.txt")

n = int(input())

result = [input() for _ in range(n)]

result = set(result)
result = list(result)
result.sort()
result.sort(key=len)

for i in result:
    print(i)
