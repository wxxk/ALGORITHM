import sys

input = sys.stdin.readline

x, y = map(int, input().split())
z = y * 100 // x

start = 1
end = x
res = 0
if z >= 99:
    print(-1)
else:
    while start <= end:
        mid = (start + end) // 2

        if (y + mid) * 100 // (x + mid) <= z:
            start = mid + 1
        else:
            res = mid
            end = mid - 1

    print(res)
