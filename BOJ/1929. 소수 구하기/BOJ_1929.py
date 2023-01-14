# 1과 자기자신만 약수로 가지는 수

import sys

sys.stdin = open("input.txt")

input = sys.stdin.readline

n, m = map(int, input().split())

for i in range(n, m + 1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break
    else:
        print(i)
