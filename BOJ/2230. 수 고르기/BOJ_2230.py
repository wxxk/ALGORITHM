import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

n, m = map(int, input().split())
num = sorted([int(input()) for _ in range(n)])

ans = num[-1] - num[0]
start = 0
end = 0

while start < len(num) - 1:
    temp = num[end] - num[start]
    if temp >= m:  # 차이가 m이상이면서
        if ans > temp:  # 가장 작은 것
            ans = temp
        start += 1
    elif temp < m:
        if len(num) - 1 > end:
            end += 1
        else:
            start += 1

print(ans)
