import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
result = []
for i in info:
    rank = 1
    for j in info:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")
