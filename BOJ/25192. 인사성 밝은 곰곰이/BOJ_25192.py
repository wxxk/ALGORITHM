import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
hello = {}
sum = 0
for i in range(n):
    word = input().strip()
    if word == "ENTER":
        for k, v in hello.items():
            if v == 1:
                sum += 1
        hello = {}
        continue
    elif word not in hello:
        hello[word] = 1

for k, v in hello.items():
    if v == 1:
        sum += 1

print(sum)
