import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
mem = []

for _ in range(n):
    mem.append(list(input().split()))

mem.sort(key=lambda x: int(x[0]))

for i in mem:
    print(*i)
