import sys

sys.stdin = open("input.txt")

t = int(input())

for i in range(1, t + 1):
    n, m = map(int, input().split())
    dp = [0, 1]
    cnt = 0

    while True:
        dp.append((dp[-1] + dp[-2]) % m)
        cnt += 1
        if dp[-1] == 1 and dp[-2] == 0:
            break

    print(i, cnt)
