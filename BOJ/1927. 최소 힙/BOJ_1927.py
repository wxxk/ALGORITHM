from heapq import heappush, heappop
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
q = []

for i in range(n):
    x = int(input())
    if x == 0:
        if not q:
            print(0)
        else:
            print(heappop(q))
    else:
        heappush(q, x)
