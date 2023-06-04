import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
cnt, s, start, end = 0, 0, 0, 0

while end <= n:
    if s < n:
        end += 1
        s += end
    elif s > n:
        s -= start
        start += 1
    else:
        cnt += 1
        end += 1
        s += end

print(cnt)
