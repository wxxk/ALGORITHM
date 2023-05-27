import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

s = input()
n = len(s)
result = set()

for i in range(n):
    for j in range(i + 1, n + 1):
        result.add(s[i:j])

print(len(result))
