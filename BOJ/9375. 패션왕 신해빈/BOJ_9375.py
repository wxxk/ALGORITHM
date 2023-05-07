import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    dict = {}

    for _ in range(n):
        a, b = map(str, input().split())

        if b in dict:
            dict[b] += 1

        else:
            dict[b] = 1

    cnt = 1

    for i in dict:
        cnt *= dict[i] + 1

    print(cnt - 1)
