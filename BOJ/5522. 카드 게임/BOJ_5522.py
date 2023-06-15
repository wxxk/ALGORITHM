import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

res = 0

for i in range(5):
    res += int(input())

print(res)
