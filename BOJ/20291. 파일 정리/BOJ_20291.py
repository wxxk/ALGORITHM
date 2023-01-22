import sys

sys.stdin = open("input.txt")

n = int(input())
file = {}


for _ in range(n):
    form = input().split(".")[1]

    if not form in file:
        file[form] = 1
    else:
        file[form] += 1

file = sorted(file.items())

for k, v in file:
    print(k, v)
